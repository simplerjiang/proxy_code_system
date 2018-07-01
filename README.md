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

---

## 架设环境及说明：

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

## 付费客制化

本网站由simplerjiang 完成，如果你有定制此网站需求，可联系。
邮箱：jiangsimpler@gmail.com
QQ: 1013171256
