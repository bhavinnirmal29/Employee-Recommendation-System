import os
import PyPDF2
import re
import statistics
from nltk.tokenize import sent_tokenize,word_tokenize
import sqlite3
temp2="bhavinnirmal29@gmail.com"
temp1="str1"
temp3="str3"
conn=sqlite3.connect("users1.db")
c=conn.cursor()
c.execute("drop table demotable")
conn.commit()