# from urllib import request
import requests
import os
import json
import pafy
from time import sleep


class YoutubeVideoDownload():
    def __init__(self,url):
        self.download_url == url

    def runDownload(self,save_path):
        self.save_path = save_path
        video = pafy.new(self.download_url)
        v_best =video.getbest()
        v_best.download(self.save_path)

def get_url():
    urlList=[]
    path = r"./urllist.txt"
    with open(path,"r",encoding="utf-8") as f1:
        urls = f1.readlines()
    for i in urls:
        i = i.rstrip("\n")
        urlList.append(i)

    return urlList

def downloadPlayerList(channelId):
    list_url="https://www.googleapis.com/youtube/v3/playlists?part=id&maxResults=50&channelId="+channelId+"&key=AIzaSyDi16FjCv6GdCH4YPPxxYki3PqUjgiBpD4"
    playerList = []
    res = requests.get(list_url,timeout=10)
    dict1 = json.loads(res.text)
    for j in dict1['items']:
        playerList.append(j['id'])
    return playerList

def downloadVideoList(playerList):
    videoList = []
    for i in playerList:
        video_url="https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId="+i+"&key=AIzaSyDi16FjCv6GdCH4YPPxxYki3PqUjgiBpD4"

        res = requests.get(video_url)
        dict1 = json.loads(res.text)
        for j in dict1['items']:
            videoList.append(j['contentDetails']['videoId'])
    return videoList

def downloadChannelDescrip(channelId):
    channel_url = "https://www.googleapis.com/youtube/v3/channels?part=snippet&id="+channelId+"&key=AIzaSyDi16FjCv6GdCH4YPPxxYki3PqUjgiBpD4"
    res = requests.get(channel_url)
    dict1 = json.loads(res.text)
    name = dict1['items'][0]['snippet']['title']
    descript = dict1['items'][0]['snippet']['description']
    path = os.path.join("./data",name)
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    descriptFile = os.path.join(path,'descript.txt')
    with open(descriptFile,'w',encoding='utf-8') as f:
        f.write(name+'\n')
        f.write(descript)
    num = 0
    for i in dict1['items'][0]['snippet']['thumbnails']:
        url1 = dict1['items'][0]['snippet']['thumbnails'][i]['url']
        sleep(1)
        r = requests.get(url1)
        filename = str(num)+name+".jpg"
        filesname = os.path.join(path,filename)
        with open(filesname,'wb') as f1:
            f1.write(r.content)
        num += 1
    return path


def downloadThumbnailList(videoId,num,path):
    thumbnail_url="https://www.googleapis.com/youtube/v3/videos?part=snippet&id="+videoId+"&key=AIzaSyDi16FjCv6GdCH4YPPxxYki3PqUjgiBpD4"
    res = requests.get(thumbnail_url)
    dict1 = json.loads(res.text)
    descript = dict1['items'][0]['snippet']['description']
    paths = os.path.join(path,str(num))
    if os.path.exists(paths):
        pass
    else:
        os.mkdir(paths)
    descriptFile = os.path.join(paths,'descript.txt')
    with open(descriptFile,'w',encoding='utf-8') as f1:
        f1.write(descript+'\n')
    for i in dict1['items'][0]['snippet']['thumbnails']:
        url = dict1['items'][0]['snippet']['thumbnails'][i]['url']
        r = requests.get(url)
        filename = os.path.join(paths,os.path.basename(url))
        with open(filename,'wb') as f:
            f.write(r.content)
    return paths

if __name__ == "__main__":
    urls = get_url()
    for url in urls:
        playerList = downloadPlayerList(url)
        videoList = downloadVideoList(playerList)
        path = downloadChannelDescrip(url)
        num = 0
        for i in videoList:
            try:
                paths = downloadThumbnailList(i,num,path)
                youtube = YoutubeVideoDownload(i)
                youtube.runDownload(paths)
                num += 1
            except Exception as e:
                num += 1
                pass
            continue
