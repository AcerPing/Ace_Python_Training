# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:40:03 2021

@author: Ace
"""

import os
import pandas as pd
import random
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
from bs4 import BeautifulSoup
import pymysql

url = r'https://today.line.me/tw/v2/tab'

driver.get(url) #打開網址，前往商工平台網站(商工登記服務入口)
'''
My apologies for the log spam. 
If you aren't having issues connecting to a device with WebUSB you can ignore these warnings.
They are triggered by Chrome attempting to read properties of USB devices that are currently suspended.
'''
driver.implicitly_wait(5) #等待前往搜尋結果頁面
driver.find_element_by_class_name("form-control").send_keys(str(tax_ID_number)) #尋找輸入搜尋文字的標籤，在該輸入方塊輸入統一編號號碼
driver.find_element_by_class_name("form-control").send_keys(Keys.ENTER) #按下"ENTER"鍵
time.sleep(2*test_time) #等待前往搜尋結果頁面
driver.find_element_by_class_name("moreLinkMouseOut").click() #點入詳細資料
driver.implicitly_wait(5) #等待前往搜尋結果頁面

warnings.filterwarnings("ignore")
html = BeautifulSoup(driver.page_source) #抓取網頁內容，beautifulsoup4分析工具→快速解析網頁HTML碼
