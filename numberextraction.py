# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:11:36 2020

@author: Jitendra Nirmal
"""

import re
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:09:57 2019

@author: Sayali
"""
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
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

def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

def extract_skills(document):
    skills=[]
    skills.append(re.findall('Python',document))
    return skills
    
    
def extract_ratings(document):
    ratings=[]
    '''for sentence in string:
        sen=" ".join([words[0].lower() for words in sentence])
        if(re.search('python',sen)):
            sen_tokenized=nltk.word_tokenize(sen)
            tagged=nltk.pos_tag(sen_tokenized)
            entities=nltk.chunk.ne_chunk(tagged)
            for subtree in entities.subtrees():
                for leaf in subtree.leaves():
                    if(leaf[1]=="CD"):
                        ratings=leaf[0]'''
    #Text=document
    regex_=re.compile(r'[A-Z]*[a-z] - \b\d{2}')
    text1=document
    #print(word_tokenize(text1))
    #ratings.append(re.compile(r"[A-Z]*[a-z] - \b\d{2}",document))
    #ratings.append(re.findall("/(?:[a-z][A-Z]\ \-\ [0-100]\ )/",Text))
    return ratings
    
s1=""
count=0
skills=[]
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
            if(pdf_document.numPages>1):
                second_page=pdf_document.getPage(1)
                string=string+second_page.extractText()
            numbers = extract_phone_numbers(string)
            emails = extract_email_addresses(string)
            ratings=extract_ratings(string)
            #sentences=ie_preprocess(string)
            #print (lines[10])
            skills=extract_skills(string)
            print(numbers)
            print(emails)
            #print(ratings)
            string=""
            print(skills)
            continue
        else:
            continue
'''string = second_page.extractText()
Text="76 "       
el =string
lines=[el.strip() for el in string.split("\n") if len(el) > 0]
lines=[nltk.word_tokenize(el) for el in lines]
lines=[nltk.pos_tag(el) for el in lines]

sentences=nltk.sent_tokenize(string)
sentences=[nltk.word_tokenize(sent) for sent in sentences]
tokens = sentences
sentences = [nltk.pos_tag(sent) for sent in sentences]
dummy=[]
for el in tokens:
    dummy+=el
tokens=dummy
print(tokens)'''
#print(re.findall(r"\b\d{2}\b", Text))