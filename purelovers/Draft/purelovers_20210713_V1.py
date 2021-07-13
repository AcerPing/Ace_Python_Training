# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:55:55 2021

@author: Ace
"""
from bs4 import BeautifulSoup
# import codecs
import os
import sys
from urllib.request import urlopen, Request, urlretrieve 
import warnings

#執行程式 #主程式
if __name__ == '__main__':
    
    #TODO: 建立資料夾
    save_dir = r'難波の店舗型ヘルス「Amour -アムール-」の女の子在籍ページです。色々な女の子をご紹介！'
    if not os.path.isdir(save_dir): os.mkdir(save_dir)
    
    #至Amour -アムール網站 
    # 風俗情報ぴゅあらば→関西→大阪府→ミナミ(難波・道頓堀)→店舗型ヘルス→Amour -アムール
    # Amour -アムール-／難波｜在籍一覧｜関西風俗情報ぴゅあらば # 難波/店舗型ヘルス
    url="https://www.purelovers.com/kansai/shop/587/girllist/" 
    
    #向網站索要資料
    request = Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
    #以urlopen開啟檔案
    with urlopen(request) as file: data = file.read().decode("utf8")
    # with codecs.open("HTML.txt","w",encoding='utf-8') as file: file.write(str(data)) 
    # print(data)
    
    #解析網頁原始碼
    warnings.filterwarnings("ignore")
    html=BeautifulSoup(data) #beautifulsoup4分析工具→快速解析網頁HTML碼    
    
    #開始逐步搜尋
    mainArea = html.find("div",id='mainArea') 
    girlListShop = mainArea.find("ul",class_='girlListShop') 
    girlList = girlListShop.find_all("li", class_='girlShopListBox') 
    
    #Question: 先定義主題，是要(封面圖片+名字)，還是要整組圖片(個別針對女優點入下載)
    
    #方法一:封面圖片+名字
    #開啟Bug檔案
    f = open("Bug.txt", "w", encoding='utf-8') # 以覆寫模式開啟檔案
    alredy_download = 0 #檢查是否全部都下載，初始值設為0
    for each_girl in girlList:
        #清除參數
        content, girl_name, img = None, None, None
        girl_name, download_img_path, data_type, save_path = "", "", "", ""
        Notes = ''
        
        try: #錯誤處理
            
            #文字
            content = each_girl.find("div",class_='girlListShop-girlDate')
            girl_name = content.find('a', class_='bold')
            if r'/kansai/shop/587/girl/' in girl_name.get('href'):pass #檢查是否為要找尋的資料 #檢查名字是否為超連結且有/kansai/shop/587/girl/
            else: 
                Notes = Notes + 'girl_name HYPERLINK Error, NO "/kansai/shop/587/girl/".'
                raise Exception('Download Error') #不是要找尋的資料 → 換下一筆 #continue
            name = girl_name.text.split(u'\xa0')[0].strip()
            age = girl_name.text.split(u'\xa0')[1].strip().replace('(','').replace(')','').strip()
            girl_name = girl_name.text.strip().replace(u'\xa0', u' ').strip() #名字 / 年齡
            
            #圖片 #取得所有圖片連結
            img = each_girl.find("table",class_='girlList-img girlList-').find('a')
            if r'/kansai/shop/587/girl/' in img.get('href'):pass #檢查是否為要找尋的資料 #檢查名字是否為超連結且有/kansai/shop/587/girl/
            else:
                Notes = Notes + 'img HYPERLINK Error, NO "/kansai/shop/587/girl/".'
                raise Exception('Download Error') #不是要找尋的資料 → 換下一筆
            img = img.find('img', style='width:90px;height:135px;object-fit:cover;',alt=name).get('src') #取得圖片網址 #alt==名字，確保圖片下載正確
            img = img.split('?')[0] #?後面為參數，代表圖片壓縮尺寸。 #需要取得原始尺寸圖片
            if (r'//contents.purelovers.com/upload/girl/' in img) or (r'//contents.purelovers.com/common/img/' in img): pass #檢查是否為要找尋的資料
            else: 
                Notes = Notes + 'img HYPERLINK Error, NO "//contents.purelovers.com/upload/girl/" or "//contents.purelovers.com/common/img/".'
                raise Exception('Download Error') #不是要找尋的資料 → 換下一筆
            #取得檔案類型
            download_img_path = "https:"  + img.strip()
            data_type = '.' + img.split('.')[-1].strip()
            save_path = os.path.join(save_dir, (girl_name + data_type))
            #檢查檔案是否存在
            if os.path.exists(save_path): os.remove(save_path) #若檔案已存在則刪除
            urlretrieve(download_img_path, save_path) #利用urlretrieve下載檔案
            print(girl_name)
            alredy_download += 1 #檢查是否全部都下載，每下載一次就+1
            print(alredy_download)

            if r'//contents.purelovers.com/common/img/' in img:
                Notes = Notes + 'No IMG. "//contents.purelovers.com/common/img/". No "//contents.purelovers.com/upload/girl/".'
                raise Exception('Download Error') #不是要找尋的資料 → 換下一筆

        except KeyboardInterrupt:
            sys.exit(1)

        except:
            if (content != None) and (girl_name != None) and (str(girl_name).strip() != ""):
                #記錄錯誤
                f.write("資料錯誤，無法下載\n")
                f.write(str(alredy_download).strip()+ '. ' + str(girl_name).strip() + "\n") # 寫入資料
                f.write('Notes: ' + str(Notes).strip() + "\r\n") # 寫入資料
            continue
    
    f.close()# 關閉檔案
    if not len(girlList) == alredy_download: raise Exception('Download Error')