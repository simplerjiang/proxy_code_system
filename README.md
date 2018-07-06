# 软件提卡、授权、代理人员系统三合一

## 网页展示

#### 主页（代理账户后台）

![主页](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/index.png)

#### 登陆页面

![登陆页面](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/login.png)

#### 注册页面

![注册页面](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/reg.png)

#### 购买软件卡密页面

![购买软件卡密页面](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/software_list.png)

![选择数量](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/buy_item.png)

#### 提卡卡密

![提取卡密](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/get_code_list.png)

#### 余额不足页面（所有错误页面都有，但是我没截图）

![余额不足](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/wrong.png)

#### 个人资料修改页面

![个人资料](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/profile.png)

#### 转账页面

![转账](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/transfer.png)

#### 管理下级代理

![管理下级](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/contorl_down_proxy.png)

#### 管理授权

![管理授权](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/contorl_auth.png)

#### 网站管理员登陆

![网站管理员](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/admin_login.png)

#### 网站管理员页面

![网站管理员页面](https://github.com/simplerjiang/proxy_code_system/blob/master/README_img/admin_control.png)



---

## 功能说明:

此网站系统是集成了以下多种功能：

#### 软件授权验证系统

通过API接口进行验证使用者是否拥有授权。
软件可设置使用时间，如使用者没有授权，将自动添加试用授权。

#### 网站自动生成卡密系统

内部对接授权系统，实现全自动生成卡密，无需人工放入卡密。
网站系统内置账户金额，用户自助选卡买卡，自助充值授权。

#### 多级别代理系统

原定有20级不同的VIP，VIP20 为最高级别，VIP0 为最低级别。每一级折扣为0.5折，既VIP20级
为免费提卡，VIP5级为2.5折。同时代理可开设下级代理账号（低于开通账号的等级），如下级账户
购买了卡密，将有一部分金额分成给上级代理，使得代理有钱可赚。

#### 提现系统

设定有提现系统，用户可申请提现，并由管理员完成。

#### 公告系统

公告系统，将轮番展示公告在用户界面上。

#### 安全性

经测试，可有效防止注入，伪造等普遍攻击方式。

并在上一次更新中，加入了授权查询API的可加密选项。

#### 一键启动

目前支持Windows系统32位与64位一键部署环境与启动。
详细说明请浏览下面 一键启动说明

---

## 待加入的内容

- [X] API授权查询安全加密

- [X] windows系统自动化部署脚本

- [ ] Linux系统自动化部署脚本

- [ ] 工单系统

- [ ] 将主版本(master)修改为以ip为判断根据，代替机器人QQ

- [ ] 欢迎提出更多建议，如合理我将加入待更新的内容中。

---

## 架设环境及说明：

#### 一键部署与启动

打开 "便捷搭建与开启.exe" 文件

如果你没有安装Python请先选择 "1.部署Python环境"

完成后请重新打开此文件，并选择 "2.下载模块依赖"

不出意外的话，都是正常完成。便可选择 "3.开启网站"

请保证80端口不被占用，之后就可以通过服务器域名或IP访问到。

如果你要在本机上测试网站，可选择 "4.测试网站"

与上相同，可通过http://127.0.0.1:8000/ 访问。

注意！！！步骤1,2是第一次运行时使用，不需要每次都使用！

本方法只适用于没有Python使用基础的朋友，如果你懂一些编程基础，

推荐根据下面的方式进行手动部署。

#### 简易安装

简易安装主要应用于windows系统，低并发条件下，如有需要高并发或追求更好的性能，请试用专业安装。

本网站系统由 `Python3.6.5 + Django1.8.2` 环境下编写。

新手安装说明及步骤： [点击打开后继续点击View Raw](https://github.com/simplerjiang/proxy_code_system/blob/master/%E4%B8%BB%E7%AB%99%E6%9E%B6%E8%AE%BE%E6%95%99%E7%A8%8B.docx)

需要的依赖模块（已在安装步骤中集成）：
``` python3
Django==1.8.3
mysqlclient==1.3.12
pytz==2018.4
```

#### 专业安装

推荐使用：nginx + uwsgi + django + Unix系统
由于步骤繁杂，在这里不做多介绍，可自行百度。

---
## 详细说明

#### 数据库说明

本版本使用的是Sqlite，数据库文件为：db.sqlite3。此数据库文件是有一定的测试内容，你可以在admin界面将它删除，或复制 “空白数据库（NULL DB)”中的数据库，并覆盖主文件夹中的db.sqlite3
。django可采用Mysql或其他数据库，请自行百度教程，或联系我进行付费客制化。提醒：如果要更换其他数据库，请先进行数据迁移，保证新数据库已经包含有表结构。

#### 管理后台

本网站使用的是django自带的管理员后台，Url: 127.0.0.1/admin
默认管理员用户是Kong ，密码123，如需自己创建，请参考[教程](https://jingyan.baidu.com/article/f71d6037770a7b1ab641d1b6.html)

#### API文档

我有专门写了一份本网站的API文档，请点击[API文档](https://github.com/simplerjiang/proxy_code_system/blob/master/README_api.md)

#### 日志

在log文件夹下，有记录所有的错误以及底层sql操作。

#### 付费客制化

本网站由simplerjiang 完成，如果你有定制此网站需求，可联系。
邮箱：jiangsimpler@gmail.com
QQ: 1013171256

---

## 未完待续...

有许多具体操作以及设置，晚些我会写入文档中。

本网站以及经过两个月测试，并有正式上线并用于生产环境中。

如发现bug，请发送邮件到：jiangsimpler@gmail.com
