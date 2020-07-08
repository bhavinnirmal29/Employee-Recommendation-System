# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:49:51 2020

@author: Jitendra Nirmal
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:23:03 2020

@author: Jitendra Nirmal
"""
#BACKUP CODE
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:22:17 2020

@author: Bhavin
"""
import time
import nltk
from nltk.corpus import stopwords
import PyPDF2
import os
#Send Mail
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.display import Image
#%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import date
import socket
import urllib.request
import PyPDF2
import re
import statistics
from nltk.tokenize import sent_tokenize,word_tokenize
from statistics import mean
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from tkinter.scrolledtext import ScrolledText
IPaddress=socket.gethostbyname(socket.gethostname())

class HomePage(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand= True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in (Page1,CompanyProfilePage,ProcessPage,PlacedCandidates,Create_Company,About_Page,Contact_Page,AfterUserLoginPage,DemoPage,LoginPage,MainPage):
            frame=F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(Page1)
    
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class ProcessPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.logout_btn=tk.Button(self,text="LOGOUT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.logout_Button(controller))
        self.logout_btn.grid(row=0,column=0,padx=15,pady=20)
        
        self.head_lbl=tk.Label(self,text="ERS",fg="black",bg="light blue",font=("Times New Roman",30),width=32,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0, column=1,columnspan=3,padx=15,pady=20,ipady=10)
        
        self.back_btn=tk.Button(self,text="BACK",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.back_Button(controller))
        self.back_btn.grid(row=0,column=4,padx=15,pady=20)
        
        self.head_lbl=tk.Label(self,text="CANDIDATES",fg="black",bg="light blue",font=("Times New Roman",30),width=32,relief="solid")
        self.head_lbl.grid(row=1,columnspan=5,padx=15,pady=20,ipady=10)
        
        self.Lb1 = tk.Listbox(self, width=80, height=10,font=("times",16),bg="light green",selectbackground="black")
        self.Lb1.grid(row=2, columnspan=4,pady=15)
        
        self.start_btn=tk.Button(self,text="START",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.start_Prediction(controller))
        self.start_btn.grid(row=3,columnspan=4,padx=15,pady=20)
        
        # create a vertical scrollbar to the right of the listbox
        yscroll = tk.Scrollbar(self,command=self.Lb1.yview, orient=tk.VERTICAL)
        yscroll.grid(row=2, columnspan=4,sticky="NSE",pady=15)
        self.Lb1.configure(yscrollcommand=yscroll.set)
        self.directory = 'E:/DEGREE/PROJECT WORK/BEPROJECTJUPYTER/nodejs/upload'
        self.name=[]
        for filename1 in os.listdir(self.directory):
            if filename1.endswith('.pdf'):
                f=open(self.directory+"/"+filename1,'r')
                #lines = f.read()
                self.name.append(f.name)
        for i in self.name:
            self.Lb1.insert(1,i)
        
        self.temp=""                
        def on_select(event):
            self.temp=event.widget.get(event.widget.curselection())
            print(self.temp)
        
        self.Lb1.bind('<<ListboxSelect>>', on_select)
        
        tk.Frame.configure(self,background="light blue")
        
    def back_Button(self,cont):
        self.name=[]
        self.Lb1.delete(0,'end')
        for filename1 in os.listdir(self.directory):
            if filename1.endswith('.pdf'):
                f=open(self.directory+"/"+filename1,'r')
                #lines = f.read()
                string1=filename1.split('.')
                self.name.append(string1[0])
        for i in self.name:
            self.Lb1.insert(1,i)
            
        cont.show_frame(MainPage)
    
    def extract(self,l2):
        ResSearch=[]
        l=[]
        l1=[]
        skills=[]
        ratings=[]
        backlogs=0
        cgpa=0
        experience=[]
        #internship=[]
    
        # BACKLOGS
        for i in range(0,len(l2)):
            if(i==len(l2)-3):
                break
            b1=l2[i]
            b3=l2[i+2]
            if(b1=='Backlogs' and b3.isdigit()):
                #print(b1,b3)
                backlogs=int(b3)
    
        #experience
        for i in range(0,len(l2)):
            if(i==len(l2)-3):
                break
            e1=l2[i]
            e2=l2[i+1]
    
            if(e1.isdigit() and e2=='year' or e2=='years'):
                #print(e1,e2)
                experience.append(int(e1))
            elif(e1.isdigit() and e2=='month' or e2=='months'):
                temp=int(e1)
                e1=float(temp/12)
                experience.append(e1)
        experience=sum(experience)
        if(experience<=1.0):
            experience=50
        elif(experience>1.0 and experience<=2.0):
            experience=70
        elif(experience>2.0 ):
            experience=90
        #CGPA
        for i in range(0,len(l2)):
            if(i==len(l2)-3):
                break
            b1=l2[i]
            b3=l2[i+2]
            if(b1=='CGPA' or b1=="cgpa" and b3.isdigit()):
                #print(b1,b3)
                cgpa=float(b3)
        #SKILLS AND RATINGS
        for i in range(0,len(l2)):
            if(i==len(l2)-3):
                break
            else:
                t1=l2[i]
                t2=l2[i+1]
                t3=l2[i+2]
                if(t1.isalpha() and t2=='-' and t3.isdigit() and len(t3)==2):
                    #print(t1,t2,t3)
                    skills.append(t1)
                    ratings.append(int(t3))
                else:
                    t1=""
                    t2=""
                    t3=""
                    continue
        pred=[]
        #print("SKILLS - ")  
        #print(skills)
        l=len(skills)
        if(l==0):
            technical=0
        elif(l<=2):
            technical=20
        elif(l>2 and l<=5):
            technical=50
        elif(l>5 and l<=7):
            technical=70
        elif(l>7):
            technical=90
        #print("RATINGS - ")
        #print(ratings)
        sum1=sum(ratings)/len(ratings)
    
        #print("PROJECT - ")
        project=round(sum1)
        #print(project)
        #print("EXPERIENCE - ")
        #print(experience)
        #print("CGPA - ")
        #print("Backlog - ")
        #print(backlogs)
        #print(cgpa)
    
        pred.append(technical)
        pred.append(cgpa)
        pred.append(sum1)
        pred.append(project)
        pred.append(experience)
        pred.append(backlogs)
        return pred



    def start_Prediction(self,cont):
        directory = 'E:/DEGREE/PROJECT WORK/BEPROJECTJUPYTER/nodejs/upload'
        pred=[]
        self.file=[]
        self.email=[]
        self.names=[]
        self.string1=""
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                print(filename)
                self.string1=filename.split('.')
                self.file.append(self.string1[0])
                f = open(directory+"/"+filename)
                name=f.name
                mypdf=open(name, mode='rb')
                reader=PyPDF2.PdfFileReader(mypdf)
                n_of_pages = reader.numPages
                #print(reader.numPages)
                resume_text=""
                page=0
                for i in range(0,n_of_pages):
                    page=reader.getPage(i)
                    resume_text+=page.extractText()
                self.text1=resume_text
                l2=word_tokenize(self.text1)
                x=self.extract(l2)
                print(x)
                pred.append(x)
                #print(pred)
                data = pd.read_csv("Book-test.csv")
                data.head()
                data.isnull().sum()
                f,ax=plt.subplots(1,2,figsize=(12,6))
                data[' Placed'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
                ax[0].set_title(' Placed')
                ax[0].set_ylabel('')
                sns.countplot(' Placed',data=data,ax=ax[1])
                ax[1].set_title('Placed')
                #plt.show()
                data = pd.get_dummies(data)
                data.head()
                Y=data[' Placed'].values
                X=data.drop(' Placed',axis=1).values
                
                
                x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=21)
                knn = KNeighborsClassifier(n_neighbors=7)
        
                #Train the model using the training sets
                knn.fit(x_train, y_train)
                
                y_pred = knn.predict(x_test)
                self.email.append(self.extract_email_addresses(self.text1))
                # Model Accuracy, how often is the classifier correct?
                print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
               
            else:
                continue
        
        
        for i in range(0,len(pred)):
            temp1=""
            temp2=""
            temp3=""
            predicted= knn.predict([pred[i]])# 0:Overcast, 2:Mild
            print(predicted)
            print("After PRediction "+self.file[i])
            temp2=str(self.email[i])
            temp1=str(self.file[i])
            temp3=str(predicted)
            print(type(temp1))
            print(type(temp2))
            print(type(temp3))
            time.sleep(1)
            if(predicted==1):
                print(self.email[i])
                self.pred1(temp2)
                #print("1 Row Inserted ")
            else:
                print(self.email[i])
                conn=sqlite3.connect("users1.db")
                c=conn.cursor()
                c.execute('''CREATE TABLE if not exists Prediction_Data_Unselected 
                         (c_name text,c_email text,predicted text)''')
                # Insert a row of data
                c.execute("INSERT INTO Prediction_Data_Unselected (c_name,c_email,predicted) VALUES ('"+temp1+"','"+temp2+"','"+temp3+"')")
                conn.commit()
                conn.close()
                #continue
        print(self.file)
        
    def pred1(self,temp2):
        conn=sqlite3.connect("users1.db")
        c=conn.cursor()
        c.execute("create table if not exists demotable (email1 text)")
        conn.commit()
        c.execute("insert into demotable values ('"+temp2+"')")
        conn.commit()
        conn.close()
    def extract_email_addresses(self,string):
        r = re.compile(r'[\w\.-]+@[\w\.-]+')
        return r.findall(string)

    def logout_Button(self,cont):
        tk.messagebox.showinfo("Logout","You have been Logged Out")
        cont.show_frame(LoginPage)
    
    def exit_Button(self,cont):
        cont.destroy()
    
class PlacedCandidates(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.logout_btn=tk.Button(self,text="LOGOUT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.logout_Button(controller))
        self.logout_btn.grid(row=0,column=0,padx=15,pady=20)
        
        self.head_lbl=tk.Label(self,text="PLACED CANDIDATES",fg="black",bg="light blue",font=("Times New Roman",30),width=32,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0, column=1,columnspan=3,padx=15,pady=20,ipady=10)
        
        self.exit_btn1=tk.Button(self,text="BACK",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.back_Button(controller))
        self.exit_btn1.grid(row=0,column=4,padx=15,pady=20)
    
        
        self.Lb1 = tk.Listbox(self, width=80, height=10,font=("times",16),bg="light green",selectbackground="black")
        self.Lb1.grid(row=2, columnspan=4,pady=15)
        
        # create a vertical scrollbar to the right of the listbox
        #yscroll = tk.Scrollbar(self,command=Lb1.yview, orient=tk.VERTICAL)
        #yscroll.grid(row=3, column=4, sticky="NSWE", pady=15)
        #Lb1.configure(yscrollcommand=yscroll.set)
        self.directory = 'E:/DEGREE/PROJECT WORK/BEPROJECTJUPYTER/nodejs/Selected_Candidates'
        self.name=[]
        string1=""
        for filename1 in os.listdir(self.directory):
            if filename1.endswith('.pdf'):
                f=open(self.directory+"/"+filename1,'r')
                #lines = f.read()
                string1=filename1.split('.')
                self.name.append(string1[0])
        for i in self.name:
            self.Lb1.insert(1,i)
        
        self.temp=""                
        def on_select(event):
            self.temp=event.widget.get(event.widget.curselection())
            print(self.temp)
        
        self.Lb1.bind('<<ListboxSelect>>', on_select)
        
        tk.Frame.configure(self,background="light blue")
        
    def back_Button(self,cont):
        self.name=[]
        self.Lb1.delete(0,'end')
        string1=""
        for filename1 in os.listdir(self.directory):
            if filename1.endswith('.pdf'):
                f=open(self.directory+"/"+filename1,'r')
                string1=filename1.split('.')
                #lines = f.read()
                self.name.append(string1)
        for i in self.name:
            self.Lb1.insert(1,i)
        cont.show_frame(MainPage)
    def logout_Button(self,cont):
        tk.messagebox.showinfo("Logout","You have been Logged Out")
        cont.show_frame(LoginPage)
    
    def exit_Button(self,cont):
        cont.destroy()

class CompanyProfilePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.back_btn1=tk.Button(self,text="LOGOUT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.back_Button(controller))
        self.back_btn1.grid(row=0,column=0,padx=15,pady=20)
        
        self.head_lbl=tk.Label(self,text="COMPANY PROFILE",fg="black",bg="light blue",font=("Times New Roman",30),width=32,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0, column=1,columnspan=3,padx=15,pady=20,ipady=10)
        
        self.exit_btn1=tk.Button(self,text="BACK",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.back_Button(controller))
        self.exit_btn1.grid(row=0,column=4,padx=15,pady=20)
        
        self.lb1=tk.Label(self,text="Company Name : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb1.grid(row=1,column=1,sticky="W")
        
        self.c_name=tk.StringVar()
        self.et1=ScrolledText(self,bd=6,width=24,height=2,font=("Times New Roman",22))
        self.et1.focus()
        #self.et1.delete(0,'end')
        self.et1.grid(row=1,column=2,sticky="w",pady=10)
        
        self.lb2=tk.Label(self,text="Company ID : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb2.grid(row=2,column=1,sticky="W")
        
        self.id2=tk.StringVar()
        self.et2=tk.Entry(self,bd=6,width=25,font=("Times New Roman",22),textvariable=self.id2)
        #self.et2.focus()
        #self.et2.delete(0,'end')
        self.et2.grid(row=2,column=2,sticky="w",pady=10)
        
        self.lb3=tk.Label(self,text="Address : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb3.grid(row=4,column=1,sticky="W")
        
        self.et3=ScrolledText(self,bd=6,font=("Times New Roman",22),width=24,height=3)
        self.et3.grid(row=4,column=2,sticky="W",pady=10)
        
        self.lb4=tk.Label(self,text="Username : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb4.grid(row=5,column=1,sticky="W")
        
        self.uname=tk.StringVar()
        self.et4=tk.Entry(self,bd=6,width=25,font=("Times New Roman",22),textvariable=self.uname)
        self.et4.delete(0,'end')
        self.et4.grid(row=5,column=2,sticky="w",pady=10)
        
        self.get_btn=tk.Button(self,text="GET PROFILE",fg="black",bg="light green",font=("Times New Roman",18),width=20,border=15,command = lambda:self.get_Profile_Button(controller))
        self.get_btn.grid(row=6,column=2,padx=15,pady=20)
        
        tk.Frame.configure(self,background="light blue")
        
    def get_Profile_Button(self,cont):
        conn=sqlite3.connect("users1.db")
        c=conn.cursor()
        p_uname=""
        c.execute("Select * from LoginDetail")
        rows=c.fetchall()
        for i in rows:
            p_uname=i[0]
            
        conn=sqlite3.connect("users1.db")
        c=conn.cursor()
        c.execute("Select * from Signup where username = '"+p_uname+"'")
        rows=c.fetchall()
        for row in rows:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            self.et1.insert(1.0,row[0])
            self.et2.insert(0,row[1])
            self.et3.insert(1.0,row[2])
            self.et4.insert(0,row[3])
            
     
        #print(p_uname)
    def logout_Button(self,cont):
        self.et1.delete(1.0,'end')
        self.et2.delete(0,'end')
        self.et3.delete(1.0,'end')
        self.et4.delete(0,'end')
        tk.messagebox.showinfo("Logout","You have been Logged Out")
       
        cont.show_frame(LoginPage)
        
    def back_Button(self,cont):
        self.et1.delete(1.0,'end')
        self.et2.delete(0,'end')
        self.et3.delete(1.0,'end')
        self.et4.delete(0,'end')
        cont.show_frame(MainPage)
        
        
class MainPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.logout_btn=tk.Button(self,text="LOGOUT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.logout_Button(controller))
        self.logout_btn.grid(row=0,column=0,padx=15,pady=20)
        
        self.head_lbl=tk.Label(self,text="ERS",fg="black",bg="light blue",font=("Times New Roman",30),width=32,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0, column=1,columnspan=3,padx=15,pady=20,ipady=10)
        
        self.exit_btn1=tk.Button(self,text="EXIT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.exit_Button(controller))
        self.exit_btn1.grid(row=0,column=4,padx=15,pady=20)
        
        self.btn1=tk.Button(self,text="PLACED CANDIDATES",border=15,fg="black",bg="light green",font=("Times New Roman",18),width=25,command=lambda:controller.show_frame(PlacedCandidates))
        self.btn1.grid(row=3,column=2,sticky="W",pady=25,padx=65)
        
        self.btn2=tk.Button(self,text="START SELECTION",border=15,fg="black",bg="light green",font=("Times New Roman",18),width=25,command=lambda:controller.show_frame(ProcessPage))
        self.btn2.grid(row=4,column=2,sticky="W",pady=25,padx=65)
        
        self.btn2=tk.Button(self,text="COMPANY PROFILE",border=15,fg="black",bg="light green",font=("Times New Roman",18),width=25,command=lambda:controller.show_frame(CompanyProfilePage))
        self.btn2.grid(row=5,column=2,sticky="W",pady=25,padx=65)
        
        self.btn2=tk.Button(self,text="STATISTICS",border=15,fg="black",bg="light green",font=("Times New Roman",18),width=25)
        self.btn2.grid(row=6,column=2,sticky="W",pady=25,padx=65)
        
        tk.Frame.configure(self,background="light blue")
        
    
    def logout_Button(self,cont):
        tk.messagebox.showinfo("Logout","You have been Logged Out")
        cont.show_frame(LoginPage)
    
    def exit_Button(self,cont):
        cont.destroy()
        
        
class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        self.back_btn2=tk.Button(self,text="BACK",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.back_Button(controller))
        self.back_btn2.grid(row=0,column=0,padx=15,pady=20)
        
        self.head_lbl=tk.Label(self,text="LOGIN",fg="black",bg="light blue",font=("Times New Roman",30),width=32,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0, column=1,columnspan=3,padx=15,pady=20,ipady=10)
        
        self.exit_btn1=tk.Button(self,text="EXIT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.exit_Button(controller))
        self.exit_btn1.grid(row=0,column=4,padx=15,pady=20)
        
        self.lb1=tk.Label(self,text="User Name : ",bg="light blue",fg="black",font=("Times New Roman",24))
        self.lb1.grid(row=1,column=1,sticky="W",pady=60)
        
        self.uname=tk.StringVar()
        self.login_field=tk.Entry(self,bd=6,width=24,font=("Times New Roman",24),textvariable=self.uname)
        self.login_field.focus()
        self.login_field.delete(0,'end')
        self.login_field.grid(row=1,column=2,sticky="W")
        
        self.lb2=tk.Label(self,text="Password : ",bg="light blue",fg="black",font=("Times New Roman",24))
        self.lb2.grid(row=2,column=1,sticky="W")
        
        self.pwd1=tk.StringVar()
        self.pwd_field=tk.Entry(self,bd=6,width=24,show="*",font=("Times New Roman",24),textvariable=self.pwd1)
        self.pwd_field.grid(row=2,column=2,sticky="W")
        
        self.login_btn=tk.Button(self,text="LOGIN",border=15,fg="black",bg="light green",font=("Times New Roman",18),width=10,command=lambda:self.validate_Login_Page(controller))
        self.login_btn.grid(row=3,column=2,sticky="W",pady=40)
        
        self.clear_btn=tk.Button(self,text="CLEAR",border=15,fg="black",bg="light green",font=("Times New Roman",18),width=10,command=lambda:self.clear_(controller))
        self.clear_btn.grid(row=3,column=3,pady=40)
        
        tk.Frame.configure(self,background="light blue")
    
    def clear_(self,cont):
        self.login_field.delete(0,'end')
        self.pwd_field.delete(0,'end')
        self.login_field.focus()
    def back_Button(self,cont):
        cont.show_frame(Page1)
    
    def exit_Button(self,cont):
        cont.destroy()
    
    def calculations(self,cont):
        data = pd.read_csv("Book-test.csv")
        data.head()
        data.isnull().sum()
        f,ax=plt.subplots(1,2,figsize=(12,6))
        data[' Placed'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
        ax[0].set_title(' Placed')
        ax[0].set_ylabel('')
        sns.countplot(' Placed',data=data,ax=ax[1])
        ax[1].set_title('Placed')
        #plt.show()
        data = pd.get_dummies(data)
        data.head()
        Y=data[' Placed'].values
        X=data.drop(' Placed',axis=1).values
        
        '''LOGISTICS REGRESSION '''
        
        x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=21)
        clf = LogisticRegression(fit_intercept=True)
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
        
        '''KNN NEIGHBORS '''
        
        #Create KNN Classifier
        knn = KNeighborsClassifier(n_neighbors=7)
        
        #Train the model using the training sets
        knn.fit(x_train, y_train)
        
        y_pred = knn.predict(x_test)
        
        # Model Accuracy, how often is the classifier correct?
        print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
        
        '''Naive Bayes '''
        
        #Create a Gaussian Classifier
        gnb = GaussianNB()
        
        #Train the model using the training sets
        gnb.fit(x_train, y_train)
        
        #Predict the response for test dataset
        y_pred = gnb.predict(x_test)
        
        # Model Accuracy, how often is the classifier correct?
        print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
        
    def validate_Login_Page(self,cont):
        self.uname2=self.uname.get()
        self.pwd2=self.pwd1.get()
        conn=sqlite3.connect("users1.db")
        c=conn.cursor()
        c.execute("select * from signup")
        rows=c.fetchall()
        conn.commit()
        flag=0
        for row in rows:
            if(self.uname2==row[3] and self.pwd2==row[4]):
                flag=1
                break
            else:
                continue
        if(flag==1):
            tk.messagebox.showinfo("Login","Login Successfull")
            i=0
            conn=sqlite3.connect("users1.db")
            c=conn.cursor()
            c.execute("SELECT * FROM LoginDetail")
            rows=c.fetchall()
            for row in rows:
                i=i+1
            if i>1:    
                uname=rows[0]
                c.execute("DELETE FROM LoginDetail WHERE username='%s'"%uname)
                conn.commit()
                conn.close()
            else:
                print("No Rows")
            conn1=sqlite3.connect("users1.db")
            c1=conn1.cursor()
            c1.execute("CREATE TABLE IF NOT EXISTS LoginDetail(username text)")
            c1.execute("INSERT INTO LoginDetail VALUES('"+self.uname2+"')")
            conn1.commit()
            conn1.close()
            self.login_field.delete(0,'end')
            self.pwd_field.delete(0,'end')
            self.calculations(cont)
            cont.show_frame(MainPage)
        else:
            tk.messagebox.showinfo("Error","Invalid Credentials")
            self.login_field.delete(0,'end')
            self.pwd_field.delete(0,'end')
            self.login_field.focus()
        
   
class Page1(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        self.head_lbl=tk.Label(self,text="EMPLOYEE RECOMMENDATION SYSTEM",fg="black",bg="light blue",font=("Times New Roman",30),width=50,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0,columnspan=10,pady=20,ipady=20)
        
        self.create_btn1=tk.Button(self,text="CREATE A COMPANY",fg="black",bg="light green",font=("Times New Roman",18),width=22,border=15,command = lambda: self.create_(controller))
        self.create_btn1.grid(row=1,column=1,padx=25,pady=100)
        
        self.about_btn1=tk.Button(self,text="ABOUT",fg="black",bg="light green",font=("Times New Roman",18),width=15,border=15,command = lambda:self.about_(controller))
        self.about_btn1.grid(row=1,column=2,padx=25,pady=100)
        
        self.contact_btn1=tk.Button(self,text="CONTACT",fg="black",bg="light green",font=("Times New Roman",18),width=15,border=15,command = lambda:self.contact_(controller))
        self.contact_btn1.grid(row=1,column=3,padx=25,pady=100)
        
        self.exit_btn1=tk.Button(self,text="EXIT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command= lambda: self.exit_funct(controller))
        self.exit_btn1.grid(row=1,column=4,padx=25,pady=100)
        
        self.query_btn1=tk.Button(self,text="SEND A QUERY",fg="black",bg="light green",font=("Times New Roman",18),width=15,border=15,command= lambda: self.exit_funct(controller))
        self.query_btn1.grid(row=2,column=2,sticky="ns")
        
        self.login_btn1=tk.Button(self,text="LOGIN",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command= lambda: self.login_(controller))
        self.login_btn1.grid(row=2,column=3,padx=55,pady=0)
        tk.Frame.configure(self,background="light blue")
        
        if IPaddress=="127.0.0.1":
            self.status_lbl=tk.Label(self,text="Internet Status : Not Connected ",fg="black",bg="light blue",font=("Times New Roman",30),width=50,borderwidth=3,relief="solid")
            self.status_lbl.grid(row=3,columnspan=10,pady=20,ipady=20)
        else:
            self.status_lbl=tk.Label(self,text="Internet Status : Connected with the IP Address:  "+IPaddress,fg="black",bg="light blue",font=("Times New Roman",30),width=50,borderwidth=3,relief="solid")
            self.status_lbl.grid(row=3,columnspan=10,pady=20,ipady=20)
           
    def create_(self,cont):
        cont.show_frame(Create_Company)
    
    def about_(self,cont):
        cont.show_frame(About_Page)
     
    def contact_(self,cont):
        cont.show_frame(Contact_Page)
        
    def exit_funct(self,cont):
        cont.destroy()
    
    def login_(self,cont):
        cont.show_frame(LoginPage)

class Create_Company(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        self.back_btn1=tk.Button(self,text="BACK",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.back_Button(controller))
        self.back_btn1.grid(row=0,column=0,padx=15,pady=20)
        
        self.head_lbl=tk.Label(self,text="CREATE COMPANY PROFILE",fg="black",bg="light blue",font=("Times New Roman",30),width=32,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0, column=1,columnspan=3,padx=15,pady=20,ipady=10)
        
        self.exit_btn1=tk.Button(self,text="EXIT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.exit_Button(controller))
        self.exit_btn1.grid(row=0,column=4,padx=15,pady=20)
        
        self.lb1=tk.Label(self,text="Company Name : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb1.grid(row=1,column=1,sticky="W")
        
        self.c_name=tk.StringVar()
        self.et1=ScrolledText(self,bd=6,width=24,height=2,font=("Times New Roman",22))
        self.et1.focus()
        #self.et1.delete(0,'end')
        self.et1.grid(row=1,column=2,sticky="w",pady=10)
        
        self.lb2=tk.Label(self,text="Company ID : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb2.grid(row=2,column=1,sticky="W")
        
        self.id2=tk.StringVar()
        self.et2=tk.Entry(self,bd=6,width=25,font=("Times New Roman",22),textvariable=self.id2)
        #self.et2.focus()
        self.et2.delete(0,'end')
        self.et2.grid(row=2,column=2,sticky="w",pady=10)
        
        self.lb3=tk.Label(self,text="Address : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb3.grid(row=4,column=1,sticky="W")
        
        self.et3=ScrolledText(self,bd=6,font=("Times New Roman",22),width=24,height=3)
        self.et3.grid(row=4,column=2,sticky="W",pady=10)
        
        self.lb4=tk.Label(self,text="Username : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb4.grid(row=5,column=1,sticky="W")
        
        self.uname=tk.StringVar()
        self.et4=tk.Entry(self,bd=6,width=25,font=("Times New Roman",22),textvariable=self.uname)
        self.et4.delete(0,'end')
        self.et4.grid(row=5,column=2,sticky="w",pady=10)
        
        self.lb5=tk.Label(self,text="Password : ",bg="light blue",fg="black",font=("Times New Roman",22))
        self.lb5.grid(row=6,column=1,sticky="W")
        
        self.uname=tk.StringVar()
        self.et5=tk.Entry(self,bd=6,width=25,show="*",font=("Times New Roman",22),textvariable=self.uname)
        self.et5.grid(row=6,column=2,sticky="w",pady=10)
        
        
        self.create_btn1=tk.Button(self,text="CREATE",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command= lambda: self.validate_Company(controller))
        self.create_btn1.grid(row=7,column=1,pady=10)
        
        self.reset_btn=tk.Button(self,text="CLEAR",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command= lambda: self.clear_(controller))
        self.reset_btn.grid(row=7,column=2,sticky="W",pady=10)
        
        tk.Frame.configure(self,background="light blue")
    
    def validate_Company(self,cont):
        self.c1=str(self.et1.get('1.0',tk.END))
        self.c2=str(self.et2.get())
        self.c3=str(self.et3.get('1.0',tk.END))
        self.c4=str(self.et4.get())
        self.c5=str(self.et5.get())
        conn=sqlite3.connect("users1.db")
        c=conn.cursor()
        c.execute("select * from signup")
        rows=c.fetchall()
        conn.commit()
        flag=0
        for i in rows:
            if(self.c1==i[0] or self.c2==i[1] or self.c3==i[3]):
                flag=1
                break
            else:
                flag=0
        if flag==1:
            tk.messagebox.showinfo("Error","Name, ID or Admin Already Exists")
            self.et1.delete(1.0,'end')
            self.et2.delete(0,'end')
            self.et3.delete(1.0,'end')
            self.et4.delete(0,'end')
            self.et5.delete(0,'end')
        else:
            if len(self.c1)==0 or len(self.c2)==0 or len(self.c3)==0 or len(self.c4)==0 or len(self.c5)==0: 
                tk.messagebox.showinfo("Alert","Enter valid Values")
                self.et1.delete(1.0,'end')
                self.et2.delete(0,'end')
                self.et3.delete(1.0,'end')
                self.et4.delete(0,'end')
                self.et5.delete(0,'end')
                
            else:    
                conn=sqlite3.connect("users1.db")
                c=conn.cursor()
                c.execute('''CREATE TABLE if not exists signup 
                     (company_name text,company_id text,address text,username text,pwd text)''')
                # Insert a row of data
                c.execute("INSERT INTO signup VALUES ('"+self.c1+"','"+self.c2+"','"+self.c3+"','"+self.c4+"','"+self.c5+"')")
                #print("1 Row Inserted ")
                tk.messagebox.showinfo("Register","Succesfull")
                conn.commit()
                conn.close()
                self.et1.delete(1.0,'end')
                self.et2.delete(0,'end')
                self.et3.delete(1.0,'end')
                self.et4.delete(0,'end')
                self.et5.delete(0,'end')
                cont.show_frame(LoginPage)
    
    def back_Button(self,cont):
        cont.show_frame(Page1)
    
    def exit_Button(self,cont):
        cont.destroy()
        
    def clear_(self,cont):
        self.et1.delete(1.0,'end')
        self.et2.delete(0,'end')
        self.et3.delete(1.0,'end')
        self.et4.delete(0,'end')
        self.et5.delete(0,'end')
        self.et2.focus()
        
class About_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.back_btn1=tk.Button(self,text="BACK",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.back_Button(controller))
        self.back_btn1.grid(row=0,column=1,padx=15,pady=20)
        
        self.head_lbl=tk.Label(self,text="ABOUT",fg="black",bg="light blue",font=("Times New Roman",30),width=30,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0,column=2,padx=20,pady=20,ipady=20)
        
        self.exit_btn1=tk.Button(self,text="EXIT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.exit_Button(controller))
        self.exit_btn1.grid(row=0,column=3,padx=15,pady=20)
        
        tk.Frame.configure(self,background="light blue")
    
    def back_Button(self,cont):
        cont.show_frame(Page1)
    
    def exit_Button(self,cont):
        cont.destroy()
    
class Contact_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        self.back_btn1=tk.Button(self,text="BACK",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.back_Button(controller))
        self.back_btn1.grid(row=0,column=1,padx=15,pady=20)
               
        self.head_lbl=tk.Label(self,text="CONTACT US",fg="black",bg="light blue",font=("Times New Roman",30),width=34,borderwidth=3,relief="solid")
        self.head_lbl.grid(row=0,column=2,pady=20,ipady=20)
        
        self.exit_btn1=tk.Button(self,text="EXIT",fg="black",bg="light green",font=("Times New Roman",18),width=10,border=15,command = lambda:self.exit_Button(controller))
        self.exit_btn1.grid(row=0,column=3,padx=15,pady=20)
        
        tk.Frame.configure(self,background="light blue")
    
    def back_Button(self,cont):
        cont.show_frame(Page1)
    
    def exit_Button(self,cont):
        cont.destroy()
        
class AfterUserLoginPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        skill1_label=tk.Label(self,text="SKILL 1",fg="black",bg="light green",font=("Times New Roman",18),width=10)
        skill1_label.grid(row=0,column=0,padx=15)
        
        self.sk1=tk.StringVar()
        self.skill_1=tk.Entry(self,text="",fg="black",font=("Times New Roman",18),width=20,textvariable=self.sk1)
        self.skill_1.focus()
        self.skill_1.delete(0,'end')
        self.skill_1.grid(row=0,column=1,padx=15,pady=15)
        
        skill2_label=tk.Label(self,text="SKILL 2",fg="black",bg="light green",font=("Times New Roman",18),width=10)
        skill2_label.grid(row=0,column=2,padx=15)
        
        self.sk2=tk.StringVar()
        self.skill_2=tk.Entry(self,text="",fg="black",font=("Times New Roman",18),width=20,textvariable=self.sk2)
        self.skill_2.delete(0,'end')
        self.skill_2.grid(row=0,column=3,padx=15,pady=15)
        
        skill3_label=tk.Label(self,text="SKILL 3",fg="black",bg="light green",font=("Times New Roman",18),width=10)
        skill3_label.grid(row=1,column=0,padx=15)
        
        self.sk3=tk.StringVar()
        self.skill_3=tk.Entry(self,text="",fg="black",font=("Times New Roman",18),width=20,textvariable=self.sk3)
        self.skill_3.delete(0,'end')
        self.skill_3.grid(row=1,column=1,padx=15,pady=15)
        
        skill4_label=tk.Label(self,text="SKILL 4",fg="black",bg="light green",font=("Times New Roman",18),width=10)
        skill4_label.grid(row=1,column=2,padx=15)
        
        self.sk4=tk.StringVar()
        self.skill_4=tk.Entry(self,text="",fg="black",font=("Times New Roman",18),width=20,textvariable=self.sk4)
        self.skill_4.delete(0,'end')
        self.skill_4.grid(row=1,column=3,padx=15,pady=15)
        
        btn1=tk.Button(self,text="CALCULATE",fg="black",bg="light blue",font=("Times New Roman",18),width=15,command=lambda: self.calculate(controller))
        btn1.grid(row=2,column=2,padx=25)
        
        Lb1 = tk.Listbox(self, width=80, height=10,font=("times",16),bg="light green",selectbackground="black")
        Lb1.grid(row=3, columnspan=4,pady=15)
        
        # create a vertical scrollbar to the right of the listbox
        yscroll = tk.Scrollbar(self,command=Lb1.yview, orient=tk.VERTICAL)
        yscroll.grid(row=3, column=4, sticky="NSWE", pady=15)
        Lb1.configure(yscrollcommand=yscroll.set)
        self.temp=""
        def on_select(event):
            self.temp=event.widget.get(event.widget.curselection())
            print(self.temp)
        
        tk.Frame.configure(self,background="grey")
        
    def calculate(self,cont):
        self.sk11=self.sk1.get()
        self.sk22=self.sk2.get()
        self.sk33=self.sk3.get()
        self.sk44=self.sk4.get()
        self.skillList=[self.sk11,self.sk22,self.sk33,self.sk44]
        if(self.sk11!="" and self.sk22!="" and self.sk33!="" and self.sk44!=""):
            s1=""
            ts=str(date.today())
            s1=self.sk11+""+self.sk22+""+self.sk33+""+self.sk33+""+self.sk4
            conn=sqlite3.connect("details.db")
            c=conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS Details(skills text,Timestamp text)")
            c.execute("INSERT INTO Details VALUES('"+s1+"','"+ts+"')")
            conn.commit()
            conn.close()
            
        else:
            tk.messagebox.showerror('Value Error',"Invalid Entries")
        
class DemoPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        #user_logout_btn=tk.Button(self,text="LOGOUT",fg="light green",bg="black",font=("Times New Roman",18),width=10,compound="left",command=lambda: self.logout_Button(controller))
        #user_logout_btn.grid(row=0,columnspan=2,pady=20,padx=10)        
        
        user_detail_label=tk.Label(self,text="User Details",fg="red",bg="light blue",font=("Times New Roman",38))
        user_detail_label.grid(row=0,column=2,padx=40)
        
        self.profile_btn=tk.Button(self,text="My Profile",fg="black",bg="light green",font=("Times New Roman",18),width=10)
        self.profile_btn.grid(row=1,column=2,pady=25)
        
        issue_btn=tk.Button(self,text="Issue Book",fg="black",bg="light green",font=("Times New Roman",18),width=10)
        issue_btn.grid(row=2,column=2,pady=25)
        
        return_btn=tk.Button(self,text="Return Book",fg="black",bg="light green",font=("Times New Roman",18),width=10)
        return_btn.grid(row=3,column=2,pady=25)
        
        tk.Frame.configure(self,background="light blue")
    

       
app=HomePage()
app.title("Employee Recommendation Engine")
app.geometry("1150x700")
app.resizable(0,0)
app.mainloop()