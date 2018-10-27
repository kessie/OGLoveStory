import pandas as pd
import csv
excel_file = 'transactions.xlsx'
transactions = pd.read_excel(excel_file)
#Print function below checks to see if all data from the excel sheet is gotten
#print transactions
#frequency = [cust_email.fetchall()]
print transactions['cust_email'].value_counts()
#for col in transactions.columns:
	#transactions['frequency'] = frequency
	#write to new columns in excel sheet

	#counts value of items in column 'cust_name' and return the item name and respective value.
	#print transactions['cust_email'].value_counts()
#with open('storage.csv','wb') as out:
#	csv_out=csv.writer(out)
#csv_out.writerow(['name','num'])
#use this line below instead of for loop from line 18
#	csv_out.writerows(transactions['cust_email'].value_counts())