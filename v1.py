# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:04:52 2020

@author: Jitendra Nirmal
"""

import PyPDF2
import re
 
pdfFileObj=open(r's_r1.pdf',mode='rb')
searchwords=['Skills- ', '09']
 
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
number_of_pages=pdfReader.numPages
 
pages_text=[]
words_start_pos={}
words={}
 
with pdfFileObj as f1, open('keywords.txt') as f2:
    st = set(map(str.rstrip, pages_text))
    for word in f1:
        for page in range(number_of_pages):
            pages_text.append(pdfReader.getPage(page).extractText())
            #print(pages_text)
        for line in f1:
            if any(word in st for word in  line.split()):
                print(line)