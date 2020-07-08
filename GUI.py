# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:22:17 2020

@author: Bhavin
"""
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import date
import socket
import urllib.request
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
        for F in (Page1,Create_Company,About_Page,Contact_Page,AfterUserLoginPage,DemoPage,LoginPage):
            frame=F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(Page1)
    
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()
        
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
        
    
    def back_Button(self,cont):
        cont.show_frame(Page1)
    
    def exit_Button(self,cont):
        cont.destroy()
        
    def clear_(self,cont):
        self.et1.delete(1.0,'end')
        self.et2.delete(0,'end')
        #self.et3.delete(0,'end')
        self.et4.delete(0,'end')
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
        Lb1.grid(row=3, columnspan=4,padx=10,pady=15)
        
        tk.Frame.configure(self,background="grey")
        
    def calculate(self,cont):
        self.sk11=self.sk1.get()
        self.sk22=self.sk2.get()
        self.sk33=self.sk3.get()
        self.sk44=self.sk4.get()
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
    """def logout_Button(self,cont):
        conn=sqlite3.connect("users1.db")
        c=conn.cursor()
        c.execute("SELECT * FROM LoginDetail")
        rows=c.fetchall()
        uname=rows[0]
        c.execute("DELETE FROM LoginDetail WHERE username='%s'"%uname)
        conn.commit()
        conn.close()
        tk.messagebox.showinfo("Logout","You have been Logged Out")
        cont.show_frame(LoginPage)"""
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
        
        '''l1=tk.Label(self,text="Employee Recommendation Engine",bg="black",compound=tk.CENTER)
        l1.config(font=("Times New Roman",24))
        
        login_header=tk.Label(self,text="LOGIN",fg="black",font=("Times New Roman",38))
        login_header.grid(row=1,column=1,pady=30,ipadx=10)
        
        login_label=tk.Label(self,text="Login Id: ",bg="black",fg="white",font=("Times New Roman",22))
        login_label.grid(row=2,column=0,sticky='w')
        
        
        pwd_label=tk.Label(self,text="Password: ",bg="black",fg="white",font=("Times New Roman",22))
        pwd_label.grid(row=3,column=0,sticky='w',pady=20)
        
        self.pwd1=tk.StringVar()
        self.pwd_field=tk.Entry(self,bd=10,width=20,show="*",font=("Times New Roman",18),textvariable=self.pwd1)
        self.pwd_field.grid(row=3,column=1)
        
        
        
        quit_btn=tk.Button(self,text="QUIT",bd=20,fg="black",bg="light blue",font=("Times New Roman",16),width=10,command=lambda:self.exitFunc(controller))
        quit_btn.grid(row=4,column=2)'''
        tk.Frame.configure(self,background="light blue")
    
    def clear_(self,cont):
        self.login_field.delete(0,'end')
        self.pwd_field.delete(0,'end')
        self.login_field.focus()
    def back_Button(self,cont):
        cont.show_frame(Page1)
    
    def exit_Button(self,cont):
        cont.destroy()

    def validate_Login_Page(self,cont):
        self.uname2=self.uname.get()
        self.pwd2=self.pwd1.get()
        if(self.uname2=='admin' and self.pwd2=='admin'):
            tk.messagebox.showinfo("Login","Login Successfull")
            self.login_field.delete(0,'end')
            self.pwd_field.delete(0,'end')
            conn=sqlite3.connect("users1.db")
            c=conn.cursor()
            c.execute("select username,pwd from signup")
            rows=c.fetchall()
            for row in rows:
                print(row[0],row[1])
            
            flag=0
               
            cont.show_frame(AfterUserLoginPage)
        else:
            tk.messagebox.showinfo("Error","Invalid Credentials")
            self.login_field.delete(0,'end')
            self.pwd_field.delete(0,'end')
            self.login_field.focus()
        
        '''
        b1=tk.Button(self,text="Back To Home",command=lambda: controller.show_frame(StartPage))
        b1.grid(row=5,column=1)
        '''
        
    '''def validate_Login_Page(self,cont):
            self.uname2=self.uname.get()
            self.pwd2=self.pwd1.get()
            conn=sqlite3.connect("users1.db")
            c=conn.cursor()
            c.execute("select username,pwd from signup")
            rows=c.fetchall()
            flag=0
            for row in rows:
                if(self.uname2==row[0] and self.pwd2==row[1]):
                    flag=1
                    break
                else:
                    flag=0
            if flag==1:
                tk.messagebox.showinfo("Login","Login Successful")
                conn1=sqlite3.connect("users1.db")
                c1=conn1.cursor()
                c1.execute("CREATE TABLE IF NOT EXISTS LoginDetail(username text)")
                c1.execute("INSERT INTO LoginDetail VALUES('"+self.uname2+"')")
                conn1.commit()
                conn1.close()
                self.login_field.delete(0,'end')
                self.pwd_field.delete(0,'end')
                self.login_field.focus()
                cont.show_frame(AfterUserLoginPage)
            else:
                tk.messagebox.showinfo("Error","Invalid Credentials")
                self.login_field.delete(0,'end')
                self.pwd_field.delete(0,'end')
                self.login_field.focus()'''
app=HomePage()
app.title("Employee Recommendation Engine")
app.geometry("1150x700")
app.resizable(0,0)
app.mainloop()