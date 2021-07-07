# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:24:39 2021

@author: Ace
"""

import sys
import os
import comtypes.client
import win32com.client

# .doc to pdf using python
# https://stackoverflow.com/questions/6011115/doc-to-pdf-using-python
wdFormatPDF = 17

# in_file = os.path.abspath(sys.argv[1])
in_file = os.path.abspath(r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\履歷範本.doc')
in_file = r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\履歷範本.docx'

# out_file = os.path.abspath(r'‪D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\履歷範本.pdf')
out_file = r'‪D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\履歷範本_2.pdf'.replace('\u202a','')

# https://blog.csdn.net/zw05011/article/details/90769461
# word = comtypes.client.CreateObject('Word.Application')
word = win32com.client.Dispatch('Word.Application')
# win32com.client.DispatchEx('Word.Application') # DispatchEx会使用独立进程。
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()


'''
from docx2pdf import convert
import win32api
# from win32api import pywintypes
import win32
# from win32 import pywintypes
# import win32.pywintypes
import pywintypes
convert(in_file, r'‪D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\履歷範本.pdf'.replace('\u202a',''))

# ModuleNotFoundError: No module named '_win32sysloader'
# https://blog.csdn.net/weixin_55643951/article/details/115162327

# ImportError: No system module 'pywintypes' (pywintypes27.dll)
# https://blog.csdn.net/u011478909/article/details/50670348

'''