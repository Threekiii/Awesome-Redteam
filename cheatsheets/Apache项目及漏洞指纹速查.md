# Apache项目及漏洞指纹速查

## Apache软件基金会

Apache 软件基金会，全称：**Apache Software Foundation**，简称：**ASF**，成立于 1999 年 7 月，是目前世界上最大的最受欢迎的开源软件基金会，也是一个专门为支持开源项目而生的非盈利性组织。

## 基础组件项目

### Apache（httpd） 

Apache是开源 HTTP 服务器，支持HTML、图片等静态资源服务，可以用来部署静态网站，类似于 Nginx。

- Apache HTTPd 多后缀解析漏洞
- Apache HTTPd 换行解析漏洞 CVE-2017-15715
- Apache HTTP Server 2.4.48 mod_proxy SSRF漏洞 CVE-2021-40438
- Apache HTTP Server 2.4.49 路径穿越漏洞 CVE-2021-41773
- Apache HTTP Server 2.4.50 路径穿越漏洞 CVE-2021-42013

### Tomcat

Apache Tomcat是最主流的Java开源 Web 应用服务器，支持 Java Servlet, JavaServer Pages, Java Expression Language 和 Java WebSocket 技术。

- Apache Tomcat8 弱口令+后台getshell漏洞
- Apache Tomcat AJP 文件包含漏洞 CVE-2020-1938

- Apache Tomcat PUT方法任意写文件漏洞 CVE-2017-12615

### Commons

Apache Commons 是包含一系列 Java 公共组件的项目，可以理解为 Java 开发工具包、公共类库。

例如`commons-lang3` 类库：

```
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-lang3</artifactId>
</dependency>
```

### POI

Apache POI 提供了一系列的 Java API 对 Microsoft Office 格式档案读写处理，如：Excel、Word、PowerPoint 等文件的读写。

### HttpComponents

Apache HttpComponents 提供了 HTTP 和相关协议的一系列 Java 组件和工具集，包括：HttpCore、HttpClient、HttpAsyncClient 三个组件。

例如HttpClient：

```
<dependency>
  <groupId>org.apache.httpcomponents.client5</groupId>
  <artifactId>httpclient5</artifactId>
  <version>5.0.1</version>
</dependency
```

### logging services

Apache logging services即 Apache 日志服务，其中 Log4j 是使用最多的日志框架，另外还包含还有 Log4j 2、log4php、log4cxx 等其他语言的日志框架。

- Apache Log4j Server 反序列化命令执行漏洞 CVE-2017-5645
- Apache Log4j2 lookup JNDI 注入漏洞 CVE-2021-44228

### Ant

Apache Ant 是一个比较老的 Java 项目编译和构建工具，现在已经用的比较少了，已经被 Maven/ Gradle 替代了。

### Maven

Apache Maven 是现在最主流的软件项目管理工具之一，提供项目自动编译、单元测试、打包、发布等一系列生命周期的管理。

### Subversion

Apache Subversion 即SVN，是 Apache 开源的版本控制软件，支持代码版本控制、文件版本控制等。

## Web项目

### APISIX

Apache APISIX 是一个基于 OpenResty 和 Etcd 实现的动态、实时、高性能的 API 网关，目前已经进入 Apache 进行孵化，提供了丰富的流量管理功能。

- Apache APISIX 默认密钥漏洞 CVE-2020-13945

### Struts/Struts2

Apache Struts 是一个免费开源的 MVC 框架，用于创建 Java web 应用程序。Struts2 + Spring + Hibernate 三大框架即Java Web 框架三剑客。

注意：Struts 漏洞较多，随着 Spring MVC、Spring Boot 的崛起，Struts现已被逐渐淘汰。

- Struts2 S2-001 远程代码执行漏洞
- Struts2 S2-005 远程代码执行漏洞
- Struts2 S2-007 远程代码执行漏洞
- Struts2 S2-008 远程代码执行漏洞
- Struts2 S2-009 远程代码执行漏洞
- Struts2 S2-012 远程代码执行漏洞
- Struts2 S2-013 远程代码执行漏洞
- Struts2 S2-015 远程代码执行漏洞
- Struts2 S2-016 远程代码执行漏洞
- Struts2 S2-032 远程代码执行漏洞
- Struts2 S2-045 远程代码执行漏洞
- Struts2 S2-046 远程代码执行漏洞
- Struts2 S2-048 远程代码执行漏洞
- Struts2 S2-052 远程代码执行漏洞
- Struts2 S2-053 远程代码执行漏洞
- Struts2 S2-057 远程代码执行漏洞
- Struts2 S2-059 远程代码执行漏洞
- Struts2 S2-061 远程代码执行漏洞

### FreeMarker

Apache FreeMarker 是一个基于模板和数据生成文本输出 HTML 页面、电子邮件、配置文件、源代码等的一个 Java 模板引擎库。

### Velocity

Apache Velocity 是一个基于 Java 语言的模板引擎，它允许任何人使用简单而强大的模板语言来引用 Java 代码中定义的对象。

注意：Velocity 长期未更新，Spring Boot 1.5.x 之后不再支持 Velocity。

- Apache Solr Velocity 注入远程命令执行漏洞  CVE-2019-17558

### Tapestry

Apache Tapestry是一个面向组件的 Web 框架，用于在 Java 中创建高度可伸缩的 Web 应用程序。

### Shiro

Apache Shiro 是一个功能强大且易于使用的 Java 安全框架，可用于身份验证、授权、加密和会话管理等。

- Apache Shiro 1.2.4反序列化漏洞 CVE-2016-4437
- Apache Shiro 认证绕过漏洞 CVE-2020-1957

## 分布式项目

### Dubbo

Dubbo最初是由阿里巴巴开源的分布式服务框架（RPC），一段时间停止维护后，后来又重启维护并捐给了 Apache 软件基金会。

默认端口：20880

- Apache Dubbo Java反序列化漏洞 CVE-2019-17564

### Thrift

Apache Thrift 也是一款优秀的、非常轻量级的 RPC 框架，最初由 Facebook 进行开发，后来捐给了 Apache 软件基金会。

### Zookeeper

Apache Zookeeper 是一个可以用来支持高度可靠的分布式服务协调中间件，是 Google Chubby 的一个开源实现，可用于做配置中心、分布式锁等。

现在市面上的一些主流的开源项目都有 Zookeeper 的身影，如：Hadoop、Dubbo、Kafka、ElasticJob 等。

默认端口：2181

### Curator

Apache Curator 是 ZooKeeper 的 Java 客户端，它包括一系列高级 API 和工具，简化了使用 ZooKeeper 的操作，可以更容易、可靠地使用 ZooKeeper。

### SkyWalking

Apache SkyWalking 是一个可观测性分析平台和应用性能管理系统，提供分布式跟踪、指标监控、性能诊断、度量汇总和可视化一体化的解决方案。

- Apache Skywalking 8.3.0 SQL注入漏洞

### ShardingSphere

Apache ShardingSphere 是由一组分布式数据库中间件解决方案组成的开源生态系统，包括 3 个独立的产品：JDBC, Proxy & Sidecar (计划中)。它们都提供了数据分片、分布式事务和数据库编排功能，适用于 Java 同构、异构语言和云原生等多种场景。

## 搜索项目

### Lucene+Solr

Apache Lucene 是一个顶级的开源搜索框架，包括一个核心搜索库：Lucene core，以及一个搜索服务器：Solr。

Solr 是使用 Lucene Core 构建的高性能搜索服务器。Solr 具有高伸缩性，提供完全容错的分布式索引、搜索和分析功能。

Solr默认端口：8983

- Apache Solr RemoteStreaming 文件读取与SSRF漏洞
- Apache Solr XML 实体注入漏洞 CVE-2017-12629
- Apache Solr 远程命令执行漏洞 CVE-2017-12629
- Apache Solr 远程命令执行漏洞 CVE-2019-0193
- Apache Solr Velocity 注入远程命令执行漏洞  CVE-2019-17558

## 消息中间件项目

### ActiveMQ

Apache ActiveMQ 是一个多协议开源消息中间件，是目前最流行的基于 Java 的消息中间件之一。

默认端口：8161

- Apache ActiveMQ 反序列化漏洞 CVE-2015-5254
- Apache ActiveMQ任意文件写入漏洞 CVE-2016-3088

### RocketMQ

Apache RocketMQ是一个重量级、极具竞争力的消息队列产品，是由阿里巴巴 2012 年开源的分布式消息中间件，也是一款轻量级的数据处理平台，2016 年捐给了 Apache 软件基金会。

### Kafka

Apache Kafka 也是一款重量级开源项目，最初由 Linkedin 公司进行开发，后来捐给了 Apache 软件基金会。

Apache Kafka 它是一种分布式、高吞吐量的发布订阅消息系统（MQ），它的最大的特性就是，可以实时好处理大量数据以满足各种需求和业务场景。

默认端口：5601

- Kibana 本地文件包含漏洞 CVE-2018-17246
- Kibana 原型链污染导致任意代码执行漏洞 CVE-2019-7609

## 大数据及数据库项目

### Airflow

Apache Airflow是Airbnb开源的一款数据流程工具，目前是Apache孵化项目。以非常灵活的方式来支持数据的ETL过程，同时还支持非常多的插件来完成诸如HDFS监控、邮件通知等功能。

- Apache Airflow 默认密钥导致的权限绕过 CVE-2020-17526
- Apache Airflow 示例DAG中的命令注入 CVE-2020-11978
- Apache Airflow Celery 消息中间件命令执行 CVE-2020-11981

### Hadoop

Apache Hadoop 是一种高可靠、可伸缩、分布式大数据处理框架，也是一套大数据行业公认的标准框架，成立于 2002 年，曾是 Apache Lucene 的子项目之一，2008 年正式成为 Apache 的顶级项目。

默认端口：50070

- Hadoop YARN ResourceManager 未授权访问

### HBase

Apache HBase 是一个建立在 Hadoop HDFS 的非关系数据库，以分布式、可扩展进行大数据存储，如果需要对大数据进行随机、实时的读写访问时，可以使用 Apache HBase。

### Pig

Apache Pig 是一个基于 Hadoop 的大数据分析平台，是 Map Reduce 的一个抽象，提供类似于 SQL 的面向数据流的 Pig Latin 高级语言。

Pig Latin 提供了各种操作符，以及丰富的数据类型，从而可以很轻松地执行 Map Reduce 任务。

### Hive

Apache Hive 是一个基于 Hadoop 的数据仓库工具，用来提取、转化和加载数据，可以将 Hadoop 原始结构化数据映射为 Hive 中的一张表，并提供了类似 SQL 的 HiveQL 语言查询功能。

### Spark

Apache Spark 是一个用于大规模数据处理的统一分析引擎，也被认为是第二代大数据技术，第一代是基于 Hadoop 的 Map Reduce 模型。

Apache Spark 本身不会进行分布式数据的存储，所以必须要集成其他的分布式文件系统才能工作，一船要与 Apache Hadoop 的 HDFS 结合使用，也可以选择其他的数据系统平台进行集成。

- Apache Spark 未授权访问漏洞

### Flink

Apache Flink 是一个分布式处理引擎框架，用于无边界和有边界数据流上的有状态计算。Flink 被设计用于在所有常见的集群环境中运行，以内存速度和任何规模执行计算。

默认端口：8081

- Apache Flink 小于1.9.1远程代码执行 CVE-2020-17518
- Apache Flink 目录遍历漏洞 CVE-2020-17519

### Storm

Apache Storm 是一个分布式实时计算系统，能够轻松可靠地处理数据流，就像 Hadoop 那样进行实时批处理，并且可以与任何编程语言一起使用，而且使用起来非常方便。

### Cassandra

Apache Cassandra 是一款可伸缩、高可用、高性能去中心化的分布式数据库，是 Facebook 在 2007 年为了解决消息收件箱搜索问题而开始设计的，后来被转移到了 Apache 软件基金会成为顶级项目。

### CouchDB

Apache CouchDB 是一个面向文档的分布式数据库，它以 JSON 作为存储格式，JavaScript 作为查询语言，提供直观可靠的 Restful API 接口进行操作，最显著的特点就是支持多主复制。

默认端口：5984

## 编程语言及工具项目

### Groovy

Apache Groovy 是一个功能十分强大的基于 JVM 平台的动态编程语言，语法与 Java 十分相似，并且兼容 Java，但 Groovy 要更简洁、优美，更易于学习，开发效率也非常高。

### NetBeans

NetBeans 是一款老牌的开源开发工具（IDE），集成开发环境和应用框架，支持 Java, JavaScript, PHP 等更多编程语言，最初由 SUN 公司开发，后来被 Oracle 收购，再后来被 Oracle 捐给了 Apache 软件基金会。

## 其他项目

### OfBiz

Apache OFBiz是一个电子商务平台，提供了创建基于最新J2EE/XML规范和技术标准，构建大中型企业级、跨平台、跨数据库、跨应用服务器的多层、分布式电子商务类WEB应用系统的框架。

OFBiz提供了一整套的开发基于Java的web应用程序的组件和工具。包括实体引擎、服务引擎、消息引擎、工作流引擎、规则引擎等。

- Apache OfBiz 反序列化命令执行漏洞CVE-2020-9496

### Unomi 

Apache Unomi 是一个基于标准的客户数据平台（CDP，Customer Data Platform），用于管理在线客户和访客等信息，以提供符合访客隐私规则的个性化体验。

- Apache Unomi 远程表达式代码执行漏洞 CVE-2020-13942

