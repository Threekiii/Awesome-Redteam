# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2022/11/07 19:40
# @Function: 弱密码转NTLM Hash

import sys
import getpass
import hashlib
import binascii

def main():
    print('+--------------------------------------------------')
    print('+  \033[34m弱密码转NTLM Hash      \033[0m')
    print('+  \033[34m1. 请修改对应弱密码文件名，例如：top_1000_passwd.txt      \033[0m')
    print('+  \033[34m2. 请修改对应输出文件名，例如：top_1000_ntlm.txt      \033[0m')
    print('+--------------------------------------------------')
    print('+  \033[34m正在转换...\033[0m')
    try:
        with open('top_100_passwd.txt','r',encoding='utf-8') as fr:
            content = fr.read().split()

        result = []
        for p in content:
            hash = hashlib.new('md4', p.encode('utf-16le')).digest()
            ntlm_hash = binascii.hexlify(hash).upper().decode()
            result.append('{}\t{}\n'.format(p,ntlm_hash))
            # print(ntlm_hash)

        with open('top_100_ntlm_hash.txt','w',encoding='utf-8') as fw:
            fw.writelines(result)
    except:
        print('+  \033[31m发生错误.\033[0m')
    else:
        print('+  \033[36m转换完成.\033[0m')


if __name__ == '__main__':
    main()


