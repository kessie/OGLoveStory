from __future__ import print_function
 
import MySQLdb 
 
database = MySQLdb.connect(host="localhost",
user="root",
passwd="",
db="itinventory"
)
 
cursor = database.cursor()
 
# Add frequency columns for each column...
sql = """SELECT Description, COUNT(Description)#cust_email, COUNT(cust_email), cust_tel, COUNT(cust_tel),charge_amount, COUNT(charge_amount),charge_currency, COUNT(charge_currency), originating_ip_address, COUNT(originating_ip_address),device_fingerprint, COUNT(device_fingerprint), medium, COUNT(medium), card_brand, COUNT(card_brand), card_first6, COUNT(card_first6), card_last4, COUNT(card_last4),
	#account_number, COUNT(account_number),
	#		bank_code, COUNT(bank_code),
	#		merchant_transaction_ref, COUNT(merchant_transaction_ref),
	#		narration, COUNT(narration),
	#		auth_model, COUNT(auth_model),
	#		merchant_id, COUNT(merchant_id),
	#		advice, COUNT(advice),
	#		deleted_at, COUNT(deleted_at),
	#		created_at, COUNT(created_at),
	#		updated_at, COUNT(updated_at),
	#		status, COUNT(status),
	#		is_fraudulent, COUNT(is_fraudulent),
	#		timezone, COUNT(timezone),
	#		expiry, COUNT(expiry)
	   FROM 
	   		applications
	   GROUP BY
	   		Description 
	#		cust_email, 
	#		cust_tel, 
	#		charge_amount, 
	#		charge_currency, 
	#		originating_ip_address, 
	#		device_fingerprint, 
	#		medium, 
	#		card_brand, 
	#		card_first6, 
	#		card_last4, 
	#		account_number, 
	#		bank_code, 
	#		merchant_transaction_ref, 
	#		narration, 
	#		auth_model, 
	#		merchant_id, 
	#		advice, 
	#		deleted_at, 
	#		created_at, 
	#		updated_at, 
	#		status, 
	#		is_fraudulent, 
	#		timezone, 
	#		expiry
	   HAVING COUNT(Description) > 0
	#		OR COUNT(cust_email) > 0
	#		OR COUNT(cust_tel) > 0
	#		OR COUNT(charge_amount) > 0
	#		OR COUNT(charge_currency) > 0
	#		OR COUNT(originating_ip_address) > 0
	#		OR COUNT(device_fingerprint) > 0
	#		OR COUNT(medium) > 0
	#		OR COUNT(card_brand) > 0
	#		OR COUNT(card_first6) > 0
	#		OR COUNT(card_last4) > 0
	#		OR COUNT(account_number) > 0
	#		OR COUNT(bank_code) > 0
	#		OR COUNT(merchant_transaction_ref) > 0
	#		OR COUNT(narration) > 0
	#		OR COUNT(auth_model) > 0
	#		OR COUNT(merchant_id) > 0
	#		OR COUNT(advice) > 0
	#		OR COUNT(deleted_at) > 0
	#		OR COUNT(created_at) > 0
	#		OR COUNT(updated_at) > 0
	#		OR COUNT(status) > 0
	#		OR COUNT(is_fraudulent) > 0
	#		OR COUNT(timezone) > 0
	#		OR COUNT(expiry) > 0
			;"""

#sql = "insert into applications VALUES('%s', '%d', '%s', %d, '%s', '%d', '%s', '%d')" % \
 #(Business_Applications, BusAppFreq, Application_Name, AppNameFreq, Description, DescFreq, Owners, OwnersFreq)
 
cursor.execute(sql)
database.commit()
 
database.close()