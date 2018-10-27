import MySQLdb
import MySQLdb as sql
import pandas as pd
import sys
import WriteToTxtFileThenDB
from WriteToTxtFileThenDB import Row_list
from WriteToTxtFileThenDB import Value_list
import csv

#Establish a MySQL connection OR remove and use "with conn:" as seen in SQLDemo script, followed by all query and the rest of the code below
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "itinventory", use_unicode=True, charset="utf8")

CreateTable = database.cursor()
#Query that Create table that reads each column in table
ReadTable = database.cursor()
SplitString = database.cursor()

print Row_list
for i in Row_list:
	i.join("freq")
print Row_list

#SPLIT ROWLIST VALUES INTO SEPERATE STRINGS
SPLIT_ROWLIST = """SELECT value FROM STRING_SPLIT(Row_list);"""
#SQL Table creating new table
Create_Table = """CREATE TABLE NewTransactions();"""
#Execute Create_Table
#CreateTable.execute(Create_Table)
#SplitString.execute(SPLIT_ROWLIST)
#For each column in db
#Write SQL Freq output to text file then from textfile, write back to new db created
#WRITE Row_list INTO TEXTFILE
with open('storage.csv', 'wb') as csvfile:
	wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	wr.writerow(Row_list)
	for var in enumerate(Value_list):
		print var
	wr.writerow(Value_list)

print Value_list
#newList  = Value_list
#print newList[0][0]

final1,final2,c,d=[],[],[],[]


for i in range(0,len(Value_list)):
    for j in range(0,len(Value_list[i])):
        #for k in range(0,len(cigar[i][j])):
        	#print j
        	final1.append(Value_list[i][j])
print final1
