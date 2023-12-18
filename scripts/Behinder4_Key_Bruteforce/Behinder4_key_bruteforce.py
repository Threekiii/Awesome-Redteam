# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2023/12/11 16:04


import base64
import hashlib
from Crypto.Cipher import AES


def ecb_decode(data, key):
    try:
        aes = AES.new(str.encode(key), AES.MODE_ECB)
        decrypted_text = aes.decrypt(data)
        decrypted_text = decrypted_text[:-(decrypted_text[-1])]
    except Exception as e:
        print(e)
    else:
        return decrypted_text.decode()

def cbc_decode(data, key):
    try:
        aes = AES.new(str.encode(key), mode=AES.MODE_CBC, iv=b'\x00' * 16)
        decrypted_text = aes.decrypt(data)
        decrypted_text = decrypted_text[:-(decrypted_text[-1])]
    except Exception as e:
        print(e)
    else:
        return decrypted_text.decode()

def base64_decode(data):
    res = base64.b64decode(data.strip()).decode('utf-8', "ignore")
    print(res)
    return res

def md5_truncate(key):
    return hashlib.md5(key.encode()).hexdigest()[:16]

if __name__ == '__main__':
    data = b'''<BASE64_ENCODED_ENCRYPTED_DATA_HERE>'''
    with open('key.txt', 'r', encoding='utf-8') as f:
        keys = f.readlines()

    for key in keys:
        key = key.strip()
        c2_key = md5_truncate(key)
        print('[CURRENT KEY]\t{} {}'.format(key,c2_key))
        try:
            data_b64_decode = base64.b64decode(data.strip())
            data_ecb_decode = ecb_decode(data_b64_decode, c2_key)
            if data_ecb_decode:
                print('[Ooooops, We found it!]')
                print(data_ecb_decode)
                break
        except Exception as e:
            pass

        try:
            data_b64_decode = base64.b64decode(data.strip())
            data_cbc_decode = cbc_decode(data_b64_decode, c2_key)
            if data_cbc_decode:
                print('[Ooooops, We found it!]')
                print(data_cbc_decode)
                break
        except Exception as e:
            pass