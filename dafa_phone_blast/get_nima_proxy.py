import threading
import time
from bs4 import BeautifulSoup
import requests
import json
import random

url = "http://www.nimadaili.com/gaoni/{}/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}


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


def test_http(host):
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
            print("有效IP：" + host)
            with open("nima_http_list.txt", "a") as af:
                af.write(host + "\n")
        else:
            return


def main():
    """
    主函数，入口
    """
    for i in range(1, 412):
        # 延时，避免对服务器造成太大负荷，同时在延时时间内检测代理可用情况
        time.sleep(3)
        # 请求页面text
        html = requests.get(url=url.format(i), headers=get_user_agent()).text
        soup = BeautifulSoup(html, "lxml")
        # 分析元素
        tr_list = soup.select_one(".fl-table").select_one("tbody").select("tr")
        # 获取元素
        for td_list in tr_list:
            t = threading.Thread(target=test_http, args=(
                td_list.select("td")[0].text,))
            t.start()


if __name__ == "__main__":
    main()
