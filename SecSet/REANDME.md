## 环境配置

安装文件夹下的`python-2.7.18rc1.msi`，安装后将以下路径加入环境变量中

`C:\Python27`和`C:\Python27\Scripts`

## 提醒

运行脚本前请确保管理员账户已设置密码，且密码复杂度符合要求

## 禁用的服务有

lmhosts     禁用NetBios

LanmanServer  禁用445端口和删除默认共享

ClipSrv     clipbook

Browser     computer brower

RemoteRegistry remote registry service

SSDPSRV     ssdp discovery service

W32Time     windows times

## 导入的注册表键值作用

禁用445端口

 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\NetBT\Parameters 新建 QWORD（64位）值 名字为 SMBDeviceEnabled 值为0

禁止空连接

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\LSA 将RestrictAnonymous值改为1

关闭自动播放

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers] 的 DisableAutoplay 值设置为1

## 导入的组策略管理模板作用有

密码最短使用时间

MinimumPasswordAge = 0

密码最长使用时间

MaximumPasswordAge = 30

密码最小值

MinimumPasswordLength = 12

密码必须符合复杂性要求

PasswordComplexity = 1

强制密码历史

PasswordHistorySize = 0

登录次数限制

LockoutBadCount = 3

指定分钟后重置限制次数

ResetLockoutCount = 30

指定分钟后可再次尝试密码

LockoutDuration = 30

更改默认管理员账户名

NewAdministratorName = "Administrator1"

更改默认的来宾账户名

NewGuestName = "Guest"

禁用用可还原的加密来存储密码

ClearTextPassword = 0

禁止匿名枚举

LSAAnonymousNameLookup = 0

开启管理员账户

EnableAdminAccount = 1

禁用来宾账户

EnableGuestAccount = 0



开启审核策略

审核系统事件成功、失败

AuditSystemEvents = 3

审核登录事件成功、失败

AuditLogonEvents = 3

对审核策略更改成功、失败

AuditPolicyChange = 3

审核账户管理成功、失败

AuditAccountManage = 3

审核账户登录成功、失败

AuditAccountLogon = 3



后面的为注册表对应键值，无需手动修改