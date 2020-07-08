import re
import nltk
from nltk.corpus import stopwords
import PyPDF2
import os
#Send Mail
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#print(firstPage.extractText())
MY_ADDRESS = 'bhavinnirmal98@gmail.com'
PASSWORD = '#passwordsucks#'
stop = stopwords.words('english')#to ignore english useless words such as in,above


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

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


s1=""
s5=""
count=0
i=0
name=""
filename1=""
directory = 'D:/DEGREE/PROJECT WORK/BEPROJECTJUPYTER/nodejs/Selected_Candidates'
string=""
for filename1 in os.listdir(directory):
    if filename1.endswith('.pdf'):
        f=open(directory+"/"+filename1,'r')
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
        s5=emails[i]
        print(s5)


        # set up the SMTP server
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

        # For each contact, send the email:
        msg = MIMEMultipart()       # create a message


        msg['From']=MY_ADDRESS
        msg['To']=s5
        msg['Subject']="This is TEST"

        # add in the message body
        msg.attach(MIMEText("Testing Of Project By Bhavin Nirmal. SO Just Relax.", 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

        # Terminate the SMTP session and close the connection
        s.quit()
        continue
    else:
        continue
