from __future__ import print_function

import os
 
import MySQLdb 


# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "itinventory", use_unicode=True, charset="utf8")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the function to calculate frequency


# Execute sql Query's
cursor.execute(query)
	
# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

#calculate frequency and assign frequency and put frequency in its position
#Check the excel sheet records against database entries and if entries are similar count frequency and add to 
# Import `os` 
#import os

# Retrieve current working directory (`cwd`)
#cwd = os.getcwd()
#cwd

# Change directory 
#os.chdir("/path/to/your/folder")

# List all files and directories in current directory
#os.listdir('.')