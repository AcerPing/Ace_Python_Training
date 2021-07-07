# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 20:39:44 2021

@author: Ace
"""
# Create PDF from a list of images
# https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

from fpdf import FPDF
pdf = FPDF()
imagelist = [r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\GOPR1707.JPG',
             r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\GOPR1708.JPG',
             r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\GOPR1709.JPG',
             r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\GOPR1712.JPG',
             r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\GOPR1713.JPG',
             r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\GOPR1714.JPG',
             r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo\Word_to_PDF\GOPR1710.JPG']
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(image,0,0,210,297)
pdf.output("yourfile.pdf", "F")
