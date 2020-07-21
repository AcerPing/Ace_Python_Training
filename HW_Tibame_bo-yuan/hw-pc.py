import os
import requests
import json
import codecs
import prettytable

#TODO(1.)請使用者輸入搜尋關鍵字
search = input("關鍵字:")
page="1" #一律從第一頁開始搜尋

#TODO(2-1.)若沒有輸入關鍵字，則清除畫面、跳出
if len(search) == 0: 
    os.system("cls")
    print("未輸入關鍵字")

#TODO(2-2.)當使用者有輸入搜尋關鍵字時，則進入迴圈
elif len(search) > 0:
    while True:
        
        #PChome商品搜尋頁面
        url="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q="+search+"&page="+page+"&sort=sale/dc"
        # print(url)
        

        #TODO(3.)使用requests取得url網頁資訊
        r = requests.get(url,headers={
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Cookie":"U=8c061c3e9552e22380fa925017b455d1d6f026cd; ECC=d2dc9092652f711fe874e184b7683978cf63e1c9.1594091992; ECWEBSESS=6e3208257a.d92bee036ef847acbc0a253703136c962588d608.1594091991; venguid=6b19e204-0192-481a-886e-36e4d92ef295.wg1-1n4020200707; _gcl_au=1.1.174542224.1594091993; vensession=2b222542-93bb-4821-b739-c35e0ce08bae.wg1-36wz20200707.se; _ga=GA1.3.1551641598.1594091994; _ga_9CE1X6J1FG=GS1.1.1594091993.1.1.1594092180.0; _gid=GA1.3.1152039405.1594091994; _fbp=fb.2.1594091994169.1655221813; _gat_UA-115564493-1=1",
            "Host":"ecshweb.pchome.com.tw",
            "TE":"Trailers",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"}) #讀取指定網址
        r.encoding="utf8" #讀取和設定編碼
        # print(r.text) #顯示<Response [200]→Successful

        # TODO(4)使用json分析
        try:
            js = json.loads(r.text)
            # with codecs.open("pchome.txt","w",encoding="utf8") as file:
            #     file.write(str(js))
            # print(js) #字典形式
            # print(js["prods"]) #字典形式→用js["prods"]去抓取"prods"的值(values)→串列形式(list)
            form = prettytable.PrettyTable(["名稱","價格"],encoding="utf8") #建立一個 PrettyTable表格
            form.align["名稱"]="l" #設定欄位的對其方式
            form.align["價格"]="l" #設定欄位的對其方式
            for d in js["prods"]: #串列形式(list)→用迴圈抓取每一筆資料(字典形式)
                # print(d)
                # print(d["name"]) #字典形式→抓取values的值
                # print(d['price']) #字典形式→抓取values的值
                form.add_row([d["name"],d['price']]) #新增表格的一個列
            print(form) #把表格顯示出來
            print() #排版
            print("="*110) #排版

            page=input("前往頁碼：")
            os.system("cls") #清除畫面
        
        except:
            os.system("cls") #清除畫面
            print("『頁碼超過範圍！』 或 『不是json格式檔』")
            break
