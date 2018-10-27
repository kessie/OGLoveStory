import MySQLdb
import MySQLdb as sql
import pandas as pd
import sys
#formatting import
from itertools import izip_longest

# Establish a MySQL connection OR remove and use "with conn:" as seen in SQLDemo script, followed by all query and the rest of the code below
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "itinventory", use_unicode=True, charset="utf8")
Get_row_length = database.cursor()
Get_table_columns = database.cursor()
Get_table_columns2 = database.cursor()
Quertcreatetable = database.cursor()
Querygettablename = database.cursor()
Querygettablecolumns = database.cursor()

#Queries for database
Qquery = Get_row_length.execute("SELECT COUNT(*) AS total_table FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'transactions'")
Qquery2 = Get_table_columns.execute("SHOW COLUMNS FROM transactions") #Query for the list of column headers
Qquery3 = Get_table_columns2.execute("SHOW COLUMNS FROM transactions") #important for the loop
Qqueryoutput = Querygettablename.execute("show tables like 'freq_table'") #Query for the list of column headers
#Get the length of the database
SQL_Row_len = """SELECT 
					%s, COUNT(%s)
	  			FROM
					transactions
           		GROUP BY 
           			%s
           		HAVING COUNT(%s) ;""" % (Get_table_columns.fetchone()[0],Get_table_columns.fetchone()[0],Get_table_columns.fetchone()[0],Get_table_columns.fetchone()[0])

execute_SQL_Row_len = database.cursor()
execute_SQL_Row_len.execute(SQL_Row_len)
Row_length = int(str(len(execute_SQL_Row_len.fetchall())))
print Row_length

#Get the value of the length of row and convert to an integer 
StringValue = str(Get_row_length.fetchone()[0])
Column_length = int(StringValue)
print Column_length

#Get the column names into a list 
#columns_name = [];
#columns_name = str(Qquery2.fetchone()[0])
for column_name in Querygettablename:
	#print (column_name)[0]
	columns_name.append((column_name)[0]);



#create table cursor
for i in range (0,Row_length):
	global Row_list
	global Value_list
	Row_list = []
	Value_list = []
	for names in Get_table_columns2:
		ColumnStringVal = str(names[0])
		#create and write to new database
		#SQL_TABLE = """CREATE TABLE faff;"""
		#CreateTable.execute(SQL_TABLE)
		#print "here"
		#print ColumnStringVal
#SQL Query which checks for frequency of all colums in db
	#for i in (0,Column_length):
		SQL_Freq = """SELECT 
						%s, COUNT(%s)
					AS
						frequency
	  				FROM
						transactions
           			GROUP BY 
           				%s
           			HAVING COUNT(%s) >0;""" % (ColumnStringVal,ColumnStringVal,ColumnStringVal,ColumnStringVal)

		execute_SQL_Freq = database.cursor()
		execute_SQL_Freq.execute(SQL_Freq)
		#write each frequency to new table
		Value_list.append(execute_SQL_Freq.fetchone())
		#print (ColumnStringVal)
		Row_list.append(ColumnStringVal)
		Row_list.append("frequency"+ ColumnStringVal)

#print Row_list #list of column names
#print Value_list #column values and frequency count
#format valuelist output
#FValueList =[v for v in izip_longest(*[k.split('\n') for k in Value_list])]
#print FValueList
#print column_name
#print columns_name