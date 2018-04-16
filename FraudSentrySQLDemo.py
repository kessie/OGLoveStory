import sqlParser.py
import FrequencyCheck
import MathematicalFunction
import Update
import FrequencyCheck
import Transaction

import MySQLdb
import sqlite3

#database connection 
#conn = sqlite3.

#create database pointer
c = conn.cursor()

c.execute("""CREATE TABLE transactions (
	Location text, Amount int, 
	Pan int, Email varchar, 
	First text, Last text
	)""")

#insert function for singular transaction
def insert_tran(tran):
	with conn:
		c.execute("INSERT INTO transactions VALUES (:Location, :Amount, :Pan, :Email, :First, :Last)", {'Location': tran.Location, 'Amount': tran.Amount, 'Pan': tran.Pan, 'Email': tran.Email, 'First': tran.First, 'Last': tran.Last})


#get transaction from table function
#def get_trans_by_name(lastname):
    #c.execute("SELECT * FROM transactions WHERE Last=:last", {'Last': lastname})
    #return c.fetchall()

#SORT TRANSACTION TABLE FUNCTION DEFINITION, fnc argument could be changed to a user input..No UseriNPUT
def sort_table(tablename):
	with conn:
		c.execute("SELECT * FROM applications ORDER BY Owners ASC")


#UPDATE A PARTICULAR PARAMETER IN A TRANSACTION
def update_tran(tran, Pan):
    with conn:
        c.execute("""UPDATE transactions SET Pan = :pan
                    WHERE First = :first AND Last = :last""",
                  {'first': tran.first, 'last': tran.last, 'pay': pay})

#INSERT SQL DATA SHEET
#use SQL PARSER SCRIPT/ call or SQL_Parser function
SQL_Parser(ExcelDoc, SheetNo)

#CALLING insert_tran FUNCTION ABOVE 
insert_tran(tran_1)

#CALLING SORT TRANSACTION FUNCTION
sort_table(transactions)

#CALLING SEARCH FUNCTION
trans = get_trans_by_name('Doe')
print(trans)

#CALL TO REMOVE A PARTICULAR TRANSACTION
remove_tran(tran_1)

#MATHEMATICAL FUNCTION 

#FREQUENCY SEARCH FUNCTION

#CREATE NEW TRANSACTION
#tran_1 = Transaction(#put transaction parameters)

#CALL TO UPDATE A PARTICULAR TRANSACTION PARAMETER
#update_pay(tran_1, 95000)


conn.close()
