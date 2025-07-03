**漏洞描述**

MinIO中存在一处信息泄露漏洞，由于Minio集群进行信息交换的9000端口，在未经配置的情况下通过发送特殊HPPT请求进行未授权访问，进而导致MinIO对象存储的相关环境变量泄露，环境变量中包含密钥信息。泄露的信息中包含登录账号密码。

**漏洞环境**

Fofa语法：(banner="MinIO" || header="MinIO" || title="MinIO Browser") && country="CN"

**漏洞复现**

/minio/bootstrap/v1/verify接口导致信息泄露

使用泄露的用户密码可以登陆minio控制台