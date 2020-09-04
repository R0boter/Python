import telepot
import socket

bot = telepot.Bot('1014394657:AAEK_5KAszaSAUiMthAIJRWt-EsTiEk1MXk')

chatDict = {
        'yzqp':'-1001424605052',
        '650qp':'-1001261525740',
        'sswc':'-1001261525740'
        }
HostDict = {
        'yzqp':['yzll.in','yaqp.in','yzqp.co'],
        '650qp':['88pk.in','88qp.in','650qp.app','i650.cc'],
        'sswc':['98qp.in','98pk.in']
        }

gameHostList = ['88qp.in','88pk.in','98qp.in','98pk.in']                                         # 接口和游戏域名
offcialHostList = ['yzqp.co','650qp.app']                                                        # 官网域名
adminHostList = ['i650.cc']                                                                      # 管理后台域名

interfacePortList = [8600,9562,9563,9777]                                                        # 接口和登录服端口
adminPortList = [9560,9666]                                                                      # 后台管理和代理管理端口
offcialPort = [80]

def host(ip,port,hostdict,chatdict):
    for host in hostdict:
        if ip in hostdict[host]:
            bot.sendMessage(chatdict[host],host+"的"+ip+":"+str(port)+"端口无法连通,请立即检查")

def connectTest(ip,port,hostdict,chatdict):                                                      # 测试连通性
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(10)
    c = s.connect_ex((ip,port))
    if c == 0 :
        print(ip,port,c)
    else:
        host(ip,port,hostdict,chatdict)
        print(ip,port,c)
    s.close()

def connect(hostlist,portlist,hostdict,chatdict):
    for ip in hostlist:
        for port in portlist:
            connectTest(ip,port,hostdict,chatdict)


if __name__ == '__main__':
    connect(gameHostList,range(7500,7601),HostDict,chatDict)                                     # 游戏端口测试
    connect(gameHostList,interfacePortList,HostDict,chatDict)                                    # 接口和登陆服务器端口测试
    connect(offcialHostList,offcialPort,HostDict,chatDict)                                       # 官网端口测试
    connect(adminHostList,adminPortList,HostDict,chatDict)                                       # 后台管理和代理管理端口测试














