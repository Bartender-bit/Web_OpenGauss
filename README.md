# Web_OpenGauss
## 题目要求
1. (已实现) 熟练掌握 Visual C++、C、Qt、Java、PHP 或 Python 等访问数据库的方法设计和实现学生通讯录或学生选课或类似的一个小型管理信息系统。
2. (已实现) 要求具有数据的增加、删除、修改和查询的基本功能，并尽可能提供较多的查询功能，集成半以上实验一~实验五的功能，用户界面要友好。
3. (已实现) 可选内容(加分项): 数据库中存放 100 万条记录，测试访问时间;如效率较低，提供优化方案。



## 教程与建议

原文教程链接：https://blog.csdn.net/Bartender_VA11/article/details/128506980

本教程以及代码都很糙，只是在考试周赶出来的课设，很多地方冗长且不够优雅，个人不建议使用我的代码，参考即可。

对要完成该课设题目的人提供一个最简单的思路：

1. 在自己电脑上搭建一个mysql数据库，了解怎么用python对本地mysql数据库进行增删改查操作。 (B站视频很多，用几个小时就能掌握) 

2. 构思你要做的网站是什么？最简单且网上参考资料最多的是“XXX管理系统”，只要拥有登陆注册，身份系统（用户、管理员），简单的修改操作即可。（具体思路可以看我的CSDN教程或网上众多教程）

3. 构思好你要做的网站后，构思你所需要的表结构，这里不用考虑最优化表结构，各个表设计的不够好有冗余也无所谓，只要确保数据能正常存储和读取即可。

4. 用你在第一步学到的东西，创建表，插入随便编的表数据。

5. 有了数据后接下来就要将数据渲染到浏览器上，这意味着你要做网页了，用bootstrap插件即可，该仓库的/static/js/下已经提供，教程可以看bootstrap官网文档视频。

6. 有了bootstrap插件，做出三个简单网页只需两三小时。（往里无脑放入一些表格背景图片就行）

7. 实现相关函数，将数据库里的数据和网页上的数据绑定起来，从而让网页能显示数据库里的数据，over。



## 本仓库代码运行方式：

1、填好你的数据库IP，数据库在本地就填127.0.0.1，在服务器就填服务器IP。

2、配置好OpenGauss数据库连接包jaydebeapi，代码里的目录也要填对。

3、运行主程序app.py即可
