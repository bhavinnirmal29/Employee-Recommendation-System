# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:06:17 2019

@author: Sayali
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:09:57 2019

@author: Sayali
"""
import re
import nltk
from nltk.corpus import stopwords
import PyPDF2
import os


#print(firstPage.extractText())

stop = stopwords.words('english')

"""string = 
Hey,
This week has been crazy. Attached is my report on IBM. Can you give it a quick read and provide some feedback.
Also, make sure you reach out to Claire (claire@xyz.com).
You're the best.
Cheers,
George W.
212-555-1234
"""
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

"""def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names
"""
s1=""
count=0
if __name__ == '__main__':
    directory = 'E:/DEGREE/PROJECT/BE PROJ/BE Proj'
    string=""
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            f = open(filename)
            #lines = f.read()
            name=f.name
            mypdf=open(name, mode='rb')
            pdf_document=PyPDF2.PdfFileReader(mypdf)
            print(pdf_document.numPages)
            firstPage=pdf_document.getPage(0)
            string=firstPage.extractText()
            numbers = extract_phone_numbers(string)
            emails = extract_email_addresses(string)
            #print (lines[10])
            print(numbers)
            print(emails)
            
            continue
        else:
            continue
        
    #names = extract_names(string)
    
    
        