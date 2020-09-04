#_*_coding:UTF-8_*_
#导入包
import os
import sys
import re
from time import sleep


# 获取系统编码格式，防止输出乱码
type=sys.getfilesystemencoding()

# 定义要禁用的服务，可以直接在列表中添加用逗号隔开，服务名用引号包裹
sername = ['lmhosts','LanmanServer','Browser','RemoteRegistry','SSDPSRV','W32Time']

# 执行的语句
importReg = 'reg import ./1.reg'
importSec = 'secedit /configure /db 1.sdb /cfg 1.inf /quiet'


# 禁用服务
for i in sername:
    disableServer = 'sc config ' + str(i) + ' start= disabled'

    os.system(disableServer)
    # print("已禁用"+i+"服务").decode('utf-8').encode(type)


# 导入注册表
try:
    os.system(importReg)
    print("已禁用445端口").decode('utf-8').encode(type)
    print("已关闭自动播放").decode('utf-8').encode(type)
    print("已禁止空连接").decode('utf-8').encode(type)
except:
    print("请检查注册表权限").decode('utf-8').encode(type)
    pass


# 导入组策略
try:
    os.system(importSec)
    os.system('gpupdate/force')
    print("已设置密码策略").decode('utf-8').encode(type)
    print("已更默认管理员账户名，并禁用来宾账户").decode('utf-8').encode(type)
    print("已开启审核策略").decode('utf-8').encode(type)
except:
    pass

os.system('del 1.sdb')

print("设置完成，请重启系统").decode('utf-8').encode(type)
sleep(10)

# 获取当前系统中所有用户名
# def getUser():
#     userList = []
#     getUser = 'net user'
#     text = os.popen(getUser)
#     text1 = text.read()
#     text.close()

#     x = text1.split(' ')
#     for i in x:
#         if i != '':
#             i = i.replace('\n','')
#             i= re.compile("[A-Za-z]+").findall(i)
#             if len(i) != 0:
#                 userList.append(i[0])
#     return userList

# 删除没指定的用户名
# userlist = getUser()
# for user in userlist:
#       if 语句中指定用户名，将要排除的用户名写上就行 or user == '您要排除的用户名' 注意 如果您更改了管理员名，此处排除时应写更改后的管理员名
#     if user == 'DefaultAccount' or user == 'Administrator' or user == 'Guest' or user == 'WDAGUtilityAccount':
#         continue
#     else:
#         delUser = 'net user ' + user + ' /delete'
#         try:
#             os.system(delUser)
#         except:
#             continue


