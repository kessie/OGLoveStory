import xlrd
import MySQLdb

#specify location of xlsx file
#file_location = "C:/Users/DELL/Desktop/Python/ITInventory.xlsx"
# Open the workbook and define the worksheet
def SQL_Parser(ExcelDoc, SheetNo):

	book = xlrd.open_workbook("ExcelDoc")
	sheet = book.sheet_by_name("SheetNo")

	# Establish a MySQL connection OR remove and use "with conn:" as seen in SQLDemo script, followed by all query and the rest of the code below
	database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "itinventory", use_unicode=True, charset="utf8")

	# Get the cursor, which is used to traverse the database, line by line
	cursor = database.cursor()

	# Create the INSERT INTO sql query
	query = """INSERT INTO applications (Business_Applications, Application_Name, Description, Owners) VALUES (%s, %s, %s, %s)"""


	# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
	for r in range(2, sheet.nrows):
		BusinessApplication = sheet.cell(r,1).value#change the column number back to zero and seewhat the php database says
		ApplicationName = sheet.cell(r,2).value
		Description = sheet.cell(r,3).value
		Owners = sheet.cell(r,4).value
		# Assign values from each row
		values = (BusinessApplication, ApplicationName, Description, Owners)
		
		# Execute sql Query's
		cursor.execute(query, values)

	# Close the cursor
	cursor.close()

	# Commit the transaction
	database.commit()

	# Close the database connection
	database.close()

	# Print results
	print ""
	print "All Done! Bye, for now." #Check to see if the code actually runs till the end
	print ""
	columns = str(sheet.ncols)
	rows = str(sheet.nrows)
	#print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!"
	return