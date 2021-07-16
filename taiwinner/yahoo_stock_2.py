# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:05:25 2021

@author: Ace
"""
'''
5.	請定義一個function，爬取以下網站：https://tw.stock.yahoo.com/rank/volume?exchange=TAI
並根據名次欄位設計成dict格式回傳
'''

import requests_html
session = requests_html.HTMLSession()

def get_rank_stock():
    url = 'https://tw.stock.yahoo.com/rank/volume?exchange=TAI'
    r = session.get(url)
    
    title_line = r.html.xpath("//div[(contains(@class, 'table-header-wrapper'))]") # 標題列
    title_line_list = title_line[0].text.split('\n') # 標題列 -> list型式
    # for each_title in title_line:
        # print(each_title.text)
    
    rows = r.html.xpath("//li[@class='List(n)']") # 每一筆數據資料
    data = {}
    for each_row in rows:
        Sub_Result = {}
        # print(each_row.text)
        # print(each_row.html.find('div'))
        each_row_list = each_row.text.split('\n') # 每一筆數據資料 -> list型式
        each_row_list[1] = each_row_list[1] + ' / ' + each_row_list[2] # 修改數據
        del each_row_list[2]
        for i in range(len(title_line_list)):
            Sub_Result.setdefault(title_line_list[i], each_row_list[i])
        del Sub_Result['名次'] # 名次要當dict.key
        # print(Sub_Result)
        data.setdefault(each_row_list[0], Sub_Result)
    # print(data)
    return data

data = get_rank_stock()
print(data)