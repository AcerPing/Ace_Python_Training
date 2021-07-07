# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 20:17:24 2021

@author: Ace
"""

# Extract a page from a pdf as a jpeg
# https://stackoverflow.com/questions/46184239/extract-a-page-from-a-pdf-as-a-jpeg

import fitz

pdffile = "infile.pdf"
doc = fitz.open(pdffile)
page = doc.loadPage(0)  # number of page
pix = page.getPixmap()
output = "outfile.png"
pix.writePNG(output)
