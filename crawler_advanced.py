import urllib.request as req
import bs4
import warnings 
warnings.filterwarnings('ignore')  #不想看到BeautifulSoup跳出來的Warnings

def getData(url): #建立一個url函式
    #建立一個request物件，附加Request Headers資訊
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "cookie":"over18=1"})

    #讀取網頁原始碼資訊
    with req.urlopen(request) as response:
        data = response.read().decode("utf8")
    # print(data) 列印出網頁原始碼資料

    #解析原始碼，取得每篇文章的標題
    root = bs4.BeautifulSoup(data) #對整份網頁原始碼資料作分析，讓BeautifulSoup協助解析HTML格式文件
    # print(root.title.string) #列出title的文字

    '''
    titles = root.find("div",class_="title") #尋找class="title"的div標籤
    print(titles.a.string) #抓取class="title"的當中a的文字
    '''

    titles = root.find_all("div",class_="title") #尋找所有class="title"的div標籤
    # print(titles) #印出所有所有class="title"的div標籤

    for x in titles: #List的內容一個一個抓取出來
        if x.find("a") != None: #如果標題包含a標籤(沒有被刪除)，印出來
            # print(x.find("a").attrs["href"])
            print(x.find("a").string)

    #抓取上一頁的連結
    nextlink = root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的a標籤
    # print(nextlink)
    return nextlink.attrs["href"]

#主程序:抓取多個頁面的標題 (HTML)
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"

count = 0
while count<5:
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    print(pageURL)
    count+=1

