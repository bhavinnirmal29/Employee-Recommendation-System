# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:47:06 2019

@author: Jitendra Nirmal
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:33:27 2019

@author: Jitendra Nirmal
"""
import PyPDF2 
import re
  
# creating a pdf file object 
pdfFileObj = open('resume.pdf','rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
n=pdfReader.getNumPages() 
# printing number of pages in pdf file 
print(n) 
String1 = "C,C++,JAVA"
# rotating each page 
# extract text and do the search
for i in range(0, n):
    PageObj = pdfReader.getPage(i)
    print("this is page ", str(i)) 
    Text1 = PageObj.extractText() 
    # print(Text)
    ResSearch = re.search(String1, Text1)
    print(ResSearch)
# extracting text from page 
print(pdfFileObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close() 