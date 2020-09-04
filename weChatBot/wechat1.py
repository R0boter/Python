#!/usr/bin/env python3
import itchat
import time
import datetime
import os
from itchat.content import TEXT

roomslist = []

itchat.auto_login(hotReload=True,enableCmdQR=2)

def getroom_message(n):
    #获取群的username，对群成员进行分析需要用到
    itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    RoomList =  itchat.search_chatrooms(name=n)
    if RoomList is None:
        pass
        #print("{0} group is not found!".format(name))
    else:
       # print('取得：',RoomList[0]['UserName'])
        return RoomList[0]['UserName']

def getchatrooms():
    #获取群聊列表
    roomslist = itchat.get_chatrooms()
    #print('列表',roomslist)
    return roomslist

path_test = "./test.txt"
print("程序开始：",datetime.datetime.now())
for i in getchatrooms():
    roomslist.append(i['NickName'])

with open('群用户名.txt', 'w', encoding='utf-8')as f:
    f.write("你一共加入了{0}群".format(str(len(roomslist))))
    for n in roomslist:
        ChatRoom = itchat.update_chatroom(getroom_message(n), detailedMember=True)
        f.write('\n\n------------------------------群名称：'+ChatRoom['NickName']+"该微信群一共有{0}个成员".format(str(len(ChatRoom['MemberList'])))+'----------------------------------\n')
        with open(path_test,"w") as f1:
            f1.write(str(ChatRoom)+'\n')
        ImageFlore = "./"+str(ChatRoom['NickName'])
        os.makedirs(ImageFlore)

        print(ChatRoom['NickName'])
        for i in ChatRoom['MemberList']:
            f.write(i['NickName']+'\n')
            img = itchat.get_head_img(userName=i["UserName"])
            print(img)
            pass
#            name = i.get('NickName')
#            fileImage = open(ImageFlore+str(name)+".jpg","wb")
#            fileImage.write(img)
#            fileImage.close()

    f.close()
    print("程序结束：",datetime.datetime.now())
