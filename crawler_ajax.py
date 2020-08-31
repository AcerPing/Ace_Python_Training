import urllib.request as req
import bs4
import warnings 

#TODO:抓取Medium.com的文章資料
url="https://medium.com/_/api/home-feed"

#TODO:建立一個request物件，附加Request Headers資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})

#TODO:讀取網頁原始碼資訊
with req.urlopen(request) as response:
    data = response.read().decode("utf8") #根據觀察，取得的資料是JSON格式

#TODO:解析JSON格式的資料，取得每篇文章的標題
import json
data = data.replace("])}while(1);</x>","")
data = json.loads(data) #把原始的JSON資料解析成字典/列表的表示形式
# print(data)

#TODO:取得JSON資料中的文章標題
posts = data["payload"]["references"]["Post"]
# print(posts)
for key in posts:
    post = posts[key]
    print(post["title"])