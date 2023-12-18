# CobaltStrike流量分析

参考链接：

- 浅析CobaltStrike流量解密 https://5ime.cn/cobaltstrike-decrypt.html

## 流量特征

http-beacon 通信中，默认使用 GET 方法向 `/dpixel` 、`/__utm.gif` 、`/pixel.gif` 等地址发起请求，同时，Cobalt Strike 的 Beacon 会将元数据（例如AES密钥）使用 RSA 公钥加密后发送给 C2 服务器。这些元数据通常被编码为 Base64 字符串并作为 Cookie 发送。

![](images/CobaltStrike流量分析/image-20231124103813576.png)

下发指令的时候会请求 `/submit.php?id=一串数字` ，同时 POST 传递一串 0000 开头的16进制数据。

过滤 POST 请求包：

```
http.request.method==POST
```

![](images/CobaltStrike流量分析/image-20231124104222437.png)


https-beacon 通信中，默认使用空证书建立加密通道。

过滤 TLS 协议：

```
tls
```

![](images/CobaltStrike流量分析/image-20231124105107971.png)

JA3 / JA3S 可以为客户端和服务器之间的通信创建 SSL 指纹。唯一签名可以表示从 Client Hello 数据包中的字段收集的几个值：

- SSL Version
- Accepted Ciphers
- List of Extensions
- Elliptic Curves
- Elliptic Curve Formats

几个已知的 `ja3` / `ja3s` 指纹信息，不同操作系统上是不一样的：

```
JA3

72a589da586844d7f0818ce684948eea
a0e9f5d64349fb13191bc781f81f42e1
```

```
JA3s

b742b407517bac9536a77a7b0fee28e9
ae4edc6faf64d08308082ad26be60767
```
## 流量解密

 `.cobaltstrike.beacon_keys` 文件，该文件本质上为 `KeyPair` 的 Java 对象，Python 的 `javaobj-py3` 库可以直接读取里面存储的数据。

获取 `.cobaltstrike.beacon_keys` 文件中的 `RSA` 私钥，用于解密元数据：

```python
import base64  
import javaobj.v2 as javaobj  
  
with open(".cobaltstrike.beacon_keys", "rb") as fd:  
pobj = javaobj.load(fd)  
  
def format_key(key_data, key_type):  
key_data = bytes(map(lambda x: x & 0xFF, key_data))  
formatted_key = f"-----BEGIN {key_type} KEY-----\n"  
formatted_key += base64.encodebytes(key_data).decode()  
formatted_key += f"-----END {key_type} KEY-----"  
return formatted_key  
  
privateKey = format_key(pobj.array.value.privateKey.encoded.data, "PRIVATE")  
publicKey = format_key(pobj.array.value.publicKey.encoded.data, "PUBLIC")  
  
print(privateKey)  
print(publicKey)
```

通过私钥解密元数据，获取 `AES KEY`，其中 `encode_data` 为元数据，也就是前面提到的 `cookie` 的值。

`Cobalt Strike` 的 `Beacon` 通信主要依赖于 `AES key` 和 `HMAC key` 。这两个密钥都是由 `Beacon` 在每次执行时随机生成的 16字节数据。

- `AES key`：这个密钥用于加密和解密 `Beacon` 与 `C2` 服务器之间的通信内容。具体来说，它用于 `AES` 算法，该算法用于加密和解密Beacon任务的传输。

- `HMAC key` ：这个密钥用于验证数据的完整性和真实性。`HMAC` （Hash-based Message Authentication Code）是一种基于密钥的哈希算法，用于在不安全的通信环境中验证消息的完整性和真实性。
- 
获取 `AES key` 和 `HMAC key`：

```python
import hashlib  
from Crypto.PublicKey import RSA  
from Crypto.Cipher import PKCS1_v1_5  
import base64  
import hexdump  
PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----  
{}  
-----END PRIVATE KEY-----"""  
  
encode_data = ""  
  
private_key = RSA.import_key(PRIVATE_KEY.encode())  
  
cipher = PKCS1_v1_5.new(private_key)  
ciphertext = cipher.decrypt(base64.b64decode(encode_data), 0)  
  
if ciphertext[0:4] == b'\x00\x00\xBE\xEF':  
raw_aes_keys = ciphertext[8:24]  
raw_aes_hash256 = hashlib.sha256(raw_aes_keys).digest()  
aes_key = raw_aes_hash256[0:16]  
hmac_key = raw_aes_hash256[16:]  
  
print("AES key: {}".format(aes_key.hex()))  
print("HMAC key: {}".format(hmac_key.hex()))  
  
hexdump.hexdump(ciphertext)
```

解密 `submit.php` 传递的 Data 。首先要先对该串16进制数据进行处理，转字符串后进行 `Base64` 编码：

```python
import base64  
  
encode_data = ''  
  
bytes_data = bytes.fromhex(encode_data)  
encrypt_data = base64.b64encode(bytes_data)  
  
print(encrypt_data.decode())
```

最终分别填入 `SHARED_KEY`，`HMAC_KEY`，`encrypt_data` 即可：

```python
import hmac  
import binascii  
import base64  
import hexdump  
from Crypto.Cipher import AES  
  
SHARED_KEY = binascii.unhexlify("")  
HMAC_KEY = binascii.unhexlify("")  
encrypt_data = ""  
  
def decrypt(encrypted_data, iv_bytes, signature, shared_key, hmac_key):  
if hmac.new(hmac_key, encrypted_data, digestmod="sha256").digest()[:16] != signature:  
print("message authentication failed")  
return  
  
cipher = AES.new(shared_key, AES.MODE_CBC, iv_bytes)  
return cipher.decrypt(encrypted_data)  
  
encrypt_data = base64.b64decode(encrypt_data)  
encrypt_data_length = int.from_bytes(encrypt_data[:4], byteorder='big', signed=False)  
encrypt_data_l = encrypt_data[4:]  
  
data1 = encrypt_data_l[:encrypt_data_length-16]  
signature = encrypt_data_l[encrypt_data_length-16:encrypt_data_length]  
iv_bytes = b"abcdefghijklmnop"  
  
dec = decrypt(data1, iv_bytes, signature, SHARED_KEY, HMAC_KEY)  
  
print("counter: {}".format(int.from_bytes(dec[:4], byteorder='big', signed=False)))  
print("任务返回长度: {}".format(int.from_bytes(dec[4:8], byteorder='big', signed=False)))  
print("任务输出类型: {}".format(int.from_bytes(dec[8:12], byteorder='big', signed=False)))  
print(dec[12:int.from_bytes(dec[4:8], byteorder='big', signed=False)])  
print(hexdump.hexdump(dec))
```

综合了以上流程的 CobaltStrike 流量解密脚本：

```
file_path = ".cobaltstrike.beacon_keys路径"
encode_data = "元数据"
encrypt_data = "任务数据"
```

```python
import hmac
import base64
import hashlib
import hexdump
import binascii
import javaobj.v2 as javaobj
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

file_path = ".cobaltstrike.beacon_keys"
encode_data = "PcdKQuOPNdlyJMzB9IdLt3FyYJK5ooh2hagReIiCPX3enVE8IUWclknGedXTxAW6Seq0pUuqbA3d6h59a43lQH+2l4egkNL/aTuaMndjIcrM7HFHDQSumu/VoeG+O9vNB63W6YtJDidYt+SjFCZPOjcTblEU+CDGzN4xNO+bh1s="
encrypt_data = "000000c0cc3581241436712c84735d65bf5faa7ac3da1ac1b7583bea79d54c00c517866397786623818cb11af81460bf963e7da0be7bd4c8afc27d4d7efb783ce7d3a889d14dada2a851f0b2919af4242efdc0e43ad80053b5d7ffc933416ec0861d24280f6d80bf6baf39264c534296b81635f8b2ce9824f03839f1aa4a2941186bed40820296e5637b168ad6bac0801c6c79e2c63f0319e9b12434854c0721cc34a323f044b630b2796478f6802590774d1a83f769fb1e2bfb1c577bfe02d958f5b41c"

def format_key(key_data):
    key_data = bytes(map(lambda x: x & 0xFF, key_data))
    formatted_key = f"-----BEGIN PRIVATE KEY-----\n"
    formatted_key += base64.encodebytes(key_data).decode()
    formatted_key += f"-----END PRIVATE KEY-----"
    return formatted_key

def decrypt(encrypted_data, iv_bytes, signature, shared_key, hmac_key):
    if hmac.new(hmac_key, encrypted_data, digestmod="sha256").digest()[:16] != signature:
        print("message authentication failed")
        return

    cipher = AES.new(shared_key, AES.MODE_CBC, iv_bytes)
    return cipher.decrypt(encrypted_data)

with open(file_path, "rb") as fd:
    pobj = javaobj.load(fd)

PRIVATE_KEY = format_key(pobj.array.value.privateKey.encoded.data)
private_key = RSA.import_key(PRIVATE_KEY.encode())
cipher = PKCS1_v1_5.new(private_key)
ciphertext = cipher.decrypt(base64.b64decode(encode_data), 0)

if ciphertext[0:4] == b'\x00\x00\xBE\xEF':
    raw_aes_keys = ciphertext[8:24]
    raw_aes_hash256 = hashlib.sha256(raw_aes_keys).digest()
    aes_key = raw_aes_hash256[0:16]
    hmac_key = raw_aes_hash256[16:]

SHARED_KEY = binascii.unhexlify(aes_key.hex())
HMAC_KEY = binascii.unhexlify(hmac_key.hex())

encrypt_data = base64.b64encode(bytes.fromhex(encrypt_data)).decode()
encrypt_data = base64.b64decode(encrypt_data)
encrypt_data_length = int.from_bytes(encrypt_data[:4], byteorder='big', signed=False)
encrypt_data_l = encrypt_data[4:]
data1 = encrypt_data_l[:encrypt_data_length-16]
signature = encrypt_data_l[encrypt_data_length-16:encrypt_data_length]
iv_bytes = b"abcdefghijklmnop"

dec = decrypt(data1, iv_bytes, signature, SHARED_KEY, HMAC_KEY)
print("AES key: {}".format(aes_key.hex()))
print("HMAC key: {}".format(hmac_key.hex()))
print(dec[12:int.from_bytes(dec[4:8], byteorder='big', signed=False)])
print(hexdump.hexdump(dec))
```
