import MySQLdb
import MySQLdb as sql

# Establish a MySQL connection OR remove and use "with conn:" as seen in SQLDemo script, followed by all query and the rest of the code below
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "itinventory", use_unicode=True, charset="utf8")
Get_row_length = database.cursor()
Get_table_columns = database.cursor()
Get_table_columns2 = database.cursor()
Quertcreatetable = database.cursor()
Querygettablename = database.cursor()
Querygettablecolumns = database.cursor()

#Queries for the database
Qquery = Get_row_length.execute("SELECT COUNT(*) AS total_table FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'transactions'")
Qquery2 = Get_table_columns.execute("SHOW COLUMNS FROM transactions") #Query for the list of column headers
Qquery3 = Get_table_columns2.execute("SHOW COLUMNS FROM transactions") #important for the loop
Quertcreatetablefreq = Quertcreatetable.execute("CREATE TABLE Freq_Table ( SN int)") #Query for the list of column headers
Qqueryoutput = Querygettablename.execute("show tables like 'freq_table'") #Query for the list of column headers




def Createnewtable( database, Row_list, Value_list, table, frequency ):
   Create_a_new_table1 = database.cursor()
   Create_a_new_table2 = database.cursor()
   Create_a_new_table3 = database.cursor()
   Create_a_new_table4 = database.cursor()
   Create_a_new_table5 = database.cursor()

   global Values 
   values = [] 
   #for i in range (0,len(Row_list)):
   	#   if Row_list[i] is None:
   	 #  	  Row_list = ""
   	  # 	  print Row_list[i]

#   	   elif Value_list[i] == None:
 #  	   	   Value_list[i]= ["",""]
  # 	   	   print Value_list[i][0]
   #	   	   print Value_list[i][1]
   	#   else:
   	 #  	   print Row_list[i]
   	  # 	   print Value_list[i][0]
   	   #	   print Value_list[i][1]
   print "=============" 
   print Value_list
   #print len(Row_list)

   columns_declaration = ', '.join('%s' % c for c in Row_list)
   print columns_declaration

   for i in Row_list:
	if i == Row_list[0]:
		Create_a_new_table3.execute("DROP TABLE IF EXISTS %s" % table)
		Create_a_new_table3.execute("CREATE TABLE %s" % table + "(%s varchar(255))" % i)
	else:
		Create_a_new_table3.execute("ALTER TABLE %s ADD COLUMN (%s varchar(255))" % (table,i))
    

  # for i in Value_list:
   #	if Value_list[[i][0]] == ('','' ):
   		#i =  ["empty","empty"]
   		#for row in i:
   			#print row
   	#else:
   		#print row
   
   		#Value_list[i] = [""]
        #count = len(i)
        #question_marks = []
   #while a < count:
       #question_marks.append('%s')
       #a += 1
   #quests = ','.join(question_marks)
   #cur.executemany("INSERT INTO Freq_Table VALUES(%s)" % quests, Value_list)
   


   	
   #QueryCrt3 = Create_a_new_table3.execute("DROP TABLE IF EXISTS %s" % table)
   
   #QueryCrt4 = Create_a_new_table4.execute("CREATE TABLE Freq_Table (%s)" % (columns_declaration))


   #QueryCrt4 = Create_a_new_table4.execute("ALTER TABLE %s ADD column %s int" % (table, frequency))
   #insert = ("INSERT INTO %s" % table + "(%s, %s)" % (col_name, frequency) + " VALUES (%s, %s)" )

   #QueryCrt5 = Create_a_new_table5.execute(insert, (col_val, frequencynum))
   database.commit()
   return

 
def Appendtotable( database, Row_list, Value_list, table, frequency):
   Create_a_new_table1 = database.cursor()
   Create_a_new_table2 = database.cursor()
   Create_a_new_table3 = database.cursor()
   Create_a_new_table4 = database.cursor()
   Create_a_new_table5 = database.cursor()
   #QueryCrt1 = Create_a_new_table1.execute("ALTER TABLE %s DROP COLUMN SN" % (table))
   #insert = ("INSERT INTO %s" % table + "(%s, %s)" % (col_name, frequency) + " VALUES (%s, %s)" )
   QueryCrt5 = Create_a_new_table5.execute(insert, (col_val, frequencynum))
   database.commit()
   return

print Get_table_columns.fetchone()[0]


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

for names in Get_table_columns2:
	print names[0]

#Get the value of the length of row and convert to an integer 
StringValue = str(Get_row_length.fetchone()[0])
Column_length = int(StringValue)
print Column_length

#Get the column names into a list 
columns_name = [];
for column_name in Querygettablename:
	#print (column_name)[0]
	columns_name.append((column_name)[0]);




for i in range (0,Row_length):
	global Row_list
	global Value_list
	Row_list = []
	Value_list = []
	for names in Get_table_columns2:
		ColumnStringVal = str(names[0])
		#print "here"
		#print ColumnStringVal
#SQL Query which checks for frequency of all colums in db
	#for i in (0,Column_length):
		SQL_Freq = """SELECT 
						%s, COUNT(%s)
            FROM
						transactions
           			GROUP BY 
           				%s
           			HAVING COUNT(%s) ;""" % (ColumnStringVal,ColumnStringVal,ColumnStringVal,ColumnStringVal)

		execute_SQL_Freq = database.cursor()
		execute_SQL_Freq.execute(SQL_Freq)
		Value_list.append(execute_SQL_Freq.fetchone())
		print (ColumnStringVal)
		Row_list.append(ColumnStringVal)
		Row_list.append("frequency"+ ColumnStringVal)
		#print Row_list
		#print Value_list
	
	#global check
	#check = 0
		#for row in Value_list:
		#	print (row)[0] # value 
		#	print (row)[1] # frequency
		#	Value_list.append((row)[0])
		#	Value_list.append((row)[1])
	if i > 0:
		
		Appendtotable( database = database, Row_list = Row_list, Value_list = Value_list, table = column_name[0], frequency = "frequency" + ColumnStringVal );
	else:
		Createnewtable( database = database, Row_list = Row_list, Value_list = Value_list, table = column_name[0], frequency = "frequency" + ColumnStringVal );
	






#def a fuction to create a table 
