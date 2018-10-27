#ITERATE OVER ALL COLUMNS IN DB TEST
#database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "itinventory", use_unicode=True, charset="utf8")
#cursorRR = database.cursor()
#request = """SELECT * FROM ' + TABLE_SCHEMA + '.[' + transactions + ']' + CHAR(13)
# INFORMATION_SCHEMA.TABLES"""
#number_of_cols = cursorRR.execute(request)

#result = cursorRR.fetchall()
#for column in result.T:
#	print column

import MySQLdb 

#define inputs
#arg1 = input()
#arg2 = input()

#Function which calls SQL_freq query
#def ColumnFreq():
# Establish a MySQL connection OR remove and use "with conn:" as seen in SQLDemo script, followed by all query and the rest of the code below
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "itinventory", use_unicode=True, charset="utf8")

"""cursor = database.cursor()
#Query for length of database columns
Qquery = cursor.execute("SELECT COUNT(*) AS total_table FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'transactions'")"""
########################################################
Ccursor = database.cursor()
QQquery = Ccursor.execute("SELECT * FROM transactions")
data = str(Ccursor.fetchall())
#data = Ccursor.fetchall()
for i in data:
	#print data
 	wordlist = data.split()
 	wordfreq = []
 	for w in wordlist:
 		wordfreq.append(wordlist.count(w))
		print("Frequencies\n" + str(wordfreq) + "\n")
	#SQL_Freq = """SELECT 
					#card_last4, COUNT(card_last4)
		  		#FROM
					#transactions
               	#GROUP BY 
               		#card_last4
             	#HAVING COUNT(card_last4);
	#while i< len(data):
		#pass
######################################################
"""x = str(cursor.fetchone()[0])
k = int(x)
print k
#for i in query
#SQL Query which checks for frequency of all colums in db
i = 1
while i <= k:"""
	
	#SQL_Freq = """SELECT 
					#card_last4, COUNT(card_last4)
		  		#FROM
					#transactions
               	#GROUP BY 
               		#card_last4
             	#HAVING COUNT(card_last4);"""

# Get the cursor, which is used to traverse the database, line by line
	#cursorR = database.cursor()
	#Create for loop which loops over the number of columns in the database
	#for r in range (k):
		# Execute sql Query's
		#cursorR.execute(SQL_Freq)
	
# query = select * from transactions
# cursorRRR = database.cursor()
#cursor.execute(query)
# for a in 
# m = 0
# for m in range (cursorRRR)

#for m in length 
#	query2 = select


#	for m in :
#		j = str((row)[0])