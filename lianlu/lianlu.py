#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

for j in range(1,19):
    url = "https://www.linksfin.com/eco/vc/0/"+str(j)
    html =urlopen(url).read().decode('utf-8')
#    url1 = "https://www.linksfin.com/"
    path = r"./count.txt"
    soup = BeautifulSoup(html)
    list1 = soup.find_all('a',class_="z wrap")
    for i in list1:
        i = str(i)
        url1 = "https://www.linksfin.com/"+re.findall(r"vc/[\-0-9a-zA-Z]*",i)[0]
#        url2 = re.findall(r"vc/[0-9a-zA-Z]*",i)
#        url3 = url1 + url2[0]
        html1 = urlopen(url1).read()
        soup1 = BeautifulSoup(html1)
        if soup1.find('div',class_="company_header"):
            list2 = soup1.find('div',class_="company_header")

            name = list2.find('h1').string

            if len(list2.find_all('em')) > 1: 
                email = list2.find_all('em')[1].string
            elif len(list2.find_all('em')) == 1:
                email = list2.find_all('em')[0].string
            else:
                email = "未找到"

            if list2.find('a'):
                www = list2.find('a').string
            else:
                pass

            with open(path, "a", encoding = "utf-8") as f1:
                f1.write(str(name)+'\n')
                f1.write('email：'+str(email)+'\n')
                f1.write('url：'+str(www)+'\n')
        else:
            continue
