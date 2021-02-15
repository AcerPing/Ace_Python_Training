'''
第一題: 
下載商工開放平台的公司統編csv ，選擇一類下載，
再使用Python開發爬蟲且使用Proxy進入商工平台，輸入統一編號獲取公司登記地址，
地址轉成經緯度座標(TGOS或第三方套件)，
相關數據請使用ORM存到本機的 Sqlite 資料庫。
'''

import pandas as pd
import random
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
import warnings
from bs4 import BeautifulSoup
import pymysql

#TODO:下載商工開放平台的公司統編csv ，選擇一類下載
df = pd.read_csv('202010.csv') #讀取csv檔
print(df) #顯示公司設立登記清冊(月份)
# print(df.shape[0]) #整張資料的長度(資料筆數)與寬度(欄位數量)
# print(df["統一編號"]) #抓取"統一編號"的column
row = df.shape[0] #整張資料的長度(資料筆數)
random_row = random.randint(0,row) #隨機從資料筆數中抽取一筆資料
print(df["統一編號"][random_row]) #顯示這筆資料的統一編號
tax_ID_number = df["統一編號"][random_row]

#TODO:再使用Python開發爬蟲且使用Proxy進入商工平台，輸入統一編號獲取公司登記地址
driver = Chrome("D:\Python_Summarize\Python_Training\chromedriver.exe") #開啟chrome瀏覽器
driver.get("https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do") #打開網址，前往商工平台網站(商工登記服務入口)
'''
My apologies for the log spam. 
If you aren't having issues connecting to a device with WebUSB you can ignore these warnings.
They are triggered by Chrome attempting to read properties of USB devices that are currently suspended.
'''
time.sleep(5) #等待前往搜尋結果頁面
driver.find_element_by_class_name("form-control").send_keys(str(tax_ID_number)) #尋找輸入搜尋文字的標籤，在該輸入方塊輸入統一編號號碼
driver.find_element_by_class_name("form-control").send_keys(Keys.ENTER) #按下"ENTER"鍵
time.sleep(5) #等待前往搜尋結果頁面
driver.find_element_by_class_name("moreLinkMouseOut").click() #點入詳細資料
time.sleep(5) #等待前往搜尋結果頁面

warnings.filterwarnings("ignore")
html = BeautifulSoup(driver.page_source) #抓取網頁內容，beautifulsoup4分析工具→快速解析網頁HTML碼

form = html.find("div",class_="tab-pane active") #找到公司基本資料表
form = form.find("table",class_="table table-striped") #找到公司基本資料表
columns = form.find_all("tr") #表格每一欄
for every_column in columns: #從每一欄位當中判斷是否為"公司所在地"的欄位(當中是否含有"公司所在地"的字樣)
    if "公司所在地" in every_column.text:
        address = every_column.find_all("td") 
        # print(repr(address)) #使用repr取得string中的表示
        address = address[1].text.replace("電子地圖","").replace("\n","").replace("\t","").replace("\xa0","") #第一個為公司地址
        print(address) #"公司所在地"的title
driver.close() #關閉瀏覽器

#TODO:地址轉成經緯度座標(TGOS或第三方套件)
driver = Chrome("D:\Python_Summarize\Python_Training\chromedriver.exe") #開啟chrome瀏覽器
driver.get("https://www.tgos.tw/tgos/Web/Address/TGOS_Address.aspx") #打開網址，前往TGOS查詢入口
time.sleep(5) #等待前往搜尋結果頁面
driver.find_element_by_tag_name("input").send_keys(address) #尋找輸入搜尋文字的標籤，在該輸入方塊輸入公司所在地
time.sleep(3) #等待前往搜尋結果頁面
driver.find_element_by_id("TGOS_AddressBox_QueryAddress_Execute").click()
driver.switch_to.window(driver.window_handles[1]) #selenuim分頁管理
time.sleep(10) #等待前往搜尋結果頁面
warnings.filterwarnings("ignore")
try:
    html = BeautifulSoup(driver.page_source) #抓取網頁內容，beautifulsoup4分析工具→快速解析網頁HTML碼
    form = html.find("div",style={"width: auto; height: auto; position: absolute; overflow: auto; margin: 10px; word-break: keep-all;"})
    print(form.text) #整串文字
    print(form.text[-47:-33],"\n",form.text[-33:-18]) #X坐標,Y坐標
    
    #TODO:請開啟xampp
    # 相關數據請存到本機的Sqlite資料庫
    conn=pymysql.connect(host="localhost",user="root",db="hitrust",charset="utf8",port=None)
    cur = conn.cursor()  # 取得指令操作變數
    # 執行插入方法，SQL語句
    # 格式化的作用是為了防止SQL注入，`的作用是為了防止關鍵詞被數據庫解析
    cur.execute("INSERT INTO `homework_hitrust_crawling`(`tax_ID_number`,`Address`,`Latitude&Longitude`,`Latitude`,`Longitude`) VALUES(%s,%s,%s,%s,%s)",
                                                    [int(tax_ID_number), address, form.text,form.text[-47:-33],form.text[-33:-18]])
    conn.commit()
    conn.close()
    
except:
    print("something error")
finally:
    driver.quit() #quit方法就是直接退出並關閉所有關聯的tab視窗
