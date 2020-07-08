# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:33:27 2019

@author: Jitendra Nirmal
"""

import PyPDF2
import re
import statistics
from nltk.tokenize import sent_tokenize,word_tokenize
ResSearch=[]
l=[]
l1=[]
object1 = open('Siddhesh_Shinde.pdf','rb')
reader = PyPDF2.PdfFileReader(object1)
n_of_pages = reader.numPages
print(reader.numPages)
resume_text=""
page=0
for i in range(0,n_of_pages):
    page=reader.getPage(i)
    resume_text+=page.extractText()

'''page=reader.getPage(1)
text1=page.extractText()
l.append(re.findall('Python\b \-\ {2}', text1))
l.append(re.findall('Java', text1))
l.append(re.findall('PHP', text1))
print(l)
print("Bhavin_Sayali Resume")
object2 = open('s_r1.pdf','rb')
reader2 = PyPDF2.PdfFileReader(object2)
print(reader.numPages)
page1=reader2.getPage(1)
text2=page1.extractText()
#print(text2)
l1.append(re.findall('Python', text2))
l1.append(re.findall('Java', text2))
l1.append(re.findall('PHP', text2))
ratings=[]
ratings.append(re.findall("/[A-Z]*[a-z]\b - \d{2}/gi",text2))'''
text1=resume_text
l2=[]
skills=[]
ratings=[]
backlogs=[]
cgpa=[]
experience=[]
l2=word_tokenize(text1)
# BACKLOGS
for i in range(0,len(l2)):
    if(i==len(l2)-3):
        break
    b1=l2[i]
    b3=l2[i+2]
    if(b1=='Backlogs' and b3.isdigit()):
        print(b1,b3)
        backlogs.append(int(b3))
#EXPERIENCE
for i in range(0,len(l2)):
    if(i==len(l2)-3):
        break
    e1=l2[i]
    print(e1)
    e2=l2[i+1]
    
    if(e1.isdigit() and e2=='year' or e2=='years'):
        print(e1,e2)
        experience.append(int(e1))
    elif(e1.isdigit() and e2=='month' or e2=='months'):
        temp=int(e1)
        e1=float(temp/12)
        experience.append(e1)
        
#CGPA
for i in range(0,len(l2)):
    if(i==len(l2)-3):
        break
    b1=l2[i]
    b3=l2[i+2]
    if(b1=='CGPA' or b1=="cgpa" and b3.isdigit()):
        print(b1,b3)
        cgpa.append(float(b3))
#SKILLS AND RATINGS
for i in range(0,len(l2)):
    if(i==len(l2)-3):
        break
    else:
        t1=l2[i]
        t2=l2[i+1]
        t3=l2[i+2]
        if(t1.isalpha() and t2=='-' and t3.isdigit() and len(t3)==2):
            print(t1,t2,t3)
            skills.append(t1)
            ratings.append(int(t3))
        else:
            t1=""
            t2=""
            t3=""
            continue
pred=[]
print("TECHNICAL - ")
temp1=statistics.mean(ratings)
print(statistics.mean(ratings))
pred.append()
print("CGPA - ")
print(cgpa)
print("SKILLS - ")  
print(skills)
print("RATINGS - ")
print(ratings)
sum1=sum(ratings)/len(ratings)
print("PROJECT - ")
print(round(sum1))
print("EXPERIENCE - ")
print(sum(experience))

#print(l2)
#print(page.extractText())
