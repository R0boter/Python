import requests
import random
import time
from bs4 import BeautifulSoup
from time import sleep

base_url = "https://www.jihaoba.com"

prefix_list = [
    "139",
    "138",
    "137",
    "136",
    "134",
    "135",
    "147",
    "150",
    "151",
    "152",
    "157",
    "158",
    "159",
    "172",
    "178",
    "182",
    "183",
    "184",
    "187",
    "188",
    "195",
    "197",
    "198",
    "130",
    "131",
    "132",
    "140",
    "145",
    "146",
    "155",
    "156",
    "166",
    "185",
    "186",
    "175",
    "176",
    "196",
    "133",
    "149",
    "153",
    "177",
    "173",
    "180",
    "181",
    "189",
    "191",
    "193",
    "199"
]


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


def get_res(url):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    res = requests.get(url=url, headers=get_user_agent(), timeout=10).text
    return res


for prefix in prefix_list:
    local_list = []
    hd_url = base_url + "/haoduan/" + str(prefix) + "/"
    while True:
        try:
            hd_res = get_res(hd_url)
            break
        except:
            sleep(5)

    hd_soup = BeautifulSoup(hd_res, "lxml")
    del (hd_res)
    haoduan = hd_soup.select_one(
        ".haoduan-hd").select_one(".hd_result1").select("a")
    for link in haoduan:
        local_list.append(link.get("href"))
    for local in local_list:
        local_url = base_url + local
        while True:
            try:
                local_res = get_res(local_url)
                break
            except:
                sleep(5)
        local_soup = BeautifulSoup(local_res, "lxml")
        del (local_res)
        for num in local_soup.select(".hd-city01"):
            try:
                pre = str(num.select_one("a").text)
                with open(prefix + ".txt", "a", encoding="utf-8") as f:
                    f.write(pre+"\n")
            except:
                pass
        sleep(3)
