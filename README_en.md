# Awesome-Redteam

<p align="left">
  <a href="https://github.com/Threekiii/Awesome-Redteam">
    <img src="https://badgen.net/github/stars/Threekiii/Awesome-Redteam?color=yellow&icon=github" alt="stars">
  </a>
  <a href="https://github.com/Threekiii/Awesome-POC">
    <img src="https://badgen.net/github/forks/Threekiii/Awesome-Redteam?color=blue&icon=github" alt="forks">
  </a>
  <a href="https://github.com/Threekiii/Awesome-POC">
    <img src="https://badgen.net/github/last-commit/Threekiii/Awesome-Redteam?color=green" alt="last-commit">
  </a>
</p>

**❗Disclaimer: The technologies, concepts, and tools provided in this Git repository are intended for educational and research purposes only. Any use for illegal activities, unauthorized penetration testing, or commercial purposes is strictly prohibited. Please read the [Awesome-Laws](https://github.com/Threekiii/Awesome-Laws) before using this repository.**

📖 _A knowledge base for red teaming and offensive security._

👍 means recommand

## _Roadmap_

![](images/README/Awesome-Redteam-20260302.png)

## Contents

- [Open-Source Navigation](#open-source-navigation)
	- [Cryptography](#cryptography)
		- [Online Tools](#online-tools)
		- [Offline Tools](#offline-tools)
		- [Encode/Decode](#encodedecode)
		- [Regular Expressions](#regular-expressions)
		- [Hash Algorithms](#hash-algorithms)
		- [RSA](#rsa)
		- [SM Algorithms](#sm-algorithms)
	- [Cyberspace Search Engine](#cyberspace-search-engine)
		- [Nice Tools](#nice-tools)
		- [Web/Ports](#webports)
		- [Google Hacking](#google-hacking)
		- [GitHub Dork](#github-dork)
	- [Open-Source Intelligence](#open-source-intelligence)
		- [Nice Tools](#nice-tools)
		- [Threat Intelligence](#threat-intelligence)
		- [Disclosed Vulnerabilities](#disclosed-vulnerabilities)
		- [API Search](#api-search)
		- [Source Code Search](#source-code-search)
	- [Open-Source Resources](#open-source-resources)
		- [Communities/Knowledge Base](#communitiesknowledge-base)
		- [Mindmap/Cheat Sheets](#mindmapcheat-sheets)
		- [Red Teaming and Offensive Security](#red-teaming-and-offensive-security)
		- [Blue Teaming and Defensive Security](#blue-teaming-and-defensive-security)
		- [Operation Security](#operation-security)
		- [Learning and Practice Platforms](#learning-and-practice-platforms)
- [Reconnaissance](#reconnaissance)
	- [Nice Tools](#nice-tools)
	- [IP/Domain/Subdomain](#ipdomainsubdomain)
	- [Fingerprint](#fingerprint)
		- [Fingerprint Collection](#fingerprint-collection)
		- [Fingerprint Reconnaissance](#fingerprint-reconnaissance)
		- [Waf Checks](#waf-checks)
	- [Brute Force](#brute-force)
		- [Brute Force Tools](#brute-force-tools)
		- [Brute Force Dictionaries](#brute-force-dictionaries)
		- [Generate a Custom Dictionary](#generate-a-custom-dictionary)
		- [Default Credentials](#default-credentials)
	- [Social Engineering](#social-engineering)
		- [Leaked Credentials](#leaked-credentials)
		- [Email](#email)
		- [SMS Online](#sms-online)
		- [Phishing](#phishing)
	- [Mobile](#mobile)
- [Vulnerability Research](#vulnerability-research)
	- [Vulnerable Environments](#vulnerable-environments)
		- [Basic Vulnerabilities](#basic-vulnerabilities)
		- [Comprehensive Vulnerabilities](#comprehensive-vulnerabilities)
		- [Vulnerable IoT Environment](#vulnerable-iot-environment)
		- [Vulnerable Active Directory Environment](#vulnerable-active-directory-environment)
		- [Vulnerable Cloud Environments](#vulnerable-cloud-environments)
		- [Vulnerable AI Environments](#vulnerable-ai-environments)
	- [Proof of Concept](#proof-of-concept)
		- [PoC/ExP](#pocexp)
		- [PoC Templates](#poc-templates)
- [Vulnerability Exploits](#vulnerability-exploits)
	- [Nice Tools](#nice-tools)
	- [Code Audit](#code-audit)
	- [Serialization](#serialization)
		- [Java](#java)
	- [Deserialization](#deserialization)
		- [Java](#java)
		- [PHP](#php)
	- [Database](#database)
		- [Redis](#redis)
		- [MySQL](#mysql)
		- [Oracle](#oracle)
		- [MSSQL](#mssql)
	- [Information Disclosure](#information-disclosure)
	- [CMS/OA](#cmsoa)
	- [Middleware/Application](#middlewareapplication)
- [Penetration Testing](#penetration-testing)
	- [Nice Tools](#nice-tools)
	- [Extensions](#extensions)
		- [Chrome](#chrome)
		- [Burpsuite](#burpsuite)
		- [Yakit](#yakit)
	- [Auxiliary Tools](#auxiliary-tools)
		- [Open-Source Toolkit](#open-source-toolkit)
		- [DNSLog](#dnslog)
		- [Command Line](#command-line)
		- [Beautifier](#beautifier)
		- [Generator](#generator)
	- [SQL Injection](#sql-injection)
	- [Access Control](#access-control)
		- [Bypass 40X errors](#bypass-40x-errors)
	- [XSS](#xss)
	- [File Inclusion](#file-inclusion)
	- [SSRF](#ssrf)
	- [Mobile Security](#mobile-security)
		- [Mini Program](#mini-program)
		- [APK](#apk)
		- [SessionKey](#sessionkey)
	- [Payload and Bypass](#payload-and-bypass)
- [Red Teaming and Offensive Security](#red-teaming-and-offensive-security)
	- [Infrastructure](#infrastructure)
	- [Reconnaissance](#reconnaissance)
	- [Credential Access](#credential-access)
		- [Credential Dumping](#credential-dumping)
		- [Local Enumeration](#local-enumeration)
		- [NTLM Cracking](#ntlm-cracking)
	- [Post Exploitation](#post-exploitation)
		- [Nice Tools](#nice-tools)
		- [Binaries and Libraries](#binaries-and-libraries)
	- [Persistence](#persistence)
		- [MemShell](#memshell)
		- [Webshell Management](#webshell-management)
		- [Webshell Bypass](#webshell-bypass)
		- [Reverse Shell Management](#reverse-shell-management)
	- [Privilege Escalation](#privilege-escalation)
		- [Linux Local Enumeration](#linux-local-enumeration)
		- [Windows Local Enumeration](#windows-local-enumeration)
		- [Windows Exploits](#windows-exploits)
		- [Linux Exploits](#linux-exploits)
		- [Database Exploits](#database-exploits)
	- [Defense Evasion](#defense-evasion)
		- [Linux Defense Evasion](#linux-defense-evasion)
		- [Windows Defense Evasion](#windows-defense-evasion)
	- [Proxy](#proxy)
		- [Proxy Client](#proxy-client)
		- [Proxy Tools](#proxy-tools)
		- [DNS Tunnel](#dns-tunnel)
		- [ICMP Tunnel](#icmp-tunnel)
		- [Port Forwarding](#port-forwarding)
	- [Operation Security](#operation-security)
- [Active Directory Penetration](#active-directory-penetration)
	- [Collection and Discovery](#collection-and-discovery)
	- [Privilege Escalation](#privilege-escalation)
	- [Known Exploited Vulnerabilities](#known-exploited-vulnerabilities)
		- [MS14-068](#ms14-068)
		- [noPac](#nopac)
		- [Zerologon](#zerologon)
		- [ProxyLogon/ProxyShell](#proxylogonproxyshell)
		- [ProxyNotShell](#proxynotshell)
		- [Printnightmare](#printnightmare)
	- [Methodology](#methodology)
		- [Coerce and Relay](#coerce-and-relay)
		- [Delegation](#delegation)
		- [ADCS](#adcs)
		- [ACLs and ACEs](#acls-and-aces)
- [Blue Teaming and Defensive Security](#blue-teaming-and-defensive-security)
	- [Memshell Detection](#memshell-detection)
	- [Webshell Detection](#webshell-detection)
	- [Blue Teaming](#blue-teaming)
	- [Enforcement](#enforcement)
	- [Incident Response](#incident-response)
	- [Ransomware](#ransomware)
		- [Search Engine](#search-engine)
		- [Decryption Tools](#decryption-tools)
	- [Open-Source Honeypot](#open-source-honeypot)
	- [Reverse Engineering](#reverse-engineering)
		- [Nice Tools](#nice-tools)
		- [Static Analysis](#static-analysis)
		- [Dynamic Analysis](#dynamic-analysis)
		- [Java](#java)
		- [Mobile](#mobile)
		- [Python](#python)
		- [Rust/Go/.NET](#rustgonet)
- [Cloud Security](#cloud-security)
	- [Resources](#resources)
	- [Cloud Threat Matrix](#cloud-threat-matrix)
	- [Cloud Services](#cloud-services)
		- [Management Tools](#management-tools)
		- [AK/SK Exploit](#aksk-exploit)
	- [Cloud Native](#cloud-native)
		- [Nice Tools](#nice-tools)
		- [Docker](#docker)
		- [Kubernetes](#kubernetes)
- [AI Security](#ai-security)
	- [Resources](#resources)
	- [Model Rankings & Evaluation Platforms](#model-rankings--evaluation-platforms)
	- [AI Agent Security & Guardrails](#ai-agent-security--guardrails)
	- [AI-Powered Red Teaming & Offensive Automation](#ai-powered-red-teaming--offensive-automation)
	- [Agent Skills](#agent-skills)
- [Productivity-Boosting Auxiliary Tools](#productivity-boosting-auxiliary-tools)
	- [LLM](#llm)
		- [Open-Source Resources](#open-source-resources)
		- [Orchestration Framework](#orchestration-framework)
		- [Prompts](#prompts)
		- [Deployment](#deployment)
- [Productivity-Boosting Usage Methods](#productivity-boosting-usage-methods)
	- [How to Use Alias Quickly](#how-to-use-alias-quickly)
	- [How to Optimize the Native Terminal](#how-to-optimize-the-native-terminal)

## Open-Source Navigation

### Cryptography

#### Online Tools

- http://www.ip33.com/
- http://www.metools.info/
- https://www.107000.com/
- http://www.hiencode.com/
- http://www.atoolbox.net/
- https://www.sojson.com/
- https://the-x.cn/

#### Offline Tools

- https://github.com/wangyiwy/oktools
- https://github.com/Ciphey/Ciphey
- https://github.com/gchq/CyberChef 👍
- http://1o1o.xyz/bo_ctfcode.html
- https://github.com/guyoung/CaptfEncoder

#### Encode/Decode

- http://code.mcdvisa.com/ Chinese Commercial Code
- https://www.compart.com/en/unicode/ Unicode
- http://web.chacuo.net/charsetuuencode UUencode
- https://tool.chinaz.com/tools/escape.aspx Escape/Unescape
- https://zh.rakko.tools/tools/21/ HTML Entity Encode

#### Regular Expressions

- https://regex101.com/
- https://github.com/VincentSit/ChinaMobilePhoneNumberRegex
- https://github.com/any86/any-rule

#### Hash Algorithms

- https://www.cmd5.org/
- https://www.somd5.com/
- https://www.onlinehashcrack.com/
- https://crackstation.net/
- https://crack.sh/
- https://passwordrecovery.io/
- https://md5decrypt.net/en/Sha256/
- https://hashes.com/en/decrypt/hash

#### RSA

- https://www.ssleye.com/ssltool/
- https://www.lddgo.net/en/encrypt/rsa works with .pem format

#### SM Algorithms

- hutool-crypto: https://github.com/dromara/hutool The hutool-crypto module provides encapsulation for symmetric, asymmetric and digest algorithms
- GmSSL: https://github.com/guanzhi/GmSSL SM2/SM3/SM4/SM9/SSL
- gmssl-python: https://github.com/gongxian-ding/gmssl-python SM2/SM3/SM4/SM9
- SM4: https://www.toolhelper.cn/SymmetricEncryption/SM4

### Cyberspace Search Engine

#### Nice Tools

- Fofa: https://fofa.info/
- Shodan: https://www.shodan.io/
- ZoomEye: https://www.zoomeye.org/
- Hunter: https://hunter.qianxin.com/
- Ditecting: https://www.ditecting.com/
- Quake: https://quake.360.cn/quake/
- Censys: https://search.censys.io/
- Netlas: https://app.netlas.io/domains/

#### Web/Ports

- Wayback Machine: https://web.archive.org/ web pages saved over time
- VisualPing: https://visualping.io/ website changes monitor
- Dark Web Exposure: https://www.immuniweb.com/darkweb/
- SG TCP/IP: https://www.speedguide.net/ports.php ports database

#### Google Hacking

- https://www.exploit-db.com/google-hacking-database Google Hacking Database
- https://github.com/cipher387/Dorks-collections-list Google Hacking Database
- https://cxsecurity.com/dorks/ Google Hacking Database
- https://dorks.faisalahmed.me/ Google Hacking Online
- https://pentest-tools.com/information-gathering/google-hacking Google Hacking Online
- http://advangle.com/ Google Hacking Online
- https://0iq.me/gip/ Google Hacking Online
- https://github.com/obheda12/GitDorker Google Hacking CLI
- https://github.com/six2dez/dorks_hunter Google Hacking CLI
- https://github.com/Pa55w0rd/google-hacking-assistant Chrome Extension

#### GitHub Dork

- https://github.com/search/advanced GitHub Dork
- https://github.com/obheda12/GitDorker GitHub Dork
- https://github.com/damit5/gitdorks_go GitHub Dork

### Open-Source Intelligence

#### Nice Tools

- OSINT Resource List: https://start.me/p/rx6Qj8/nixintel-s-osint-resource-list
- OSINT Framework: https://osintframework.com/
- OSINT Handbook: https://i-intelligence.eu/uploads/public-documents/OSINT_Handbook_2020.pdf

#### Threat Intelligence

- Virustotal: https://www.virustotal.com/
- Tencent Hubble Analysis System: https://habo.qq.com/tool/index
- ThreatBook Threat Intelligence: https://x.threatbook.com/
- QiAnXin Threat Intelligence: https://ti.qianxin.com/
- 360 Threat Intelligence: https://ti.360.net/
- Cybersecurity Threat Information Sharing Platform: https://share.anva.org.cn/web/publicity/listPhishing
- DBAppSecurity Threat Intelligence: https://ti.dbappsecurity.com.cn/
- Huoxian Security Platform: https://www.huoxian.cn
- KnownSec Hacker News Stream: https://hackernews.cc/
- SecWiki Security Information Stream: https://www.sec-wiki.com/

#### Disclosed Vulnerabilities

- 360 Cybersecurity Response Center: https://cert.360.cn/
- KnownSec Vulnerability Database: https://www.seebug.org/
- Chaitin Stack Vulnerability Database: https://stack.chaitin.com/vuldb/
- Alibaba Cloud Vulnerability Database: https://avd.aliyun.com/high-risk/list
- PeiQi Vulnerability Database: https://peiqi.wgpsec.org/
- Hackerone: https://www.hackerone.com/
- CVE: https://cve.mitre.org/
- National Vulnerability Database: https://nvd.nist.gov/
- Vulnerability & Exploit Database: https://www.rapid7.com/db/
- Packet Storm's file archive: https://packetstormsecurity.com/files/tags/exploit
- Shodan: https://cvedb.shodan.io/cves stay updated with CVEs `curl https://cvedb.shodan.io/cves | jq '[.cves[] | select(.cvss > 8)]'`
- CVEShield: https://www.cveshield.com/ latest trending vulnerabilities

#### API Search

- https://www.postman.com/explore/ public API
- https://rapidapi.com/ public API
- https://serene-agnesi-57a014.netlify.app/ discover secret API keys

#### Source Code Search

- https://publicwww.com/
- https://searchcode.com/

### Open-Source Resources

#### Communities/Knowledge Base

- Aliyun xz: https://xz.aliyun.com/
- Infocon: https://infocon.org/
- ffffffff0x Security Knowledge Framework: https://github.com/ffffffff0x/1earn
- Wolf Group Public Knowledge Base: https://wiki.wgpsec.org/
- Mitre ATT&CK matrices: https://attack.mitre.org/matrices/enterprise
- Mitre ATT&CK techniques: http://attack.mitre.org/techniques/enterprise/
- Hacking Articles: https://www.hackingarticles.in/
- PostSwigger Blog: https://portswigger.net/blog
- InGuardians Labs Blog: https://www.inguardians.com/
- Pentest Workflow: https://pentest.mxhx.org/
- Pentest Cheatsheet: https://pentestbook.six2dez.com/

#### Mindmap/Cheat Sheets

- https://cheatsheets.zip/ Cheat Sheets for Developers
- https://learnxinyminutes.com/ Programming/Toolkit/Command/OS/Shortcuts cheat sheet
- https://github.com/Ignitetechnologies/Mindmap/ Cyber Security Mindmap
- https://html5sec.org/ HTML5 Security Cheatsheet
- https://orange-cyberdefense.github.io/ocd-mindmaps/img/mindmap_ad_dark_classic_2025.03.excalidraw.svg AD attack&defense mindmaps
- https://github.com/WADComs/WADComs.github.io Windows/AD cheat sheet 👍

#### Red Teaming and Offensive Security

- https://www.ired.team/
- https://www.thehacker.recipes/
- https://ppn.snovvcrash.rocks/
- https://book.hacktricks.xyz/
- https://blog.harmj0y.net/
- https://hausec.com/domain-penetration-testing/
- https://dirkjanm.io/
- https://casvancooten.com/
- https://evasions.checkpoint.com/
- https://redteam.guide/docs/definitions
- https://github.com/HadessCS/Red-team-Interview-Questions

#### Blue Teaming and Defensive Security

- https://github.com/Purp1eW0lf/Blue-Team-Notes

#### Operation Security

- https://github.com/WesleyWong420/OPSEC-Tradecraft

#### Learning and Practice Platforms

- Cybrary: https://www.cybrary.it/
- HacktheBox: https://www.hackthebox.com/
- TryHackMe: https://tryhackme.com/
- Try2Hack: https://try2hack.me/
- Vulnmachines: https://www.vulnmachines.com/
- RangeForce: https://www.rangeforce.com/
- Root Me: https://www.root-me.org/
- ichunqiu: https://yunjing.ichunqiu.com/
- echoCTF: https://github.com/echoCTF/echoCTF.RED for CTF
- Vulnhub: https://www.vulnhub.com/

For Mac M1 to use ova format images like Vulnhub, you need to convert ova to qcow2 and run via UTM:

- https://github.com/qemu/qemu
- https://github.com/utmapp/UTM

## Reconnaissance

### Nice Tools

- AlliN: https://github.com/P1-Team/AlliN
- fscan: https://github.com/shadow1ng/fscan
- qscan: https://github.com/qi4L/qscan
- TscanPlus: https://github.com/TideSec/TscanPlus
- dddd: https://github.com/SleepingBag945/dddd
- kscan: https://github.com/lcvvvv/kscan
- Kunyu: https://github.com/knownsec/Kunyu
- OneForAll: https://github.com/shmilylty/OneForAll
- ShuiZe: https://github.com/0x727/ShuiZe_0x727
- FofaX: https://github.com/xiecat/fofax
- Fofa Viewer: https://github.com/wgpsec/fofa_viewer
- ENScan_GO: https://github.com/wgpsec/ENScan_GO
- Amass: https://github.com/owasp-amass/amass
- ApolloScanner: https://github.com/b0bac/ApolloScanner

### IP/Domain/Subdomain

- IP:
    - https://www.ipuu.net/
    - https://site.ip138.com/
    - https://myip.ms/
    - https://ipwhois.cnnic.net.cn
- Multi Ping:
    - https://ping.chinaz.com/
    - https://www.host-tracker.com/
    - https://www.webpagetest.org/
    - https://dnscheck.pingdom.com/
- IP to Domain:
    - https://site.ip138.com/
    - https://x.threatbook.cn/
    - https://www.virustotal.com/
- Whois:
    - https://whois.chinaz.com/
    - https://whois.aliyun.com/
    - https://who.is/
    - https://www.whoxy.com/
- DNS:
    - https://hackertarget.com/find-dns-host-records
    - https://dnsdumpster.com
    - https://dnsdb.io/zh-cn
    - https://centralops.net/co/
    - https://viewdns.info/
    - https://dnsdumpster.com/
    - https://rapiddns.io/
- ASN:
    - https://wq.apnic.net/
    - https://bgp.he.net/
    - https://bgpview.io/
- TLS/SSL Certificate:
    - https://censys.io
    - https://crt.sh

### Fingerprint

#### Fingerprint Collection

- https://github.com/r0eXpeR/fingerprint
- https://github.com/0x727/FingerprintHub

#### Fingerprint Reconnaissance

- https://github.com/EASY233/Finger
- https://github.com/EdgeSecurityTeam/EHole
- https://github.com/lemonlove7/EHole_magic
- https://github.com/0x727/ObserverWard
- https://github.com/TideSec/TideFinger_Go
- https://github.com/zhzyker/dismap
- https://www.webshell.cc/4697.html
- http://www.yunsee.cn/ online

#### Waf Checks

- https://github.com/stamparm/identYwaf
- https://github.com/EnableSecurity/wafw00f
- https://github.com/MISP/misp-warninglists

### Brute Force

#### Brute Force Tools

- Port:
    - https://github.com/antirez/hping
- Subdomain:
    - https://github.com/projectdiscovery/subfinder
    - https://github.com/knownsec/ksubdomain
- Web:
    - https://github.com/pingc0y/URLFinder
    - https://github.com/s0md3v/Arjun
    - https://github.com/OJ/gobuster
    - https://github.com/jaeles-project/gospider
    - https://github.com/xmendez/wfuzz
- Directory:
    - https://github.com/maurosoria/dirsearch
    - https://github.com/H4ckForJob/dirmap
    - https://github.com/ffuf/ffuf
- Password:
    - https://github.com/vanhauser-thc/thc-hydra
    - https://github.com/galkan/crowbar supports sshkey and openvpn
    - https://github.com/evilsocket/legba/
- Hash Cracking:
    - https://github.com/openwall/john
    - https://github.com/hashcat/hashcat
    - https://hashcat.net/wiki/doku.php?id=example_hashes hashcat examples
    - https://github.com/HashPals/Name-That-Hash hash identifier
    - https://github.com/noraj/haiti hash identifier
- Json web token (JWT):
    - https://jwt.io/
    - https://github.com/Sjord/jwtcrack
    - https://github.com/ticarpi/jwt_tool
    - https://github.com/mazen160/jwt-pwn
    - https://github.com/brendan-rius/c-jwt-cracker
    - https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list
    - https://github.com/hahwul/jwt-hack

#### Brute Force Dictionaries

- Wordlists for All:
    - https://github.com/danielmiessler/SecLists 46.4k star
    - https://github.com/SexyBeast233/SecDictionary + ffuf
    - https://github.com/insightglacier/Dictionary-Of-Pentesting
    - https://github.com/TheKingOfDuck/fuzzDicts
    - https://github.com/gh0stkey/Web-Fuzzing-Box
    - https://github.com/a3vilc0de/PentesterSpecialDict
    - https://github.com/Bo0oM/fuzz.txt
    - https://github.com/assetnote/wordlists
    - https://github.com/rapid7/metasploit-framework/tree/master/data/wordlists
- Web Fuzz Wordlists:
    - https://github.com/xmendez/wfuzz/tree/master/wordlist
    - https://github.com/lutfumertceylan/top25-parameter
- Others (not frequently used):
    - https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content
    - https://github.com/assetnote/commonspeak2-wordlists/tree/master/wordswithext
    - https://github.com/random-robbie/bruteforce-lists
    - https://github.com/google/fuzzing/tree/master/dictionaries
    - https://github.com/six2dez/OneListForAll

#### Generate a Custom Dictionary

- Online:
    - Generate wordlists: https://weakpass.com/generate
    - Generate subdomains and wordlists: https://weakpass.com/generate/domains
    - Chinese to Pinyin: https://www.aies.cn/pinyin.htm
    - Password Cracking: https://www.hacked.com.cn/pass.html
- Private Deployment:
    - Generate wordlists(offline): https://github.com/zzzteph/weakpass
    - Generate subdomains and wordlists(offline): https://github.com/zzzteph/probable_subdomains
- Offline:
    - pydictor: https://github.com/LandGrey/pydictor/
    - crunch:
        - Kali/Linux: https://sourceforge.net/projects/crunch-wordlist
        - Windows: https://github.com/shadwork/Windows-Crunch

#### Default Credentials

- Default Credentials Cheat Sheet: https://github.com/ihebski/DefaultCreds-cheat-sheet 3468 default creds
- datarecovery: https://datarecovery.com/rd/default-passwords/ online
- cirt.net: https://cirt.net/passwords online
- Online Router Passwords:
  - https://www.routerpasswords.com/
  - https://portforward.com/router-password/
  - https://www.cleancss.com/router-default/
  - https://www.toolmao.com/baiduapp/routerpwd/
  - https://datarecovery.com/rd/default-passwords/

### Social Engineering

#### Leaked Credentials

- https://have-ibeenpwned.com/
- https://breachdirectory.org/

#### Email

- Temporary Email:
    - http://24mail.chacuo.net/
    - https://www.guerrillamail.com/
    - https://rootsh.com/
- Snov.io: https://app.snov.io
- Phonebook: also works on subdomains and urls https://phonebook.cz
- Skymem: https://www.skymem.info
- Hunter: https://hunter.io
- email-format: https://www.email-format.com/i/search/
- Search Email: https://souyouxiang.com/find-contact/
- theHarvester: also works on subdomains https://github.com/laramies/theHarvester
- Verify emails: https://tools.emailhippo.com/
- Accounts registered by email: https://emailrep.io/

#### SMS Online

- https://sms-activate.io 👍 more than 180 countries for sale
- https://www.supercloudsms.com/en/
- https://getfreesmsnumber.com/
- https://www.zusms.com/
- https://yunduanxin.net/
- https://www.free-sms-receive.com/
- https://receive-sms.cc/#google_vignette
- https://bestsms.xyz/
- https://smscodeonline.com/

#### Phishing

- gophish: https://github.com/gophish/gophish open-source phishing toolkit
- SpoofWeb: https://github.com/5icorgi/SpoofWeb deploy phishing website

### Mobile

- https://www.xiaolanben.com/
- https://www.qimai.cn/

## Vulnerability Research

### Vulnerable Environments

#### Basic Vulnerabilities

- Sqli-labs: https://github.com/Audi-1/sqli-labs
- Upload-labs: https://github.com/c0ny1/upload-labs
- Xss-labs: https://github.com/do0dl3/xss-labs
- DVWA: https://github.com/digininja/DVWA
- WebGoat: https://github.com/WebGoat/WebGoat
- encrypt-labs: https://github.com/SwagXz/encrypt-labs AES/DES/RSA

#### Comprehensive Vulnerabilities

- Vulhub: https://vulhub.org/
- PortSwigger Web Security Academy: https://portswigger.net/web-security
- OWASP Top10: https://owasp.org/www-project-juice-shop/
- Vulstudy: https://github.com/c0ny1/vulstudy 17 platform based on docker
- Vulfocus: https://github.com/fofapro/vulfocus
- FastJsonParty: https://github.com/lemono0/FastJsonParty

#### Vulnerable IoT Environment

- IoT-vulhub: https://github.com/firmianay/IoT-vulhub

#### Vulnerable Active Directory Environment

- Game of active directory: https://github.com/Orange-Cyberdefense/GOAD
- BadBlood: https://github.com/davidprowe/BadBlood create your own example Active Directory environment

#### Vulnerable Cloud Environments

- Awesome-CloudSec-Labs: https://github.com/iknowjason/Awesome-CloudSec-Labs
- K8s Lan Party: https://www.k8slanparty.com/
- badPods: https://github.com/BishopFox/badPods
- Metarget: https://github.com/Metarget/metarget
- TerraformGoat: https://github.com/HXSecurity/TerraformGoat
- Kubernetes Goat: https://github.com/madhuakula/kubernetes-goat
- Attack Defense: https://attackdefense.pentesteracademy.com/listing?labtype=cloud-services&subtype=cloud-services-amazon-s3
- AWSGoat: https://github.com/ine-labs/AWSGoat
- CloudGoat: https://github.com/RhinoSecurityLabs/cloudgoat

#### Vulnerable AI Environments

- AI prompt injection challenge: https://gandalf.lakera.ai/baseline

### Proof of Concept

> Be careful Malware, the latest CVEs in POC repositories may have poisoning risks.

#### PoC/ExP

- https://github.com/wy876/POC
- https://github.com/lal0ne/vulnerability
- https://github.com/DawnFlame/POChouse
- https://github.com/coffeehb/Some-PoC-oR-ExP
- https://github.com/luck-ying/Library-POC
- https://github.com/Mr-xn/Penetration_Testing_POC
- https://github.com/nomi-sec/PoC-in-GitHub
- https://github.com/ycdxsb/PocOrExp_in_Github
- https://github.com/helloexp/0day
- https://github.com/trickest/cve
- https://sploitus.com/ exploits of the week
- https://www.exploit-db.com/ works with `searchsploit <keywords>`

#### PoC Templates

- https://poc.xray.cool/ online
- https://github.com/zeoxisca/gamma-gui offline
- https://github.com/projectdiscovery/nuclei-templates/

## Vulnerability Exploits

### Nice Tools

- https://github.com/chaitin/xpoc
- https://github.com/chaitin/xray
- https://github.com/zhzyker/vulmap
- https://github.com/zan8in/afrog
- https://github.com/projectdiscovery/nuclei

### Code Audit

- tabby: https://github.com/wh1t3p1g/tabby

### Serialization

#### Java

- https://github.com/phith0n/zkar

### Deserialization

#### Java

- https://github.com/frohoff/ysoserial
- https://github.com/Y4er/ysoserial
- https://github.com/wh1t3p1g/ysomap
- https://github.com/mbechler/marshalsec
- https://github.com/qi4L/JYso
- https://github.com/vulhub/JNDIExploit
- https://github.com/welk1n/JNDI-Injection-Exploit
- https://github.com/WhiteHSBG/JNDIExploit
- https://github.com/rebeyond/JNDInjector
- https://github.com/A-D-Team/attackRmi
- https://github.com/Java-Chains/web-chains
- https://github.com/DeEpinGh0st/ysoserial

#### PHP

- https://github.com/ambionics/phpggc PHP unserialize() payloads

### Database

#### Redis

- https://github.com/cinience/RedisStudio
- https://github.com/qishibo/AnotherRedisDesktopManager
- https://github.com/n0b0dyCN/redis-rogue-server
- https://github.com/Ridter/redis-rce
- https://github.com/yuyan-sec/RedisEXP
- https://github.com/r35tart/RedisWriteFile

#### MySQL

- https://github.com/SafeGroceryStore/MDUT multiple database utilization tools
- https://github.com/4ra1n/mysql-fake-server
- https://github.com/dushixiang/evil-mysql-server
- https://github.com/fnmsd/MySQL_Fake_Server

#### Oracle

- odat: https://github.com/quentinhardy/odat RCE
- sqlplus: https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html xxx as sysdba

#### MSSQL

- https://github.com/uknowsec/SharpSQLTools
- https://github.com/Ridter/PySQLTools

### Information Disclosure

- trufflehog: https://github.com/trufflesecurity/trufflehog find, verify, and analyze leaked credentials
- git-dumper: https://github.com/arthaud/git-dumper
- gitleaks: https://github.com/gitleaks/gitleaks
- dvcs-ripper: https://github.com/kost/dvcs-ripper .svn、.hg、.cvs disclosure
- ds_store_exp: https://github.com/lijiejie/ds_store_exp .DS_Store disclosure
- Hawkeye: https://github.com/0xbug/Hawkeye gitHub sensitive information leakage monitor Spider

### CMS/OA

- TongdaScan_go https://github.com/Fu5r0dah/TongdaScan_go
- Apt_t00ls: https://github.com/White-hua/Apt_t00ls
- OA-EXPTOOL: https://github.com/LittleBear4/OA-EXPTOOL
- DecryptTools: https://github.com/wafinfo/DecryptTools 22 types of encryption and decryption
- ncDecode: https://github.com/1amfine2333/ncDecode UFIDA NC decryption
- PassDecode-jar: https://github.com/Rvn0xsy/PassDecode-jar FineReport/Zhiyuan decryption
- ezOFFICE_Decrypt: https://github.com/wafinfo/ezOFFICE_Decrypt Wanhou decryption
- LandrayDES: https://github.com/zhutougg/LandrayDES Landray OA decryption

### Middleware/Application

**Confluence**

- ConfluenceMemshell: https://github.com/Lotus6/ConfluenceMemshell
- CVE-2022-26134 Memshell: https://github.com/BeichenDream/CVE-2022-26134-Godzilla-MEMSHELL
- CVE-2023-22527 Memshell: https://github.com/Boogipop/CVE-2023-22527-Godzilla-MEMSHELL

**Druid**

- DruidCrack: https://github.com/rabbitmask/DruidCrack
- druid_sessions: https://github.com/yuyan-sec/druid_sessions

**Fastjson**

- fastjson-exp: https://github.com/amaz1ngday/fastjson-exp

**GitLab**

- CVE-2021-22205: https://github.com/Al1ex/CVE-2021-22205/

**Nacos**

- NacosRce: https://github.com/c0olw/NacosRce/
- nacosleak: https://github.com/a1phaboy/nacosleak
- nacosScan:https://github.com/Whoopsunix/nacosScan
- NacosExploitGUI: https://github.com/charonlight/NacosExploitGUI

**Nps**

- nps-auth-bypass: https://github.com/carr0t2/nps-auth-bypass

**Java**

- jdwp-shellifier: python2 https://github.com/IOActive/jdwp-shellifier
- jdwp-shellifier: https://github.com/Lz1y/jdwp-shellifier
- jascypt encryption & decryption: https://www.devglan.com/online-tools/jasypt-online-encryption-decryption Jasypt encryption & decryption tool

**Shiro**

- Shiro rememberMe Decrypt: https://vulsee.com/tools/shiroDe/shiroDecrypt.html
- shiro_attack: https://github.com/j1anFen/shiro_attack
- shiro_rce_tool: https://github.com/wyzxxz/shiro_rce_tool
- ShiroExploit: https://github.com/feihong-cs/ShiroExploit-Deprecated
- ShiroExp: https://github.com/safe6Sec/ShiroExp
- shiro_key: https://github.com/yanm1e/shiro_key 1k+

**Struts**

- Struts2VulsTools: https://github.com/shack2/Struts2VulsTools

**Spring Boot**

- SpringBoot-Scan: https://github.com/AabyssZG/SpringBoot-Scan
- SpringBootVulExploit: https://github.com/LandGrey/SpringBootVulExploit
- CVE-2022-22963 https://github.com/mamba-2021/EXP-POC/tree/main/Spring-cloud-function-SpEL-RCE
- CVE-2022-22947/CVE-2022-22963: https://github.com/savior-only/Spring_All_Reachable
- swagger-exp: https://github.com/lijiejie/swagger-exp
- jasypt decrypt: https://www.devglan.com/online-tools/jasypt-online-encryption-decryption Jasypt decryption tool
- heapdump_tool: https://github.com/wyzxxz/heapdump_tool
- Memory Analyzer: https://eclipse.dev/mat/download/
- JDumpSpider:https://github.com/whwlsfb/JDumpSpider

**Tomcat**

- CVE-2020-1938: https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi
- ClassHound: https://github.com/LandGrey/ClassHound

**Thinkphp**

- ThinkphpGUI: https://github.com/Lotus6/ThinkphpGUI
- thinkphp_gui_tools: https://github.com/bewhale/thinkphp_gui_tools

**Weblogic**

- WeblogicTool: https://github.com/KimJun1010/WeblogicTool
- WeblogicScan: https://github.com/dr0op/WeblogicScan
- WeblogicScan: https://github.com/rabbitmask/WeblogicScan
- weblogicScanner: https://github.com/0xn0ne/weblogicScanner
- weblogic-framework: https://github.com/sv3nbeast/weblogic-framework
- CVE-2020-14882: https://github.com/zhzyker/exphub/blob/master/weblogic/cve-2020-14882_rce.py

**WebSocket**

- wscat: https://github.com/websockets/wscat

**vCenter**

- VcenterKiller: https://github.com/Schira4396/VcenterKiller
- VcenterKit:https://github.com/W01fh4cker/VcenterKit
- vcenter_saml_login: https://github.com/horizon3ai/vcenter_saml_login extract the Identity Provider (IdP) cert

**Zookeeper**

- ZooInspector: https://issues.apache.org/jira/secure/attachment/12436620/ZooInspector.zip
- apache-zookeeper: https://archive.apache.org/dist/zookeeper/zookeeper-3.5.6/ zkCli.sh command line tool

## Penetration Testing

### Nice Tools

- Yakit: https://github.com/yaklang/yakit
- Burpsuite: https://portswigger.net/burp

### Extensions

#### Chrome

- ZeroOmega: https://github.com/zero-peak/ZeroOmega proxy switchyOmega for manifest v3
- serp-analyzer: https://leadscloud.github.io/serp-analyzer/ show domain/IP
- FindSomething: https://github.com/ResidualLaugh/FindSomething find something in source code or javascript
- Hack Bar:https://github.com/0140454/hackbar
- Wappalyzer: https://www.wappalyzer.com/ identify technologies on websites
- EditThisCookie:https://www.editthiscookie.com/
- Cookie-Editor:https://github.com/Moustachauve/cookie-editor
- Disable JavaScript: https://github.com/dpacassi/disable-javascript
- Heimdallr: https://github.com/Ghr07h/Heimdallr for honeypot
- anti-honeypot:https://github.com/cnrstar/anti-honeypot for honeypot
- immersive-translate: https://github.com/immersive-translate/immersive-translate/ translator
- relingo: https://cn.relingo.net/en/ translator
- json-formatter: https://github.com/callumlocke/json-formatter
- markdown-viewer: https://github.com/simov/markdown-viewer

#### Burpsuite

- HaE: https://github.com/gh0stkey/HaE highlighter and extractor
- Log4j2Scan: https://github.com/whwlsfb/Log4j2Scan for Log4j
- RouteVulScan: https://github.com/F6JO/RouteVulScan route vulnerable scanning
- BurpCrypto: https://github.com/whwlsfb/BurpCrypto support AES/RSA/DES/ExecJs
- domain hunter: https://github.com/bit4woo/domain_hunter_pro domain hunter
- BurpAppletPentester: https://github.com/mrknow001/BurpAppletPentester sessionkey decryptor

#### Yakit

- HaeToYakit: https://github.com/youmulijiang/HaeToYakit

### Auxiliary Tools

#### Open-Source Toolkit

- https://forum.ywhack.com/bountytips.php?tools
- https://github.com/knownsec/404StarLink
- https://pentest-tools.com/

#### DNSLog

- dig.pm: https://dig.pm/
- ceye.io: http://ceye.io/
- dnslog.cn: http://dnslog.cn/
- Alphalog: dns/http/rmi/ldap https://github.com/AlphabugX/Alphalog
- DNS rebinding: https://lock.cmpxchg8b.com/rebinder.html
- DNSLog-GO: https://github.com/lanyi1998/DNSlog-GO

#### Command Line

- https://github.com/ohmyzsh/ohmyzsh command line enhancement for zsh
- https://github.com/chrisant996/clink command line enhancement for cmd.exe
- https://github.com/hanslub42/rlwrap a readline wrapper
- https://github.com/Eugeny/tabby for Windows
- https://github.com/warpdotdev/Warp for Mac
- https://github.com/zellij-org/zellij terminal multiplexers
- https://github.com/tmux terminal multiplexers
- https://github.com/tomnomnom/anew tool for adding new lines to files, skipping duplicates
- https://github.com/jlevy/the-art-of-command-line
- Linux command line:
    - https://github.com/jaywcjlove/linux-command online
    - https://github.com/chenjiandongx/pls go ver.
    - https://github.com/chenjiandongx/how python ver.
- https://explainshell.com/ explain shell command
- https://github.com/BurntSushi/ripgrep a line-oriented search tool(faster)

#### Beautifier

- http://web.chacuo.net/formatsh
- https://beautifier.io/
- http://jsnice.org/

#### Generator

- revshells: https://www.revshells.com/
- reverse-shell: https://forum.ywhack.com/reverse-shell/
- reverse-shell-generator: https://tex2e.github.io/reverse-shell-generator/index.html
- reverse-shell-generator: https://github.com/0dayCTF/reverse-shell-generator
- File-Download-Generator: https://github.com/r0eXpeR/File-Download-Generator

### SQL Injection

- https://github.com/sqlmapproject/sqlmap
- https://github.com/payloadbox/sql-injection-payload-list

### Access Control

#### Bypass 40X errors

- https://github.com/yunemse48/403bypasser
- https://github.com/lobuhi/byp4xx
- https://github.com/Dheerajmadhukar/4-ZERO-3
- https://github.com/devploit/nomore403

### XSS

- XSS Chop: https://xsschop.chaitin.cn/demo/
- XSS/CSRF: https://evilcos.me/lab/xssor/

### File Inclusion

- https://github.com/hansmach1ne/lfimap
- https://github.com/mzfr/liffy

### SSRF

- https://portswigger.net/web-security/ssrf/url-validation-bypass-cheat-sheet
- https://github.com/tarunkant/Gopherus Gopherus for py2
- https://github.com/Esonhugh/Gopherus3 Gopherus for py3

### Mobile Security

#### Mini Program

- ~~[wxappUnpacker: https://github.com/xuedingmiaojun/wxappUnpacker]~~
- https://github.com/Cherrison/CrackMinApp
- https://github.com/mrknow001/API-Explorer ak/sk for X platform
- https://github.com/eeeeeeeeee-code/e0e1-wx
- https://github.com/wux1an/wxapkg

#### APK

- https://github.com/kelvinBen/AppInfoScanner
- https://github.com/iBotPeaches/Apktool

#### SessionKey

- https://github.com/mrknow001/wx_sessionkey_decrypt

### Payload and Bypass

- PayloadsAllTheThings: https://github.com/swisskyrepo/PayloadsAllTheThings
- IP to Decimal: https://www.browserling.com/tools/ip-to-dec 127.0.0.1 >>> 2130706433
- java.lang.Runtime.exec() Payload: https://payloads.net/Runtime.exec/
- PHPFuck: https://github.com/splitline/PHPFuck
- JSFuck: http://www.jsfuck.com/
- JavaScript Deobfuscator and Unpacker: https://lelinhtinh.github.io/de4js/ JavaScript Deobfuscator and Unpacker
- CVE-2021-44228-PoC-log4j-bypass-words: https://github.com/Puliczek/CVE-2021-44228-PoC-log4j-bypass-words

## Red Teaming and Offensive Security

### Infrastructure

- f8x: https://github.com/ffffffff0x/f8x red/blue team environment automation deployment tool
- openvpn-install: https://github.com/hwdsl2/openvpn-install OpenVPN server installer for x
- cloudreve: https://github.com/cloudreve/Cloudreve self-hosted file management system with multi-cloud support
- updog: https://github.com/sc0tfree/updog uploading and downloading via HTTP/S
- mattermost: https://github.com/mattermost/mattermost
- rocketchat: https://github.com/RocketChat/Rocket.Chat
- codimd: https://github.com/hackmdio/codimd
- hedgedoc: https://github.com/hedgedoc/hedgedoc

### Reconnaissance

- SharpHunter: https://github.com/lintstar/SharpHunter Automated Hosting Information Hunting Tool
- netspy: https://github.com/shmilylty/netspy intranet segment spy
- SharpHostInfo: https://github.com/shmilylty/SharpHostInfo
- SharpScan: https://github.com/INotGreen/SharpScan
- smbmap: https://github.com/ShawnDEvans/smbmap SMB enumeration

### Credential Access

#### Credential Dumping

- LaZagne: https://github.com/AlessandroZ/LaZagne
- WirelessKeyView: https://www.nirsoft.net/utils/wireless_key.html
- Windows credential manager: https://www.nirsoft.net/utils/credentials_file_view.html
- Pillager: https://github.com/qwqdanchun/Pillager/
- searchall: https://github.com/Naturehi666/searchall
- pypykatz: https://github.com/skelsec/pypykatz mimikatz implementation in pure python
- regsecrets & dpapidump: https://github.com/fortra/impacket/pull/1898 tested on windows 11 and server 2022 without issue
- DonPAPI: https://github.com/login-securite/DonPAPI
- SharpDPAPI: https://github.com/GhostPack/SharpDPAPI
- dploot: https://github.com/zblurx/dploot DPAPI
- PPLdump: https://github.com/itm4n/PPLdump LSASS as protected process
- lsassy: https://github.com/login-securite/lsassy

#### Local Enumeration

- HackBrowserData: https://github.com/moonD4rk/HackBrowserData
- BrowserGhost: https://github.com/QAX-A-Team/BrowserGhost
- chrome: http://www.nirsoft.net/utils/chromepass.html
- firefox: https://github.com/unode/firefox_decrypt
- foxmail: https://securityxploded.com/foxmail-password-decryptor.php
- mobaxterm: https://github.com/HyperSine/how-does-MobaXterm-encrypt-password
- navicat: https://github.com/Zhuoyuan1/navicat_password_decrypt
- navicat: https://github.com/HyperSine/how-does-navicat-encrypt-password
- sunflower: https://github.com/wafinfo/Sunflower_get_Password
- FindToDeskPass: https://github.com/yangliukk/FindToDeskPass
- sundeskQ: sunflower & todesk https://github.com/milu001/sundeskQ
- securreCRT: https://github.com/depau/shcrt
- xshell:
    - https://github.com/HyperSine/how-does-Xmanager-encrypt-password version<7.0
    - https://github.com/RowTeam/SharpDecryptPwd decrypt locally
    - https://github.com/JDArmy/SharpXDecrypt

#### NTLM Cracking

- NetNTLMv1: https://ntlmv1.com/ online
- LM + NTLM hashes and corresponding plaintext passwords:
    - https://openwall.info/wiki/_media/john/pw-fake-nt.gz 3107
    - https://openwall.info/wiki/_media/john/pw-fake-nt100k.gz 100k

### Post Exploitation

#### Nice Tools

- https://github.com/rapid7/metasploit-framework
- https://github.com/byt3bl33d3r/CrackMapExec 👍
- https://github.com/Pennyw0rth/NetExec
- https://github.com/fortra/impacket 👍
- https://github.com/ghost-ng/slinger An impacket-lite cli tool that combines many useful impacket functions using a single session.
- https://github.com/XiaoliChan/wmiexec-Pro AV Evasion based on wmiexec.py
- https://docs.microsoft.com/en-us/sysinternals/downloads/pstools
- https://github.com/GhostPack/Rubeus
- https://github.com/Kevin-Robertson/Powermad
- https://github.com/PowerShellMafia/PowerSploit
- https://github.com/k8gege/Ladon
- https://github.com/samratashok/nishang for powershell
- Cobaltstrike Extensions:
    - Awesome CobaltStrike: https://github.com/zer0yu/Awesome-CobaltStrike
    - Erebus: https://github.com/DeEpinGh0st/Erebus
    - LSTAR: https://github.com/lintstar/LSTAR
    - ElevateKit: https://github.com/rsmudge/ElevateKit
    - C2ReverseProxy: https://github.com/Daybr4ak/C2ReverseProxy
    - pystinger: https://github.com/FunnyWolf/pystinger

#### Binaries and Libraries

- LOLBAS: https://github.com/LOLBAS-Project/LOLBAS-Project.github.io binaries and scripts for Windows
- GTFOBins: https://github.com/GTFOBins/GTFOBins.github.io binaries for Unix

### Persistence

#### MemShell

- https://github.com/pen4uin/java-memshell-generator 👍
- https://github.com/ReaJason/MemShellParty
- https://github.com/BeichenDream/GodzillaMemoryShellProject
- https://github.com/1ucky7/jmg-for-Godzilla
- https://github.com/X1r0z/Godzilla-Suo5MemShell
- https://github.com/tennc/webshell
- https://github.com/novysodope/RMI_Inj_MemShell
- https://github.com/ce-automne/TomcatMemShell
- https://github.com/veo/wsMemShell

#### Webshell Management

- https://github.com/rebeyond/Behinder
- https://github.com/BeichenDream/Godzilla
- https://github.com/shack2/skyscorpion

#### Webshell Bypass

- https://github.com/AabyssZG/WebShell-Bypass-Guide
- http://bypass.tidesec.com/web/
- https://github.com/cseroad/Webshell_Generate

#### Reverse Shell Management

- https://github.com/WangYihang/Platypus
- https://github.com/calebstewart/pwncat python 3.9+

### Privilege Escalation

#### Linux Local Enumeration

- https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite
- https://github.com/mostaphabahadou/postenum
- https://github.com/rebootuser/LinEnum
- https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
- https://github.com/DominicBreuker/pspy Monitor linux processes without root permission

#### Windows Local Enumeration

- https://github.com/S3cur3Th1sSh1t/WinPwn
- https://github.com/carlospolop/PEASS-ng/blob/master/winPEAS/winPEASbat/winPEAS.bat
- https://github.com/S3cur3Th1sSh1t/PowerSharpPack
- https://github.com/Flangvik/SharpCollection
- https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1
- https://github.com/dafthack/DomainPasswordSpray
- https://github.com/dafthack/MailSniper

#### Windows Exploits

- https://github.com/bitsadmin/wesng
- https://github.com/AonCyberLabs/Windows-Exploit-Suggester
- https://github.com/SecWiki/windows-kernel-exploits
- https://github.com/Al1ex/WindowsElevation
- https://i.hacking8.com/tiquan/ online
- https://github.com/BeichenDream/BadPotato/
- https://github.com/giuliano108/SeBackupPrivilege
- https://github.com/gtworek/PSBits/blob/master/Misc/EnableSeBackupPrivilege.ps1
- https://github.com/itm4n/PrivescCheck
- https://github.com/peass-ng/PEASS-ng/blob/master/winPEAS/winPEASexe/README.md
- https://github.com/Ascotbe/Kernelhub

#### Linux Exploits

- https://github.com/The-Z-Labs/linux-exploit-suggester
- https://github.com/InteliSecureLabs/Linux_Exploit_Suggester
- https://github.com/liamg/traitor

#### Database Exploits

- https://github.com/Hel10-Web/Databasetools

### Defense Evasion

#### Linux Defense Evasion

- libprocesshider: https://github.com/gianlucaborello/libprocesshider hide a process under Linux using the ld preloader
- Linux Kernel Hacking: https://github.com/xcellerator/linux_kernel_hacking
- tasklist /svc && ps -aux: https://tasklist.ffffffff0x.com/

#### Windows Defense Evasion

- yetAnotherObfuscator: https://github.com/0xb11a1/yetAnotherObfuscator
- hoaxshell: https://github.com/t3l3machus/hoaxshell
- bypassAV: https://github.com/pureqh/bypassAV
- GolangBypassAV: https://github.com/safe6Sec/GolangBypassAV
- BypassAntiVirus: https://github.com/TideSec/BypassAntiVirus
- AV_Evasion_Tool: https://github.com/1y0n/AV_Evasion_Tool
- shellcodeloader: https://github.com/knownsec/shellcodeloader
- tasklist/systeminfo: https://www.shentoushi.top/av/av.php
- rpeloader: https://github.com/Teach2Breach/rpeloader use Python on Windows without installation

### Proxy

#### Proxy Client

- Proxifier: https://www.proxifier.com/
- Proxychains: https://github.com/haad/proxychains

#### Proxy Tools

- frp: https://github.com/fatedier/frp
- frpModify: https://github.com/uknowsec/frpModify
- suo5: https://github.com/zema1/suo5
- Stowaway: https://github.com/ph4ntonn/Stowaway
- Neo-reGeorg: https://github.com/L-codes/Neo-reGeorg
- nps: https://github.com/ehang-io/nps
- reGeorg: https://github.com/sensepost/reGeorg
- rakshasa: https://github.com/Mob2003/rakshasa
- Viper: https://github.com/FunnyWolf/Viper
- ligolo-ng: https://github.com/nicocha30/ligolo-ng TUN interface
- gost: https://github.com/ginuerzh/gost

#### DNS Tunnel

- iodine: https://github.com/yarrick/iodine
- dnscat2: https://github.com/iagox86/dnscat2
- DNS-Shell: https://github.com/sensepost/DNS-Shell

#### ICMP Tunnel

- icmpsh: https://github.com/bdamele/icmpsh

#### Port Forwarding

- tcptunnel: https://github.com/vakuum/tcptunnel intranet → dmz → attacker

### Operation Security

- https://privacy.sexy/ enforce privacy & security best-practices on Windows, macOS and Linux.
- https://transfer.sh/ anonymous file transfer
- https://a.f8x.io/ shorten URLs

## Active Directory Penetration

### Collection and Discovery

- BloodHound:
    - https://github.com/SpecterOps/BloodHound
    - https://github.com/dirkjanm/BloodHound.py
    - https://github.com/BloodHoundAD/SharpHound
    - https://github.com/CompassSecurity/BloodHoundQueries
    - https://github.com/SpecterOps/BloodHound-Legacy/blob/master/Collectors/SharpHound.ps1
    - https://github.com/AD-Security/AD_Miner
    - https://github.com/NH-RED-TEAM/RustHound
    - https://github.com/FalconForceTeam/SOAPHound
- https://github.com/lzzbb/Adinfo
- https://github.com/wh0amitz/SharpADWS via Active Directory Web Services (ADWS) protocol
- LDAP:
    - https://github.com/franc-pentest/ldeep
    - https://github.com/dirkjanm/ldapdomaindump
    - https://github.com/yaap7/ldapsearch-ad
- DNS:
    - https://github.com/dirkjanm/adidnsdump
- SCCM:
    - https://github.com/garrettfoster13/sccmhunter
    - https://github.com/Mayyhem/SharpSCCM
- Brute force users:
    - https://github.com/ropnop/kerbrute

### Privilege Escalation

- https://github.com/CravateRouge/bloodyAD

### Known Exploited Vulnerabilities

#### MS14-068

- https://github.com/SpiderLabs/Responder/blob/master/tools/FindSMB2UPTime.py
- https://github.com/SecWiki/windows-kernel-exploits/blob/master/MS14-068/pykek/ms14-068.py
- https://github.com/fortra/impacket/blob/master/examples/goldenPac.py

#### noPac

> CVE-2021-42278/CVE-2021-42287

- https://github.com/Ridter/noPac
- https://github.com/Amulab/advul

#### Zerologon

> CVE-2020-1472

- https://github.com/SecuraBV/CVE-2020-1472/blob/master/zerologon_tester.py
- https://github.com/XiaoliChan/zerologon-Shot
- https://github.com/dirkjanm/CVE-2020-1472
- https://github.com/Potato-py/Potato/tree/03c3551e4770db440b27b0a48fc02b0a38a1cf04/exp/cve/CVE-2020-1472
- https://github.com/risksense/zerologon
- https://github.com/StarfireLab/AutoZerologon

#### ProxyLogon/ProxyShell

> CVE-2021-34473

- https://github.com/dirkjanm/privexchange/
- https://github.com/Jumbo-WJB/PTH_Exchange
- https://github.com/hausec/ProxyLogon
- https://github.com/dmaasland/proxyshell-poc/blob/main/proxyshell_rce.py

#### ProxyNotShell

> CVE-2022-41040/CVE-2022-41082

- https://github.com/testanull/ProxyNotShell-PoC

#### Printnightmare

> CVE-2021-34527/CVE-2021-1675

- https://github.com/cube0x0/CVE-2021-1675
- https://github.com/nemo-wq/PrintNightmare-CVE-2021-34527
- https://github.com/calebstewart/CVE-2021-1675

### Methodology

#### Coerce and Relay

- PetitPotam: https://github.com/topotam/PetitPotam
- PrinterBug: https://github.com/leechristensen/SpoolSample
- DFSCoerce: https://github.com/Wh04m1001/DFSCoerce
- WSPCoerce: https://github.com/slemire/WSPCoerce
- ShadowCoerce: https://github.com/ShutdownRepo/ShadowCoerce
- PrivExchange: https://github.com/dirkjanm/privexchange/
- Coercer: https://github.com/p0dalirius/Coercer
- cannon: https://github.com/Amulab/cannon
- Responder: https://github.com/lgandx/Responder
- Responder-Windows: https://github.com/lgandx/Responder-Windows
- KrbRelayUp: https://github.com/Dec0ne/KrbRelayUp
- ntlmrelayx: https://github.com/fortra/impacket/blob/master/examples/ntlmrelayx.py
- kerbrelayx: https://github.com/dirkjanm/krbrelayx

#### Delegation

- findDelegation: https://github.com/fortra/impacket/blob/master/examples/findDelegation.py
- Impacket rbcd.py: https://github.com/fortra/impacket/blob/master/examples/rbcd.py
- SharpRBCD: https://github.com/Kryp7os/SharpRBCD
- PowerView: https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1
- Delegations: https://github.com/TheManticoreProject/Delegations

#### ADCS

> Active Directory Certificate Services

- Active Directory Certificate Services(AD CS) enumeration and abuse:
    - Certify: https://github.com/GhostPack/Certify
    - Certipy: https://github.com/ly4k/Certipy
    - certi: https://github.com/zer1t0/certi
    - PKINITtools: https://github.com/dirkjanm/PKINITtools
    - ADCSPwn: https://github.com/bats3c/ADCSPwn
- PassTheCert: https://github.com/AlmondOffSec/PassTheCert

#### ACLs and ACEs

- https://github.com/n00py/DCSync
- https://github.com/ShutdownRepo/pywhisker
- https://github.com/ShutdownRepo/targetedKerberoast

## Blue Teaming and Defensive Security

### Memshell Detection

- https://github.com/LandGrey/copagent
- https://github.com/alibaba/arthas
- https://github.com/c0ny1/java-memshell-scanner
- https://github.com/yzddmr6/ASP.NET-Memshell-Scanner

### Webshell Detection

- https://webshellchop.chaitin.cn/demo/
- https://n.shellpub.com/
- http://www.shellpub.com
- https://github.com/jvoisin/php-malware-finder
- https://www.d99net.net/

### Blue Teaming

- CobaltStrike Decrypt: https://github.com/5ime/CS_Decrypt
- BlueTeamTools: https://github.com/abc123info/BlueTeamTools
- IP Logger: https://iplogger.org/ log and track IP Addresses

### Enforcement

- https://github.com/AV1080p/Benchmarks
- https://github.com/xiaoyunjie/Shell_Script

### Incident Response

- https://github.com/grayddq/GScan
- https://github.com/ppabc/security_check
- https://github.com/T0xst/linux
- https://github.com/al0ne/LinuxCheck

### Ransomware

#### Search Engine

- 360: http://lesuobingdu.360.cn
- Tencent: https://guanjia.qq.com/pr/ls
- Venustech: https://lesuo.venuseye.com.cn
- Qianxin: https://lesuobingdu.qianxin.com
- Sangfor: https://edr.sangfor.com.cn/#/information/ransom_search

#### Decryption Tools

- Tencent: https://habo.qq.com/tool
- Kingsoft Antivirus: http://www.duba.net/dbt/wannacry.html
- Rising: http://it.rising.com.cn/fanglesuo/index.html
- Kaspersky: https://noransom.kaspersky.com/
- https://www.nomoreransom.org/zh/index.html
- https://id-ransomware.malwarehunterteam.com
- https://www.avast.com/ransomware-decryption-tools
- https://www.emsisoft.com/en/ransomware-decryption/
- https://github.com/jiansiting/Decryption-Tools

### Open-Source Honeypot

- awesome-honeypots: https://github.com/paralax/awesome-honeypots list of honeypot resources
- HFish: https://github.com/hacklcx/HFish
- conpot: https://github.com/mushorg/conpot for ICS
- MysqlHoneypot: https://github.com/qigpig/MysqlHoneypot via MySQL honeypot to get wechat ID
- Ehoney: https://github.com/seccome/Ehoney

### Reverse Engineering

#### Nice Tools

- OpenArk: https://github.com/BlackINT3/OpenArk anti-rootkit
- python arsenal for RE: https://pythonarsenal.com/ reverse toolkit
- IDA Pro: https://hex-rays.com/ida-pro/
- IDA Pro MCP: https://github.com/mrexodia/ida-pro-mcp IDA with AI
- Angr: https://github.com/angr/angr binary analysis platform
- Cutter: https://cutter.re/ open source RE platform
- UPX: https://github.com/upx/upx

#### Static Analysis

- checksec: https://github.com/slimm609/checksec
- Detect-It-Easy: https://github.com/horsicq/Detect-It-Easy
- ExeinfoPE: https://github.com/ExeinfoASL/ASL
- PEiD: https://www.aldeid.com/wiki/PEiD
- bindiff: https://www.zynamics.com/software.html
- Online Compiler: https://godbolt.org/

#### Dynamic Analysis

- Ollydbg: https://www.ollydbg.de/
- x64dbg: https://x64dbg.com/

#### Java

- jadx: https://github.com/skylot/jadx
- JEB: https://www.pnfsoftware.com/
- GDA: https://github.com/charles2gan/GDA-android-reversing-Tool
- jd-gui: https://github.com/java-decompiler/jd-gui

#### Mobile

- scrcpy: https://github.com/Genymobile/scrcpy
- android-reverse: https://github.com/WuFengXue/android-reverse

#### Python

- py2exe: https://www.py2exe.org/ py->exe
- pyinstaller: https://github.com/pyinstaller/pyinstaller py->exe
- unpy2exe: https://github.com/matiasb/unpy2exe exe->pyc
- pyinstxtractor: https://github.com/extremecoders-re/pyinstxtractor exe->pyc
- pycDcode: https://github.com/rocky/python-uncompyle6/ pyc->py
- pycDcode: https://github.com/BarakAharoni/pycDcode

#### Rust/Go/.NET

- https://github.com/cha5126568/rust-reversing-helper for rust
- https://github.com/strazzere/golang_loader_assist for golang
- https://github.com/sibears/IDAGolangHelper for golang
- https://www.jetbrains.com/zh-cn/decompiler/ for .NET
- https://github.com/dnSpy/dnSpy for .NET

#### JavaScript

- https://github.com/0xsdeo/AntiDebug_Breaker

## Cloud Security

### Resources

- TeamsSix:
    - https://github.com/teamssix/awesome-cloud-security
    - https://wiki.teamssix.com/
- lzCloudSecurity:
    - https://github.com/EvilAnne/lzCloudSecurity
    - https://lzcloudsecurity.gitbook.io/yun-an-quan-gong-fang-ru-men/
- CSA Research: https://c-csa.cn/research/results/
- HackTricks Cloud: https://cloud.hacktricks.xyz/
- Awesome-CloudSec-Labs: https://github.com/iknowjason/Awesome-CloudSec-Labs
- Aliyun OpenAPI: https://next.api.aliyun.com/api/
- Cloud Native Landscape: https://landscape.cncf.io/
- Cloud Vulnerabilities and Security Issues Database: https://www.cloudvulndb.org/

### Cloud Threat Matrix

- https://attack.mitre.org/matrices/enterprise/cloud/
- https://cloudsec.huoxian.cn/
- https://cloudsec.tencent.com/home/
- https://owasp.org/www-project-kubernetes-top-ten/ OWASP Kubernetes Top Ten - 2022
- https://www.microsoft.com/en-us/security/blog/2021/03/23/secure-containerized-environments-with-updated-threat-matrix-for-kubernetes/ threat matrix for Kubernetes

### Cloud Services

> Top 3 Cloud Service Providers：
>     - Amazon Web Services (AWS) / Microsoft Azure / Google Cloud Platform (GCP)
>     - Alibaba Cloud / Tencent Cloud / Huawei Cloud

#### Management Tools

- https://yun.cloudbility.com/ Cloud storage graphical management platform
- https://github.com/aliyun/aliyun-cli for aliyun oss
- https://github.com/aliyun/oss-browser via aliyun cli
- https://github.com/TencentCloud/cosbrowser for tencentcloud cos
- https://github.com/TencentCloud/tencentcloud-cli via tencentcloud cli
- https://support.huaweicloud.com/browsertg-obs/obs_03_1003.html for huaweicloud obs
- https://www.ctyun.cn/document/10000101/10006768 for ctyun obs
- https://www.ctyun.cn/document/10306929/10132519 for ctyun media
- https://docsv4.qingcloud.com/user_guide/development_docs/cli/install/install/ via qingcloud cli
- https://github.com/qiniu/kodo-browser for qiniu oss

#### AK/SK Exploit

- https://wiki.teamssix.com/cf/ exploit framework v0.5.0(open source)
- https://github.com/wgpsec/cloudsword
- https://github.com/CloudExplorer-Dev/CloudExplorer-Lite fit2cloud CloudExplorer
- https://github.com/mrknow001/aliyun-accesskey-Tools
- https://github.com/iiiusky/alicloud-tools
- https://github.com/NS-Sp4ce/AliyunAccessKeyTools
- https://github.com/freeFV/Tencent_Yun_tools
- https://github.com/libaibaia/cloudSec web tool for top3 + aws/qiniu
- https://github.com/wyzxxz/aksk_tool for top3 + aws/ucloud/jd/baidu/qiniu
- https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools leak detection
- https://github.com/dark-kingA/cloudTools top3 + ucloud

### Cloud Native

#### Nice Tools

- https://github.com/HummerRisk/HummerRisk open source cloud-native security platform

#### Docker

- https://github.com/wagoodman/dive exploring each layer in a docker image
- https://github.com/docker/docker-bench-security docker bench for security
- https://github.com/eliasgranderubio/dagda/ static analysis of known vulnerabilities, trojans, viruses, malware & other malicious threats
- https://github.com/teamssix/container-escape-check container escape check
- https://github.com/brant-ruan/awesome-container-escape container escape check
- https://github.com/cdk-team/CDK pentest toolkit
- https://github.com/chaitin/veinmind-tools pentest toolkit

#### Kubernetes

- https://kubernetes.io/docs/tasks/tools/
- https://github.com/etcd-io/etcd
- https://github.com/kubernetes/minikube for local clusters
- https://github.com/kubernetes-sigs/kind for local clusters
- https://github.com/kubernetes/kubeadm for deploying production or staging clusters
- https://github.com/kubernetes-sigs/cri-tools Kubelet Container Runtime Interface (CRI)
- https://github.com/derailed/k9s kubernetes cli
- https://github.com/lightspin-tech/red-kube redteam k8s adversary emulation based on kubectl
- https://github.com/DataDog/KubeHound tool for building kubernetes attack paths
- https://github.com/inguardians/peirates kubernetes pentest tool
- https://github.com/docker/docker-bench-security Docker CIS benchmarks analysis
- https://github.com/aquasecurity/kube-bench Kubernetes CIS benchmarks analysis
- https://github.com/aquasecurity/kube-hunter Hunt for security weaknesses in Kubernetes clusters

## AI Security

### Resources

- GPTSecurity: https://www.gptsecurity.info/
- Nsfocus AI Security Matrix: https://aiss.nsfocus.com/

### Model Rankings & Evaluation Platforms

- https://openrouter.ai/rankings OpenRouter AI Rankings
- https://arena.ai/leaderboard AI Arena Benchmark Leaderboard
- https://github.com/open-compass/opencompass OpenCompass LLM Evaluation Platform

### AI Agent Security & Guardrails

- https://github.com/kappa9999/ClawShield for OpenClaw
- https://semgrep.dev/blog/2026/openclaw-security-engineers-cheat-sheet cheetsheet for OpenClaw

### AI-Powered Red Teaming & Offensive Automation

> Some projects may not be fully tested. Use with caution.

- https://github.com/GreyDGL/PentestGPT Automated Penetration Testing Agentic Framework Powered by Large Language Models.
- https://github.com/NVIDIA/garak the LLM vulnerability scanner
- http://github.com/SuperagenticAI/superclaw Red-Team AI Agents
- https://github.com/usestrix/strix Open-source AI hackers to find and fix your app’s vulnerabilities
- https://github.com/jd-opensource/JoySafeter an "operating system" for security capabilities
- https://github.com/Significant-Gravitas/AutoGPT AutoGPT is a powerful platform that allows you to create, deploy, and manage continuous AI agents that automate complex workflows
- https://github.com/aliasrobotics/cai Cybersecurity AI (CAI), the framework for AI Security
- - https://github.com/vxcontrol/pentagi Fully autonomous AI Agents system
- https://github.com/Ed1s0nZ/CyberStrikeAI AI-native security testing platform
- https://github.com/KeygraphHQ/shannon Autonomous, white-box AI pentester for web applications and APIs

### Agent Skills

- https://github.com/JackyST0/awesome-agent-skills for Cursor, Claude Code, GitHub Copilot, and more
- https://github.com/affaan-m/everything-claude-code for Claude Code, Codex, Cowork, and beyond (Anthropic hackathon winner)
- https://github.com/libukai/awesome-agent-skills Quick Start, Recommended Skills, Latest News, and Practical Case Studies
- https://github.com/JimLiu/baoyu-skills for Claude Code
- https://github.com/anthropics/skills
- - https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md

## Productivity-Boosting Auxiliary Tools

### LLM

#### Open-Source Resources

- https://github.com/Hannibal046/Awesome-LLM
- https://github.com/HqWu-HITCS/Awesome-Chinese-LLM
- https://github.com/open-compass/opencompass LLM Performance Rankings
- https://github.com/deepseek-ai/awesome-deepseek-integration DeepSeek Practical Integrations
- https://github.com/raphabot/awesome-cybersecurity-agentic-ai

#### Orchestration Framework

- https://github.com/langchain-ai/langchain

#### Prompts

- https://github.com/f/awesome-chatgpt-prompts
- https://github.com/PlexPt/awesome-chatgpt-prompts-zh
- https://github.com/langgptai/wonderful-prompts

#### Deployment

- huggingface: https://huggingface.co/ Large language model download (Github of AI field)
- ollama: https://github.com/ollama/ollama Start and run large language models
- open-webui: https://github.com/open-webui/open-webui Offline WebUI
- chatbox: https://github.com/Bin-Huang/chatbox User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...) Local client for MacOS/Windows/Linux
- anythingllm: https://anythingllm.com/ Run local LLMs fast with powerful built-in tools and features. Local client for MacOS/Windows/Linux
- enchanted: https://github.com/AugustDev/enchanted Enchanted is used for chatting with private self hosted language models. Local client for iOS/MacOS
- chatbox: https://github.com/Bin-Huang/chatbox Local client for Windows/MacOS/Linux
- obsidian-copilot: https://github.com/logancyang/obsidian-copilot
- continue: https://github.com/continuedev/continue

If you want to quickly deploy LLM locally via ollama, you can refer to this technical stack:

- Run large language models: ollama
- Run large language models and deploy WebUI: ollama + open-webui
- Run large language models and deploy applications: ollama + enchanted
- Run large language models and integrate with local editors (e.g., Obsidian): ollama + copilot (Obsidian plugin)
- Run large language models and integrate with local code editors (e.g., Vscode): ollama + continue (Vscode plugin)
- Run large language models and build local RAG applications: ollama + langchain
- ...

## Productivity-Boosting Usage Methods

### How to Use Alias Quickly

Windows: Create alias.bat, activate the conda virtual environment, and run programs or tools in an isolated environment. Double-click alias.bat, restart cmd, and the configuration will take effect.

```
@echo off
:: Software
@DOSKEY ida64=activate base$t"D:\CTFTools\Cracking\IDA_7.7\ida64.exe"

:: Tools
@DOSKEY fscan=cd /d D:\Software\HackTools\fscan$tactivate security$tdir
```

Configure alias.bat to start automatically on boot:

- Enter the registry at `Computer\HKEY_CURRENT_USER\Software\Microsoft\Command Processor`;
- Create a string value `autorun` and assign it to the location of alias.bat, e.g., `D: \Software\alias.bat`;
- Restart the system and the configuration will take effect.

MacOS: Edit .zshrc, restart the shell, and the configuration will take effect:

```
# 3. Control and Command
alias behinder="cd /Users/threekiii/HackTools/C2/Behinder_v4.1/ && /Library/Java/JavaVirtualMachines/jdk-1.8.jdk/Contents/Home/bin/java -jar Behinder.jar "
alias godzilla="cd /Users/threekiii/HackTools/C2/Godzilla_v4.0.1/ && /Library/Java/JavaVirtualMachines/jdk-1.8.jdk/Contents/Home/bin/java -jar godzilla.jar "
```

### How to Optimize the Native Terminal

Windows: Optimize the native terminal through tabby + clink to achieve automatic command completion, vps ssh/ftp/sftp, output log recording and other functions:

- warp: https://github.com/warpdotdev/Warp 👍
- tabby: https://github.com/Eugeny/tabby
- clink: https://github.com/chrisant996/clink

MacOS: Optimize the native terminal through warp + ohmyzsh. Warp has built-in automatic command completion, introduces the "block" concept, and provides a more modern programming experience (Modern UX and Text Editing):

- warp: https://github.com/warpdotdev/Warp 👍
- ohmyzsh: https://github.com/ohmyzsh/ohmyzsh

![Stargazers over time](https://starchart.cc/Threekiii/Awesome-Redteam.svg?background=%23FFFFFF&axis=%23333333&line=%23009307)
