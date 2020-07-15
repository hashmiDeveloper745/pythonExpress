import mysql.connector
import sys
""" 
Insert Example
"""
getH = "localhost"
getU = "developerfarazhashmi"
getP = "Jk*%43qAsXtU"
getDB = "pythonExpress"
try:
	connectDB = mysql.connector.connect(host = getH, username = getU, password = getP, database = getDB);
	if connectDB:
		writingCursor = connectDB.cursor()
		query = "show tables;"
		writingCursor.execute(query)
		getTables = writingCursor.fetchall()
		for tables in getTables:
			print(tables)
except:
	errorStatement = "Error Occur: "+str(sys.exc_info()[1])+"."
	print(errorStatement)
