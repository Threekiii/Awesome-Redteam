# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2022/5/27 19:40
# @Function: 杀软进程检测

import re
import os
import subprocess

def banner():
    print('+--------------------------------------------------')
    print('+  \033[36m@Function: 杀软进程检测      \033[0m')
    print('+  \033[36m@Author  : Threekiii                               \033[0m')
    print('+  \033[31m代码仅供学习，任何人不得将其用于非法用途，否则后果自行承担。  \033[0m')
    print('+--------------------------------------------------')

def check():
    antivirus_list = []
    with open('process.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    try:
        print('+  \033[34m正在执行tasklist命令,当前路径: {}\033[0m'.format(os.path.abspath(os.path.dirname(__file__))))
        tmp = subprocess.check_output('tasklist', shell=True).decode()
        tasklist = ''.join(re.findall('.*=(.*)', tmp, re.S)).strip().split('\r\n')
        print('+  \033[34m正在执行杀软进程检测...\033[0m')
        for task in tasklist:
            taskname = task.split()[0]
            for process in content:
                processname = process.strip('\n').split('\"')[1]
                if taskname == processname:
                    result = process.strip('\n').split('\"')[3]
                    antivirus_list.append('+  \033[31m存在进程：{}, 对应杀软：{}\033[0m'.format(processname, result))
        print('\n+  \033[31m[检测完成]   \033[0m')
        for al in antivirus_list:
            print(al)
    except Exception as e:
        print('\n+  \033[31m[出现异常] {}\033[0m'.format(e))

def run():
    banner()
    check()

if __name__ == '__main__':
    run()





