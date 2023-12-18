# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2023/8/29 10:35
# @Function: Godzilla JSP Raw Shell 流量解密脚本

import base64
import zlib
from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 32
def aes_decode(data, key):
    try:
        aes = AES.new(str.encode(key), AES.MODE_ECB)
        decrypted_text = aes.decrypt(pad(data,BLOCK_SIZE))
        decrypted_text = decrypted_text[:-(decrypted_text[-1])]
    except Exception as e:
        print(e)
    return decrypted_text


# key 示例：12340xxxx1901234
# s 示例：c5144463f178b352c5xxxxxxxxxxxxx528ebfc4a79b03aea0e31c
key = "<YOUR_KEY_HERE>"
s = "<YOUR_RAW_STRING_HERE>"
s = binascii.a2b_hex(s)
s = aes_decode(s,key)
print(s)
s = base64.b64encode(zlib.decompress(s,30))
print(base64.b64decode(s))
