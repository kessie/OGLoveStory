#write frequency to database.
import MySQLdb 

#define inputs
#arg1 = input()
#arg2 = input()

#Function which calls SQL_freq query
#def ColumnFreq():
# Establish a MySQL connection OR remove and use "with conn:" as seen in SQLDemo script, followed by all query and the rest of the code below
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "itinventory", use_unicode=True, charset="utf8")

cursor = database.cursor()
cursor2 = database.cursor()
	#Query for length of database columns
Qquery = cursor.execute("SELECT COUNT(*) AS total_table FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'transactions'")

Qquery2 = cursor2.execute("SHOW COLUMNS FROM transactions")

columns = [];
for l in cursor2:
	#print (l)[0]
	columns.append((l)[0]);

#print columns[0]
#print cursor2.fetchone()[0]

x = str(cursor.fetchone()[0])
k = int(x)
#print k

for t in cursor2:
	#print str(t[0])
	w = str(t[0])
#SQL Query which checks for frequency of all colums in db
	for i in (0,k):
		#print w
		SQL_Freq = """SELECT 
						%s, COUNT(%s)
					AS 
					Frequency
		  			FROM
						transactions
               		GROUP BY 
               			%s
             		HAVING COUNT(%s) ;""" % (w,w,w,w)
        #print SQL_Freq
#"""SELECT ValA FROM `%s` WHERE Val2 = '%s' AND Val3 = '%s'""" 
#SELECT cust_name, COUNT(cust_name)AS Frequency FROM transactions GROUP BY cust_name ORDER BY COUNT(cust_name) DESC
# Get the cursor, which is used to traverse the database, line by line
	cursorR = database.cursor()
	#Create for loop which loops over the number of columns in the database
	#for r in range (k):
		# Execute sql Query's
	cursorR.execute(SQL_Freq)
	#print w #name of the column
	#print SQL_Freq

	for row in cursorR:

		print (row)[0] # value
		print (row)[1] # frequency
		
		#print (row)[1] # frequency
		#print cursorR.fetchall()[0:55]

#TO DO: format fetchall output
#		write output into a bigger database.
		# Close the cursor
		#cursorR.close()

		# Commit the transaction
		#database.commit()

		# Close the database connection
		#database.close()
	#print function output


	#return

#Function call
#ColumnFreq(arg1, arg2);