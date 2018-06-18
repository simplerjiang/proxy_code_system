# 代理网站API系统

##### 全部API均使用GET方式请求，使用POST会返回错误提示！
##### 所有API都写于main_app/views/api.py 下 



## 代理账户开户API
url:http://127.0.0.1:8000/api/admin_proxy_account_add_api/?admin_code=testtest&proxy_username=Kong4&proxy_password=testtest&proxy_ad=测试广告&proxy_balance=88
#### 参数:
admin_code = 管理员代码

proxy_username = 代理账户名

proxy_password = 代理密码

proxy_ad = 代理广告（不写就是为空字符串)

proxy_balance = 代理账户金额（不写默认为0)

proxy_level = 代理等级（不填就是1，最高20级）

up_proxy = 上级代理用户名（不填写就是无）

#### 返回值： (全部json格式）

"Fail,account already existed" 账户已存在，创建失败

"Success" 创建成功

"Error, admin code wrong"  管理员代码错误

"Error,bad request method POST" 错误的请求模式

---

## 代理账户充值

url:http://127.0.0.1:8000/api/admin_proxy_account_topup/?admin_code=testtest&proxy_username=测试账号1&money=30

** 说明：试用此功能进行充值会生成一个充值订单，显示给代理账户看!所以如果需要充值请用此API进行充值！并且金额不能低于0元 **

#### 参数：

admin_code 管理员代码

proxy_username 代理账号

money 添加金额


#### 返回值:
["Success", "90"] 成功，第二个参数是目前的金额

"Error, admin code wrong"  管理员代码错误

"Error,bad request method POST" 错误的请求模式

"Proxy account not existed" 代理账号不存在

"Error, wrong number!" 充值金额低于0或等于0

---

## 代理账户金额修改

注意！此API功能用于清零，如果操作不当可能造成严重后果。且输入值必须大于等于0

** 请不要将此API用于充值！因为此API不会生成充值订单！**

url:http://127.0.0.1:8000/api/admin_proxy_account_balance_setup/?admin_code=testtest&proxy_username=测试账号1&money=30

#### 参数：

admin_code 管理员代码

proxy_username 代理账号

money 设置金钱

#### 返回值:

["Success", "90"] 成功，第二个参数是目前的金额

"Error, admin code wrong"  管理员代码错误

"Error,bad request method POST" 错误的请求模式

"Proxy account not existed" 代理账号不存在

"Error, money type wrong" money参数不是一个数字

"Error, money less than 0" money参数小于0

---

## 代理金额查询 (管理员及代理可用，不需要管理员代码）

url:http://127.0.0.1:8000/api/proxy_account_balance_check/?proxy_username=测试账号1

#### 参数：

proxy_username 代理账号

#### 返回值：

"30" 正确返回则返回目前余额(字符串）

"Error,bad request method POST" 错误的请求模式

"Proxy account not existed" 代理账号不存在

---

## 管理员用——修改代理账号密码

url:http://127.0.0.1:8000/api/admin_proxy_account_change_password/?proxy_username=测试账号1&admin_code=tedttest&proxy_new_password=MyNewPassword

#### 参数：

admin_code 管理员代码

proxy_username 代理账号

proxy_new_password 新密码

#### 返回值：

"success" 代表修改成功

"Error,admin code wrong!" 管理员密链错误

"Error, account is Not exsited" 如果账户不存在则返回此警告

"Error,bad request method POST" 错误的请求模式

---

## 管理员设置软件

url:http://127.0.0.1:8000/api/admin_set_software/?admin_code=testtest&software_id=1&software_name=测试软件&software_each_time=720&software_cost=10

#### 参数：

admin_code 管理员密链

software_id 软件id（必须是唯一！）	

software_name 软件名字

software_version_number 软件版本号（选填，不填写就默认为V1.0)

software_each_time 套餐时间

software_cost 套餐价格

software_try 是否可以试用（1为可以，0为不可以）

software_try_hours 如果可以试用，试用的小时（如果不可以，请不用填，如果可以就必填）


#### 返回值：

"success" 成功创建

"software_id already excited" 软件ID已经存在，请换一个ID

"Error,admin code wrong!" 管理员密链错误

"Error,bad request method POST" 错误的请求模式

---

## 管理员更新软件版本号

url: http://127.0.0.1:8000/api/admin_update_software_version/?admin_code=testtest&software_id=1&software_version_number=V1.1

#### 参数：

admin_code 管理员密链

software_id 软件ID

software_version_number 新版本号

#### 返回值：

"success" 成功修改

"software_id do not excited" 软件不存在或软件ID错误

"Error,admin code wrong!" 管理员密链错误

"Error,bad request method POST" 错误的请求模式

---

## 管理员更新软件套餐价格

url:http://127.0.0.1:8000/api/admin_update_software_cost/?admin_code=testtest&software_id=1&software_each_time=721&software_cost=5

#### 参数：

admin_code 管理员密链

software_id 软件ID

software_each_time 套餐时间

software_cost 套餐价格

#### 返回值：

"success" 设置成功

"software_id do not excited" 软件不存在或软件ID错误

"Error,admin code wrong!" 管理员密链错误

"Error,bad request method POST" 错误的请求模式

---
# 代理专用API

## 代理登陆

代理登陆后会返回一个TOKEN(密链）,代理的其他操作API都需要此密链，

每次调用一次登陆函数就会重新定义并返回一次密链，所以具有时效性

url:http://127.0.0.1:8000/api/proxy_account_login/?proxy_username=测试账号&proxy_password=testtest


#### 参数：

proxy_username 用户名

proxy_password 密码



#### 返回值：

"D4y2L5P9w5z9e8" 如果成功，将返回15位数的特定随机密链（这里被称为token)

"Error, account is Not exsited or password is fail" 如果账号密码或账户不存在都返回此警告

"Error,bad request method POST" 错误的请求模式



---



## 代理修改代理账户密码

url: http://127.0.0.1:8000/api/proxy_account_change_password/?proxy_username=测试账号1&proxy_password=testtest&proxy_new_password=testtest



#### 参数：

proxy_username 用户名

proxy_password 密码

proxy_new_password 新的密码



#### 返回值：

"success" 代表修改成功

"Error, account is Not exsited or password is fail" 如果账号密码或账户不存在都返回此警告

"Error,bad request method POST" 错误的请求模式



---




## 代理设置广告

url: http://127.0.0.1:8000/api/proxy_account_ad_change/?token=D4y2L5P9w5z9e8&ad=测试广告



#### 参数：

token 代理客户login函数成功后返回的密链，每个账号都有一个独立的密链，并且每次登陆后都会返回一个新的密链

ad 需要设置的广告（15字以内）



#### 返回值：

"success" 修改成功

"Error, account is Not exsited or token is fail" 如果token错误或账户不存在都返回此警告

"Error,bad request method POST" 错误的请求模式



---



## 请求代理全部信息

url:http://127.0.0.1:8000/api/proxy_info_get/?proxy_username=测试账号1



#### 参数：

proxy_username 用户名



#### 返回值:

["name","ad","balance","level"] 成功返回会有以下几个数值，第一名字，第二广告，第三余额，第四是级别。

"Error, account is Not exsited" 如果账户不存在返回此警告

"Error,bad request method POST" 错误的请求模式


---

##获取所有软件原价信息（原价！单个代理请使用另一个API，因为代理的价格会有一定的折扣)

url:http://127.0.0.1:8000/api/get_all_software/

####参数:

无

####返回值：

[[1, "\u6d4b\u8bd5\u8f6f\u4ef6", "V1.1", 720, 10, false], [2, "\u6d4b\u8bd5\u8f6f\u4ef62", "V1.0", 720, 10, false], [3, "\u6d4b\u8bd5\u8f6f\u4ef63", "V1.2", 720, 10, false], [4, "\u6d4b\u8bd5\u8f6f\u4ef64", "BetaV0.3", 720, 1, true]]

[[软件id,软件名,软件版本号,套餐时间,套餐价格,是否试用,试用时间（小时）],[软件id,软件名,软件版本号,套餐时间,套餐价格,是否试用,试用时间（小时）]]

---

##代理获取价格（此API获取得是代理打折后得价格）

url:http://127.0.0.1:8000/api/get_all_software_TOKEN/?TOKEN=XXXXXXXXX

####参数:

TOKEN 代理密链

####返回值：

[[1, "\u6d4b\u8bd5\u8f6f\u4ef6", "V1.1", 720, 10, false], [2, "\u6d4b\u8bd5\u8f6f\u4ef62", "V1.0", 720, 10, false], [3, "\u6d4b\u8bd5\u8f6f\u4ef63", "V1.2", 720, 10, false], [4, "\u6d4b\u8bd5\u8f6f\u4ef64", "BetaV0.3", 720, 1, true]]

[[软件id,软件名,软件版本号,套餐时间,套餐价格,是否试用],[软件id,软件名,软件版本号,套餐时间,套餐价格,是否试用]]

"Fail, require TOKEN!" 错误，需要代理密链

"Error, bad request method POST" 错误的请求方式

"Fail, wrong TOKEN!" 密链错误

---



## 代理提卡

url:http://127.0.0.1:8000/api/proxy_get_software_code/?token=w5M3r4U6P7t8dU0&HowMuch=3&software_id=1



#### 参数：

token 代理账户密链

software_id 软件ID

HowMuch 提多少张



#### 返回值：

["n7o7I7M3I4", "r6X7D6O5g1", "c0Z4b3s6F7"] 如果成功，将返回一个列表

"Error, HowMuch lower than 0" 提卡数量小于或等于0

"Error, account is Not exsited or token is fail" 如果token错误或账户不存在都返回此警告

"Error,bad request method POST" 错误的请求模式

"software_id do not excited" 软件不存在或软件ID错误

["Balance not enough!","100"] 如果余额不足以提卡，就会返回第一个是提示，第二个是目前的余额





---



## 创建授权（续费授权）

url:http://127.0.0.1:8000/api/authorization_make/?software_code=R4I0Z9r0h5&customer_QQ=123123&bot_QQ=123123



#### 参数：

software_code 软件卡密

customer_QQ  客户QQ，用于保存修改机器人

bot_QQ 机器人QQ



#### 返回值:

["success","2018-05-06 15:01:35"] 如果成功，第二个值会为到期时间

"Code Fail" 卡密错误

"Error,bad request method POST" 错误的请求模式

"Code already used" 卡密已经被使用过了



---



## 授权查询

url:http://127.0.0.1:8000/api/authorization_check/?software_id=1&bot_QQ=123123



#### 参数：

software_id 软件id

bot_QQ 机器人QQ



#### 返回值：

["success","2018-05-06 15:01:35","测试广告"] 	如果成功，第二个值会为到期时间，第三个是代理商的广告

["try_success","2018-05-06 15:01:35"] 如果是试用，则返回此内容，不返回代理广告

"Fail" 已过期或不存在

"Error,bad request method POST" 错误的请求模式


---



## 更换授权机器人QQ(试用授权无法更换）

url:http://127.0.0.1:8000/api/authorization_change/?software_id=1&new_bot_QQ=1414&customer_QQ=123123



#### 参数：

software_id 软件id

new_bot_QQ 新机器人QQ

old_bot_QQ 旧机器人QQ

customer_QQ 客户QQ 



#### 返回值：

["success","1414"] 如果修改成功，第二个返回目前的机器人QQ

"Error,bad request method POST" 错误的请求模式

"Fail" 授权不存在或过期

"Wrong QQ Type" 错误的QQ类型，就是说它不是数字



---

## 代理开下级账户

url:http://127.0.0.1:8000/api/proxy_open_new_account/?TOKEN=XXXXXXXXXXXXX&proxy_username=XXXX&proxy_password=XXXXX&proxy_ad=广告&proxy_level=10

#### 参数:

TOKEN = 代理账户TOKEN

proxy_username = 下级代理账户名

proxy_password = 下级代理密码

proxy_ad = 下级代理广告（不写就是为空字符串)

proxy_level = 下级代理等级（只能够填写小于当前开户级别的代理级别）

#### 返回值:

"success" 成功创建

"Fail,proxy_level is not allow" 下级代理账号等级高于本账户等级，或小于0

"Fail,account already existed" 账户已存在

"Error, account is Not exsited or token is fail" TOKEN值验证失败

"Error, bad request method POST" 错误的请求方式


---

## 代理向下级转账（仅限上级向下级转账，其他都不可行）

url:http://127.0.0.1:8000/api/proxy_transfer_money/?TOKEN=XXXXXXXXXXXX&proxy_name=XXXX&money=10

#### 参数：

TOKEN 代理账号的密链

proxy_name  收款的账户用户名

money 需要转账的数额

#### 返回值：

["success", "12161.25"] 第一个是成功，第二个是目前账号余额

"Error, bad request method POST" 错误的

"Error, account is Not exsited or token is fail" 账号密链错误

"Error, proxy_name is wrong!" 收款的账户用户名错误！

"Error, Not allow to transfer others accounts!" 禁止转账给非下级代理

"Your balance not enought!" 你的余额不足

---

## 代理申请提现（提现金额必须大于10)

url:http://127.0.0.1:8000/api/proxy_get_out_money/?TOKEN=123ddd&money_account_name=支付宝&money=100&money_account_num=130000000

#### 参数：

TOKEN

money 提现金额 （输入-1等于提现所有金额）

money_account_name 提现方式（必须为特定名字，"支付宝" "QQ" "微信"，如果不是会返回错误）

money_account_num 提现账号名（手机号或邮箱号）

money_account_name 户主名 （用于验证收款账号是否正确）

#### 返回值：

"success, please wait" 提现申请成功，请等待

"Error, money is lower than 10!" 提现金额过少，必须大于0 

"Error, money_account_name is wrong!" 提现方式错误（必须为特定名字，"支付宝" "QQ" "微信"，如果不是会返回错误）

"Error, bad request method POST" 错误的

"Error, account is Not exsited or token is fail" 账号密链错误

"Error, money is wrong!" 金额设置错误，可能是低于0元，注意 -1是否为英文符号

"Balance is not enought" 账户余额不足

"Error, miss money_account_name" 缺少户主名


