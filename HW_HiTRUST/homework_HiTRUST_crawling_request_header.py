'''
第二題: 
使用自己電腦訪問自己開發的網頁，
可顯示當前電腦設備軟硬體、系統、瀏覽器、IP..等資訊(可利用HTML、DOM、BOM…)。
'''

import os
from selenium.webdriver import Chrome
import time
import webbrowser 

'''
#TODO:首先執行自己開發的Flask網頁，建議直接在終端機操作
os.system('D:\Python_Summarize\Python_Training/flask_project/app.py')
'''

#TODO:使用自己電腦訪問自己開發的網頁
#TODO:方法一
driver = Chrome("D:\Python_Summarize\Python_Training\chromedriver.exe") #開啟chrome瀏覽器
driver.get("http://127.0.0.1:3000/") #訪問自己開發的網頁
time.sleep(5) #等待前往搜尋結果頁面
driver.quit() #quit方法就是直接退出並關閉所有關聯的tab視窗

'''
#TODO:使用自己電腦訪問自己開發的網頁
#TODO:方法二
# There is no webbrowser.close
webbrowser.open("http://127.0.0.1:3000/") 
time.sleep(10)
# use these codes to close the task(in Windows OS) /  use system function to kill the task
os.system("taskkill /im chrome.exe /f")
'''
