#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Arno0x0x, Twitter: @Arno0x0x
# 本项目将python2代码修改为python3


import argparse
from Crypto.Hash import MD5
from Crypto.Cipher import AES
import pyscrypt
from base64 import b64encode
from os import urandom
from string import Template
import os

templates = {
	'cpp': './templates/encryptedShellcodeWrapper.cpp',
	'csharp': './templates/encryptedShellcodeWrapper.cs',
	'python': './templates/encryptedShellcodeWrapper.py'
}

resultFiles = {
	'cpp': './result/encryptedShellcodeWrapper.cpp',
	'csharp': './result/encryptedShellcodeWrapper.cs',
	'python': './result/encryptedShellcodeWrapper.py'
}

#======================================================================================================
#											CRYPTO FUNCTIONS
#======================================================================================================

#------------------------------------------------------------------------
# data as a bytearray
# key as a string
def xor(data, key):
	l = len(key)
	keyAsInt = list(map(ord, key))
	return bytes(bytearray((
	    (data[i] ^ keyAsInt[i % l]) for i in range(0,len(data))
	)))

#------------------------------------------------------------------------
def pad(s):
	"""PKCS7 padding"""
	return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

#------------------------------------------------------------------------
def aesEncrypt(clearText, key):
	"""Encrypts data with the provided key.
	The returned byte array is as follow:
	:==============:==================================================:
	: IV (16bytes) :    Encrypted (data + PKCS7 padding information)  :
	:==============:==================================================:
	"""

	# Generate a crypto secure random Initialization Vector
	iv = urandom(AES.block_size)

	# Perform PKCS7 padding so that clearText is a multiple of the block size
	clearText = pad(clearText)

	cipher = AES.new(key, AES.MODE_CBC, iv)
	return iv + cipher.encrypt(bytes(clearText))

#======================================================================================================
#											OUTPUT FORMAT FUNCTIONS
#======================================================================================================
def convertFromTemplate(parameters, templateFile):
	try:
		with open(templateFile) as f:
			src = Template(f.read())
			result = src.substitute(parameters)
			f.close()
			return result
	except IOError:
		print(color("[!] Could not open or read template file [{}]".format(templateFile)))
		return None

#------------------------------------------------------------------------
# data as a bytearray
def formatCPP(data, key, cipherType):
	shellcode = "\\x"
	shellcode += "\\x".join(format(b,'02x') for b in data)
	result = convertFromTemplate({'shellcode': shellcode, 'key': key, 'cipherType': cipherType}, templates['cpp'])

	if result != None:
		try:
			fileName = os.path.splitext(resultFiles['cpp'])[0] + "_" + cipherType + os.path.splitext(resultFiles['cpp'])[1]
			with open(fileName,"w+") as f:
				f.write(result)
				f.close()
				print(color("[+] C++ code file saved in [{}]".format(fileName)))
		except IOError:
			print(color("[!] Could not write C++ code  [{}]".format(fileName)))

#------------------------------------------------------------------------
# data as a bytearray
def formatCSharp(data, key, cipherType):
	shellcode = '0x'
	shellcode += ',0x'.join(format(b,'02x') for b in data)
	result = convertFromTemplate({'shellcode': shellcode, 'key': key, 'cipherType': cipherType}, templates['csharp'])

	if result != None:
		try:
			fileName = os.path.splitext(resultFiles['csharp'])[0] + "_" + cipherType + os.path.splitext(resultFiles['csharp'])[1]
			with open(fileName,"w+") as f:
				f.write(result)
				f.close()
				print(color("[+] C# code file saved in [{}]".format(fileName)))
		except IOError:
			print(color("[!] Could not write C# code  [{}]".format(fileName)))

#------------------------------------------------------------------------
# data as a bytearray
def formatPy(data, key, cipherType):
	shellcode = '\\x'
	shellcode += '\\x'.join(format(b,'02x') for b in data)
	result = convertFromTemplate({'shellcode': shellcode, 'key': key, 'cipherType': cipherType}, templates['python'])

	if result != None:
		try:
			fileName = os.path.splitext(resultFiles['python'])[0] + "_" + cipherType + os.path.splitext(resultFiles['python'])[1]
			with open(fileName,"w+") as f:
				f.write(result)
				f.close()
				print(color("[+] Python code file saved in [{}]".format(fileName)))
		except IOError:
			print(color("[!] Could not write Python code  [{}]".format(fileName)))

#------------------------------------------------------------------------
# data as a bytearray
def formatB64(data):
	return b64encode(data)

#======================================================================================================
#											HELPERS FUNCTIONS
#======================================================================================================

#------------------------------------------------------------------------
def color(string, color=None):
    """
    Author: HarmJ0y, borrowed from Empire
    Change text color for the Linux terminal.
    """
    
    attr = []
    # bold
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

    else:
        if string.strip().startswith("[!]"):
            attr.append('31')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[+]"):
            attr.append('32')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[?]"):
            attr.append('33')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[*]"):
            attr.append('34')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        else:
            return string

#======================================================================================================
#											MAIN FUNCTION
#======================================================================================================
if __name__ == '__main__':
	#------------------------------------------------------------------------
	# Parse arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("shellcodeFile", help="File name containing the raw shellcode to be encoded/encrypted")
	parser.add_argument("key", help="Key used to transform (XOR or AES encryption) the shellcode")
	parser.add_argument("encryptionType", help="Encryption algorithm to apply to the shellcode", choices=['xor','aes'])
	parser.add_argument("-b64", "--base64", help="Display transformed shellcode as base64 encoded string", action="store_true")
	parser.add_argument("-cpp", "--cplusplus", help="Generates C++ file code", action="store_true")
	parser.add_argument("-cs", "--csharp", help="Generates C# file code", action="store_true")
	parser.add_argument("-py", "--python", help="Generates Python file code", action="store_true")
	args = parser.parse_args() 

	#------------------------------------------------------------------------------
	# Check that required directories and path are available, if not create them
	if not os.path.isdir("./result"):
		os.makedirs("./result")
		print(color("[+] Creating [./result] directory for resulting code files"))

	#------------------------------------------------------------------------
	# Open shellcode file and read all bytes from it
	try:
		with open(args.shellcodeFile,'rb') as shellcodeFileHandle:
			shellcodeBytes = bytearray(shellcodeFileHandle.read())
			shellcodeFileHandle.close()
			print(color("[*] Shellcode file [{}] successfully loaded".format(args.shellcodeFile)))
	except IOError:
		print(color("[!] Could not open or read file [{}]".format(args.shellcodeFile)))
		quit()

	print(color("[*] MD5 hash of the initial shellcode: [{}]".format(MD5.new(shellcodeBytes).hexdigest())))
	print(color("[*] Shellcode size: [{}] bytes".format(len(shellcodeBytes))))

	#------------------------------------------------------------------------
	# Perform AES128 transformation
	if args.encryptionType == 'aes':
		# Derive a 16 bytes (128 bits) master key from the provided key
		key = pyscrypt.hash(args.key, "saltmegood", 1024, 1, 1, 16)
		masterKey = formatB64(key)
		print(color("[*] AES encrypting the shellcode with 128 bits derived key [{}]".format(masterKey)))
		transformedShellcode = aesEncrypt(shellcodeBytes, key)
		cipherType = 'aes'

	#------------------------------------------------------------------------
	# Perform XOR transformation
	elif args.encryptionType == 'xor':
		masterKey = args.key
		print(color("[*] XOR encoding the shellcode with key [{}]".format(masterKey)))
		transformedShellcode = xor(shellcodeBytes, masterKey)
		cipherType = 'xor'

	#------------------------------------------------------------------------
	# Display interim results
	print("\n==================================== RESULT ====================================\n")
	print(color("[*] Encrypted shellcode size: [{}] bytes".format(len(transformedShellcode))))
	#------------------------------------------------------------------------
	# Display formated output
	if args.base64:
		print(color("[*] Transformed shellcode as a base64 encoded string")	)
		print(formatB64(transformedShellcode))
		print("")
	
	if args.cplusplus:
		print(color("[*] Generating C++ code file"))
		formatCPP(transformedShellcode, masterKey, cipherType)
		print("")
		

	if args.csharp:
		print(color("[*] Generating C# code file"))
		formatCSharp(transformedShellcode, masterKey, cipherType)
		print("")

	if args.python:
		print(color("[*] Generating Python code file"))
		formatPy(transformedShellcode, masterKey, cipherType)
		print("")
