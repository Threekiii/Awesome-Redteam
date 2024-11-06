# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2024-10-22 11:13:18
# @Function: Godzilla JAVA_AES_BASE64 Traffic Decryption

import base64
import string
import gzip
import binascii
from Crypto.Cipher import AES
from urllib.parse import unquote

def aes_decode(hex_string):
    bytes_string = binascii.a2b_hex(hex_string)
    aes = AES.new(str.encode(key), AES.MODE_ECB)
    aes_decrypt_string = aes.decrypt(bytes_string)
    aes_decrypt_string = aes_decrypt_string[:-(aes_decrypt_string[-1])]
    return aes_decrypt_string

def cprint(s):
    print(cyan+s+reset)

def request_decode(base64_string):
    """
    # 1. Extract Data and URL Decode
    # 2. Base64 Decode -> Hex
    # 3. AES Decryption
    # 4. Gunzip
    # 5. Filter Invisible Characters
    """

    # 1. Extract Data and URL Decode
    base64_string = unquote(base64_string)
    cprint("[STEP 1] Extract Data and URL Decode")
    print(base64_string)

    # 2. Base64 Decode -> Hex
    hex_string = base64.b64decode(base64_string.replace(password + "=", '')).hex()
    cprint("[STEP 2] Base64 Decode -> Hex")
    print(hex_string)


    # 3. AES Decryption
    aes_decrypt_string = aes_decode(hex_string)
    cprint("[STEP 3] AES Decryption")
    print(aes_decrypt_string.hex())

    # 4. Gunzip
    s = gzip.decompress(aes_decrypt_string).decode('utf8')
    cprint("[STEP 4] Gunzip")
    print(s)

    # 5. Filter Invisible Characters
    s = ''.join(filter(lambda x: x in string.printable, s))
    cprint("[STEP 5] Filter Invisible Characters")
    print(s)
    return s

def response_decode(base64_string):
    """
    # 1. Extract Data
    # 2. Base64 Decode -> Hex
    # 3. AES Decryption
    # 4. Gunzip
    # 5. Filter Invisible Characters
    """
    # 1. Extract Data
    base64_string = base64_string[16:-16]
    cprint("[STEP 1] Extract Data and URL Decode")
    print(base64_string)

    # 2. Base64 Decode -> Hex
    hex_string = base64.b64decode(base64_string).hex()
    cprint("[STEP 2] Base64 Decode -> Hex")
    print(hex_string)

    # 3. AES Decryption
    aes_decrypt_string = aes_decode(hex_string)
    cprint("[STEP 3] AES Decryption")
    print(aes_decrypt_string.hex())

    # 4. Gunzip
    s = gzip.decompress(aes_decrypt_string).decode('utf8')
    cprint("[STEP 4] Gunzip")
    print(s)

    # 5. Filter Invisible Characters
    s = ''.join(filter(lambda x: x in string.printable, s))
    cprint("[STEP 5] Filter Invisible Characters")
    print(s)
    return s

if __name__ == '__main__':
    password = "7f0e6f"
    key = "1710acba6220f62b"
    cyan = "\u001b[36m"
    yellow = "\u001b[33m"
    reset = "\u001b[0m"

    print(yellow + "===================== [REQUEST DATA DECRYPTION DETAILS] =====================" + reset)

    # Request Data Decryption
    req_base64_string = "7f0e6f=NrJ21IQ%2B5%2F5jh%2FC6iENFuzLG4QSyoIln8DjyLlej12aZxFNdvxRse%2F8UpTNrR%2FZAXX%2B%2FMj8PTkUyArg9LjASUWUNP8kwRBs1nEZJg6QW1FPflVogF8TiJoaTQKm%2BrGIR%2BS2iSMgsgHdPAFEHM3Po91H5UcZECdkNerEjPO8ueuk1NJ0EuO%2B13DXJUYC79ZgYt0py9nvCAOvgpSAAsBrwWQ%3D%3D"
    req_data = request_decode(req_base64_string)

    print(yellow + "\n===================== [RESPONSE DATA DECRYPTION DETAILS] =====================" + reset)
    # Response Data Decryption
    res_base64_string = "B333AF03A314E0FBgsHdfc8+H+CXoS9AxfQOJA2wfAON7mA0Bh8Uj9S1dz9Uzz7rEVdkGAQ4e2iW2kny0F00BC7E2672E1F5"
    res_data = response_decode(res_base64_string)

    print(yellow + "\n=========================== [REQUEST & RESPONSE] ===========================" + reset)
    cprint("[REQUEST DATA]")
    print(reset + req_data)
    cprint("[RESPONSE DATA]")
    print(reset + res_data)