from __future__ import print_function
 
import MySQLdb 
 
database = MySQLdb.connect(host="127.0.0.1",
user="root",
passwd="",
db="itinventory"
)
 
cursor = database.cursor()
 
Business_Applications = "Shellac"
BusAppFreq = 40
Application_Name = "Shellac2"
AppNameFreq = 10008
Description = "Shelling App"
DescFreq  = 12
Owners = "Kess"
OwnersFreq = 4
 
sql = "insert into applications VALUES('%s', '%d', '%s', %d, '%s', '%d', '%s', '%d')" % \
 (Business_Applications, BusAppFreq, Application_Name, AppNameFreq, Description, DescFreq, Owners, OwnersFreq)
 
number_of_rows = cursor.execute(sql)
database.commit()
 
database.close()