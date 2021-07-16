# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:17:53 2021

@author: Ace
"""
'''
3.	請定義一個function名為append_to_list，功能說明如下：
傳入參數為n, list, 當list沒提供的時候自動用空陣列作為default
此function功能為 將n附加到list最後傳出
'''
def append_to_list(n,lst=[]):
    lst.append(n)
    return lst


lst = append_to_list(n=1)
print(lst)    

lst = append_to_list(n=1, lst=[1,2])
print(lst)   