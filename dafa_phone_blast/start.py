import requests
import json
import time
from multiprocessing import Process, Queue as pro_queue
import threading
import sys
import random
import hashlib
from queue import Queue as thr_queue
from bs4 import BeautifulSoup

proxy_list = ["191.238.210.157:3128",
              "78.142.232.116:80",
              "103.154.190.6:8080",
              "121.232.148.195:9000",
              "123.169.100.69:9999",
              "118.212.107.3:9999",
              "13.57.194.187:8080",
              "171.35.143.126:9999",
              "112.111.217.241:9999",
              "115.221.247.107:9999",
              "110.243.12.166:9999",
              "113.194.29.253:9999",
              "115.221.246.44:9999",
              "213.230.121.115:3128",
              "115.221.240.35:9999",
              "175.43.57.61:9999",
              "118.212.106.125:9999",
              "158.227.106.21:80",
              "110.243.30.163:9999",
              "171.35.143.126:9999",
              "110.243.18.247:9999",
              "194.135.75.74:55716",
              "94.73.239.124:55443",
              "142.93.248.118:3128",
              "106.7.40.11:9000",
              "123.169.127.206:9999",
              "103.62.232.26:8080",
              "123.169.127.206:9999",
              "122.5.109.191:9999",
              "201.142.225.244:8080",
              "182.34.32.186:9999",
              "182.34.17.250:9999",
              "81.93.73.28:8081",
              "115.221.247.226:9999",
              "77.77.215.6:8080",
              "158.46.127.222:52574",
              "113.121.21.188:9999",
              "183.166.132.124:9999",
              "110.243.4.82:9999",
              "139.162.1.237:80",
              "115.218.6.170:9000",
              "192.117.146.110:80",
              "121.232.199.130:9000",
              "121.226.188.130:9999",
              "36.250.156.168:9999",
              "115.221.247.226:9999",
              "95.179.163.197:3128",
              "103.1.93.184:55443",
              "113.121.21.188:9999",
              "159.224.166.129:38779"]


class test_phone(threading.Thread):
    def __init__(self, thread_queue, total, name):
        threading.Thread.__init__(self)
        self._queue = thread_queue
        self._total = total
        self._name = name

    def check_phone(self, phone):
        proxy = random.choice(proxy_list)
        randomId = str(int(time.time()))
        strAccounts = str(phone)
        strMachineID = str(hashlib.md5(
            strAccounts.encode(encoding='utf-8')))

        loginSign_str = "cbDeviceType=17&cbGender=1&dwGameID=0&dwSource=100000&dwSpreaderGameID=0&projectSign=dafa&randomId=" + \
            str(randomId)+"&strAccounts="+strAccounts+"&strLogonPass=E10ADC3949BA59ABBE56E057F20F883E&strMachineID=" + \
            strMachineID+"&strMobilePhone=656454&strNickName=&wFaceID=176b3830298a2bec65e2a3428a528f767"

        m = hashlib.md5(loginSign_str.encode(encoding='utf-8'))

        data = {"randomId": randomId, "dwGameID": 0, "cbDeviceType": 17, "strNickName": "", "dwSource": 100000, "projectSign": "dafa",
                "strLogonPass": "E10ADC3949BA59ABBE56E057F20F883E", "strAccounts": strAccounts,
                "strMachineID": strMachineID, "strMobilePhone": 656454, "dwSpreaderGameID": 0, "cbGender": 1, "wFaceID": 1}

        data['loginSign'] = m.hexdigest().upper()
        try:
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            res = requests.post(url="http://a-dafa.wanli6847.com:9898/api/applogin/exclude/registerAccounts",
                                headers=get_user_agent(), proxies={"http": "http://" + proxy}, json=data, timeout=5)
            res.close()
            dic = json.loads(res.text)
            del (res)

            if("此帐号已被注册，请换另一帐号尝试再次注册！" == dic['msg']):
                with open("result.txt", "a+", encoding="utf-8") as f:
                    f.write(str(phone) + "\n")
        except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ProxyError, requests.exceptions.ReadTimeout, json.JSONDecodeError):
            try:
                proxy_list.remove(proxy)
            except Exception:
                pass
            self.check_phone(phone)
            print("正在切换代理")
        except Exception as e:
            with open("error.txt", "a+", encoding="utf-8") as f:
                f.write(str(e) + " ---> " + str(phone) + "\n")
            with open("re.txt", "a+", encoding="utf-8") as f:
                f.write(str(phone) + "\n")
            pass

    def run(self):
        while not self._queue.empty():
            phonenum = self._queue.get()
            self.check_phone(phonenum)


def get_user_agent():
    """
    User Agent的细节处理
    :return:
    """
    user_agent_list = [
        {'User-Agent': 'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; en) Opera 11.00',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.1.15) Gecko/20101027 Fedora/3.5.15-1.fc12 Firefox/3.5.15',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.551.0 Safari/534.10',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008092809 Gentoo Firefox/3.0.2',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.544.0',
            'Connection': 'close'},
        {'User-Agent': 'Opera/9.10 (Windows NT 5.2; U; en)',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko)',
            'Connection': 'close'},
        {'User-Agent': 'Opera/9.80 (X11; U; Linux i686; en-US; rv:1.9.2.3) Presto/2.2.15 Version/10.10',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9b3) Gecko/2008020514 Firefox/3.0b3',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; fr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.60',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4',
            'Connection': 'close'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51',
            'Connection': 'close'}
    ]
    return random.choice(user_agent_list)


def test_proxy(host):
    """
    检测http代理IP是否有效并将有效IP写入文件
    """
    ip = {}
    ip["http"] = "http://" + host
    # 通过访问下面这个ip检测网站来判断
    url = "http://ip.tool.chinaz.com/"

    # http无效的情况大致有两种 1.无法访问这个网页，那么这个代理不可用 2.能访问网页但是没有达到代理效果，即仍然使用的自己的ip访问网页
    try:
        requests.adapters.DEFAULT_RETRIES = 3
        html = requests.get(url=url, headers=get_user_agent(),
                            proxies=ip, timeout=5).text
    except:
        return
    else:
        soup = BeautifulSoup(html, "lxml")

        try:
            real_ip = soup.select_one(".fz24").text
        except:
            return
        if real_ip == host.split(":")[0]:
            if host not in proxy_list:
                proxy_list.append(host)
        else:
            return


def craw_proxy(url, num):
    try:
        # 请求页面text
        html = requests.get(url=url.format(
            num), headers=get_user_agent()).text
        soup = BeautifulSoup(html, "lxml")
        # 分析元素
        tr_list = soup.select_one(".fl-table").select_one("tbody").select("tr")
        # 获取元素

        for td_list in tr_list:
            t = threading.Thread(target=test_proxy, args=(
                td_list.select("td")[0].text,))
            t.start()
    except Exception:
        craw_proxy(url, num)


def get_proxy():
    url = "http://www.xiladaili.com/gaoni/{}/"

    while True:
        for num in range(1, 50):
            # 延时，避免对服务器造成太大负荷，同时在延时时间内检测代理可用情况
            time.sleep(3)
            craw_proxy(url, num)
        time.sleep(100)


def creat_thread(proce_queue):
    while not proce_queue.empty():
        prefix = proce_queue.get()
        thread_queue = thr_queue()
        for stuffx in range(0, 10000):
            stuffx = (4 - len(str(stuffx))) * "0" + str(stuffx)
            phonenum = str(prefix) + str(stuffx)
            thread_queue.put(phonenum)
        total = thread_queue.qsize()
        threads = []
        thread_count = int(10)

        for i in range(thread_count):
            threads.append(test_phone(thread_queue, total, prefix))
        for thread in threads:
            thread.setDaemon(True)
            thread.start()
        for thread in threads:
            thread.join()
        print(prefix + " is done\n")


if __name__ == '__main__':
    process_queue = pro_queue()
    for mid in range(0, 10000):
        mid = (4 - len(str(mid))) * "0" + str(mid)
        prefix = str(157) + str(mid)
        process_queue.put(prefix)
    gp = Process(target=get_proxy)
    gp.start()
    process_list = []
    process_count = int(10)
    for i in range(process_count):
        process_list.append(
            Process(target=creat_thread, args=(process_queue,)))
    for proce in process_list:
        proce.start()
    gp.join()
    for proce in process_list:
        proce.join()
