#database connection
import MySQLdb 
 
database = MySQLdb.connect(host="127.0.0.1",
user="root",
passwd="",
db="itinventory"
)

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

#columnName = UserArg
#weight scale function{length of the column + x} ; you can change the parameterto user input
def WeightScale (columnName):
	ColumnLength = COL_LENGTH ('tablename' , 'columnName')
	weightScale = columnLength + 1 
	print weightscale
	return weightscale;

#weight value for each column should be a big function with smaller functions
def FreqSum(ColumnNameFreq):
	SumNumber = 0
	for item in ColumnNameFreq:
		#find the sum of all frquencies in that column{Denominator}
		SumQuery = "SELECT SUM(ColumnNameFreq) FROM applications;"
		cursor.execute(SumQuery)
		SumNumber += item
		print SumNumber
		database.commit()
		database.close()
	
	return SumNumber;

def ParamFreq(ParamInQuestion):
	#find the frequency value of the particular transaction parameterand make it Numerator of formula
	for ParamInQuestion in NameOfColumn:
		#find the corresponding frequency value
		#print the frequency value
		return;

#Call WeightScale function	
WeightScale(colname)

 
#Sum of value(freq) of the column

#Frequency of i in column Numerator{the current parameter we are calcuating}