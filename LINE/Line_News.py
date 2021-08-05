# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:49:12 2021

@author: Ace
"""
'''
請現場設計爬蟲爬取LINE新聞，取得標題、來源、時間、網址，並說明設計思路 
'''

from bs4 import BeautifulSoup
import codecs
import os
import sys
from urllib.request import urlopen, Request, urlretrieve 
import warnings
import datetime
import xlwt
import xlrd
import traceback
import time
import shutil

# url = r'https://today.line.me/tw/v2/tab/top?gclsrc=aw.ds&gclid=CjwKCAjw9aiIBhA1EiwAJ_GTSvb0h8aJx7jEZfWamojBiWIHEFReWu4tXWCylS2Fyph8R4X-nYuAkBoCLtAQAvD_BwE'
# url = r'https://today.line.me/tw/'
url = r'https://today.line.me/tw/v2/tab'
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
# news_area = html.find("div",class_='main-wrap main-wrap')
# news_area_list = news_area.find_all("a",class_='articleCard articleCard--horizontal')
news_area_list = html.find_all("a",class_='articleCard articleCard--horizontal')
for each_news in news_area_list :
    title = each_news.find('span',class_='articleCard-title text text--d text--primary text--medium text--ellipsis2')
    print('title', title.text)
    source = each_news.find('span',class_='articleCard-description text text--f text--primary text--regular text--ellipsis1')
    print('source', source.text)
    # print(each_news.get('href'))
    link = r'https://today.line.me' + each_news.get('href')
    print('linkage', link)
    request = Request(link,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
    #以urlopen開啟檔案
    with urlopen(request) as file: data = file.read().decode("utf8")
    #解析網頁原始碼
    warnings.filterwarnings("ignore")
    html_2=BeautifulSoup(data) #beautifulsoup4分析工具→快速解析網頁HTML碼   
    str_time = html_2.find('span',class_='entityPublishInfo-meta-info text text--f text--secondary text--regular').text
    print('時間', str_time)

#######################################################################################################################################################################################################
#######################################################################################################################################################################################################

# url = r'https://today.line.me/tw/v2/tab'
# #向網站索要資料
# request = Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
# #以urlopen開啟檔案
# with urlopen(request) as file: data = file.read().decode("utf8")

# # with codecs.open("HTML.txt","w",encoding='utf-8') as file: file.write(str(data)) 
# # print(data)

# #解析網頁原始碼
# warnings.filterwarnings("ignore")
# html=BeautifulSoup(data) #beautifulsoup4分析工具→快速解析網頁HTML碼    
# # VideoNews_area_list = news_area.find_all("div",class_='glnSwiperWrapper carousel swiper-container swiper-container-initialized swiper-container-horizontal swiper-container-free-mode')
# VideoNews_area_list = html.find_all("div",class_='swiper-slide swiper-slide-active')
# for each_news in VideoNews_area_list :
#     title = each_news.find('span',class_='articleCard-title text text--d text--primary text--medium text--ellipsis2')
#     print('title', title.text)
#     source = each_news.find('span',class_='articleCard-description text text--f text--primary text--regular text--ellipsis1')
#     print('source', source.text)
#     # print(each_news.get('href'))
#     link = r'https://today.line.me' + each_news.get('href')
#     print('linkage', link)
#     request = Request(link,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
#     #以urlopen開啟檔案
#     with urlopen(request) as file: data = file.read().decode("utf8")
#     #解析網頁原始碼
#     warnings.filterwarnings("ignore")
#     html_2=BeautifulSoup(data) #beautifulsoup4分析工具→快速解析網頁HTML碼   
#     str_time = html_2.find('span',class_='entityPublishInfo-meta-info text text--f text--secondary text--regular').text
#     print('時間', str_time)