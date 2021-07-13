'''
第三題: 
爬取一筆公司營業地址，在財政部稅務入口網，選擇依據營業人統一編號查詢頁面會有圖片驗證碼，
使用AI學習方式或其他方式可以進入爬找資料。
'''

#TODO:軟體套用
from bs4 import BeautifulSoup #快速解析網頁HTML碼
import cv2 #驗證碼影像處理
import os
from PIL import Image #驗證碼影像處理
import pytesseract #驗證碼影像識別
import pymysql #資料庫存放
from selenium import webdriver #爬蟲
from selenium.webdriver import Chrome #爬蟲
from selenium.webdriver.chrome.options import Options #爬蟲
from selenium.webdriver.support.ui import WebDriverWait #爬蟲
from selenium.webdriver.common.keys import Keys #爬蟲
import time
import warnings
#TODO:套用Python自訂函式
import homework_HiTRUST_crawling_etax_def

url="https://www.etax.nat.gov.tw/cbes/web/CBES113W1_1" #財政部稅務入口網

# TODO: 讀取Config.txt設定檔
# 參數設定
CSV_File, csv_file_full_path = '', ''
main_path = r'D:\Python_Summarize\Python_Training\HW_HiTRUST'
f = open(os.path.join(main_path, 'Config.txt'), 'r', encoding='utf-8')
for x in f:
    if 'CSV_File=' in x:
        CSV_File = x.strip().replace('CSV_File=', '').strip()
        # 檢查檔案是否存在
        csv_file_full_path = os.path.join(main_path, CSV_File)
        if not os.path.isfile(os.path.join(main_path, CSV_File)):
            print('CSV來源檔不存在')
            raise Exception ('CSV SourceFile Error')
        print('CSV_File set to: ' + CSV_File)
        print('csv_file_full_path set to: ' + csv_file_full_path)

if CSV_File == '' or csv_file_full_path == '':
    print('CSV來源檔不存在')
    raise Exception ('CSV SourceFile Error')

#TODO:selenium爬取網站及驗證碼圖片
options = Options() #options物件，主要用途為取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行。
options.add_argument("--disable-notifications")
driver = Chrome("D:\Python_Summarize\Python_Training\chromedriver.exe",options=options) #啟動chrome瀏覽器，瀏覽器設定(chrome_options)
driver.maximize_window()  # 最大化窗口，因為每一次爬取只能看到視窗内的圖片
driver.get(url) #打開網址，前往財政部稅務入口
'''
My apologies for the log spam. 
If you aren't having issues connecting to a device with WebUSB you can ignore these warnings.
They are triggered by Chrome attempting to read properties of USB devices that are currently suspended.
'''
#方法一
wait = WebDriverWait(webdriver,5) #設定超時時間5s
elm = wait.until(lambda webdriver: driver.find_element_by_id("captchaImg"))
'''
#方法二
# time.sleep(5) #等待前往搜尋結果頁面
'''

#TODO:破解/輸入當前驗證碼，爬取的思路是用selenium擷取當前頁面，並儲存到本地
local_path = "D:\Python_Summarize\Python_Training\HW_HiTRUST\Validation Code"
Path_Screen_Shot = os.path.join(local_path , "ScreenShot.png")
driver.save_screenshot(Path_Screen_Shot) #爬取的思路是用selenium擷取當前頁面，並儲存到本地
# img = cv2.imread(Path_Screen_Shot,1) #讀取全螢幕擷取圖像
# cv2.imshow("ScreenShot",img) #顯示全螢幕擷取圖像

#TODO:僅顯示部分，擷取特定位置
#方法:利用Image(記得改成儲存為png檔的圖片)+cv2來顯示圖像
#若非png圖片，可利用OpenCV。如果想要對圖片進行裁切，就用索引的方式，將指定的區域取出即可
rangle = (955, 590, 1145, 635) 
#从图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数，各元素为（left, upper, right, lower），坐标系统的原点（0, 0）是左上角。
ScreenShot = Image.open(Path_Screen_Shot)
Path_Crop_Image = os.path.join(local_path , "Image_Crop.png")
crop_image = ScreenShot.crop(rangle) #裁切圖片
crop_image.save(Path_Crop_Image) #儲存圖片
Validation_Number_Human = cv2.imread(Path_Crop_Image,1) #讀取圖像
cv2.imshow("Validation_Number",Validation_Number_Human) #顯示驗證碼圖像

#TODO:pytesseract進行字元識別(影像辨識)
Path_Validation_Number_Machine = os.path.join(local_path , "Validation_Number_Machine.png")
threshold = 100
Validation_Number_Machine = cv2.imread(Path_Crop_Image,1) #讀取圖像
Validation_Number_Machine = cv2.cvtColor(Validation_Number_Machine,cv2.COLOR_BGR2GRAY) #色彩空間轉換，轉為灰階
_, Validation_Number_Machine = cv2.threshold(Validation_Number_Machine, threshold, 255, cv2.THRESH_BINARY) #影像二值化，超過門檻值的像素設為最大值，小於的設為0
# cv2.imshow("Validation_Number_Machine",Validation_Number_Machine) #顯示圖像
cv2.imwrite(Path_Validation_Number_Machine,Validation_Number_Machine,[cv2.IMWRITE_PNG_COMPRESSION, 9]) #PNG圖片存檔。輸出圖片檔案時，也可以調整圖片的壓縮率
Validation_Number_Machine = Image.open(Path_Validation_Number_Machine) #pytesseract進行字元識別
#方法一
# text = pytesseract.image_to_string(Validation_Number_Machine,lang='eng') #文字辨識
#方法二
text = pytesseract.image_to_string(Validation_Number_Machine).strip() #文字辨識
text = text.replace("’","").replace("‘","").replace(":","").replace("'","").replace("”","").replace("“","").replace(".","")
if text != None and text != "":
    print("影像辨識結果:",text)
elif text == None or text == "":
    print("影像辨識結果:",None,"\n抱歉機器無法辨識")
print("==================="*6)
print("0.在圖片驗證碼上先按下Enter")

cv2.waitKey() #等待按鍵繼續執行
print("1.請輸入圖片驗證碼\n"+
       "2.再按下Enter")
Validation_Number = input("請輸入圖片驗證碼:")
cv2.destroyAllWindows #關閉所有視窗

#TODO:進入爬找資料
tax_ID_number = homework_HiTRUST_crawling_etax_def.read_csv(csv_file_full_path=csv_file_full_path)
driver.find_element_by_id("vatId").send_keys(str(tax_ID_number)) #尋找輸入搜尋文字的標籤，在該輸入方塊輸入統一編號號碼
driver.find_element_by_id("captcha").send_keys(str(Validation_Number)) #尋找輸入搜尋文字的標籤，在該輸入方塊輸入統一編號號碼
driver.find_element_by_id("captcha").send_keys(Keys.ENTER) #按下"ENTER"鍵
warnings.filterwarnings("ignore")
html = BeautifulSoup(driver.page_source) #抓取網頁內容，beautifulsoup4分析工具→快速解析網頁HTML碼
try:
    #找到公司基本資料表
    business_id = html.find("td",id="businessId") 
    status = html.find("td",id="status")
    owner_name = html.find("td",id="ownerName") 
    business_name = html.find("td",id="businessName") 
    address = html.find("td",id="address") 
    capital = html.find("td",id="capital") 
    register_date = html.find("td",id="registerDate") 
    register_type = html.find("td",id="registerType")

    print("營業人統一編號：",repr(business_id.text))
    status = status.text.replace("\n","")
    print("營業狀況：",repr(status))
    print("負責人姓名：",repr(owner_name.text))
    print("營業人名稱：",repr(business_name.text))
    print("營業（稅籍）登記地址：",repr(address.text))
    print("資本額(元)：",repr(capital.text))
    print("設立日期：",repr(register_date.text))
    register_type = register_type.text.replace("\n","").replace("有關營業登記資料記載內容，因受稅務法令規章所規範及營業項目登錄欄位之限制，會與公司/商業登記不盡相同，請至主管機關經濟部之"\
    "全國商工行政服務入口網「商工登記資料公示查詢系統」查詢。","").replace("                    ","")
    print("登記營業項目：",repr(register_type))

    #TODO:請開啟xampp，存到資料庫
    conn=pymysql.connect(host="localhost",user="root",db="hitrust",charset="utf8",port=None)
    cur = conn.cursor()  # 取得指令操作變數
    # 執行插入方法，SQL語句
    # 格式化的作用是為了防止SQL注入，`的作用是為了防止關鍵詞被數據庫解析
    cur.execute("INSERT INTO `etax`(`Business Id`,`Status`,`Owner Name`,`Business Name`,`Address`,`Capital`,`Register Date`,`Register Type`) \
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                                    [int(business_id.text),status,owner_name.text,business_name.text,address.text,str(capital.text)+"元",register_date.text,register_type])
    conn.commit()
    conn.close()

except:
    print("Warning!!!\nThere could be more trouble ahead.")

finally:
    driver.quit() #quit方法就是直接退出並關閉所有關聯的tab視窗

'''
#TODO:錯誤方法，從網站『下載』驗證碼圖片
img_url = driver.find_element_by_id("captchaImg").get_attribute('src')
local_path = "D:\Python_Summarize\Python_Training\HW_HiTRUST\Validation Code"
filename = "captchaImg"
urlretrieve(img_url,os.path.join(local_path , filename+".jpeg")) #利用urlretrieve下載檔案
time.sleep(5) #等待前往搜尋結果頁面
# driver.quit()
'''

'''
#TODO:第二種辨識驗證法的方法
local_path = "D:\Python_Summarize\Python_Training\HW_HiTRUST\Validation Code"
filename = "captchaImg"
img = cv2.imread(os.path.join(local_path , filename+".jpeg"),1) #讀取homework2.png原始圖像
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshold = 160
_, IMG_Human_eyes = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow("IMG_Human_eyes",IMG_Human_eyes)
# cv2.imwrite("D:\Python_Summarize\Python_Training\HW_HiTRUST\Validation Code\captchaImg__DARK.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,100]) #將m6存檔

threshold = 91
_, img_binarized = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
# pil_img = Image.fromarray(img_binarized)
# cv2.imwrite("D:\Python_Summarize\Python_Training\HW_HiTRUST\Validation Code\captchaImg__Threshold.jpg",img_binarized,[cv2.IMWRITE_JPEG_QUALITY,100]) #將m6存檔
cv2.imshow("img 1",img_binarized)

img = Image.open("D:/Python_Summarize/Python_Training/HW_HiTRUST/Validation Code/captchaImg__Threshold.jpg")
text = pytesseract.image_to_string(img,lang='eng')
print(text)
print("===================")
'''


