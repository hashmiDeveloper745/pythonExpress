import mysql.connector
import sys

try:
	DbHost = "localhost"
	DbUser = "developerfarazhashmi"
	DbPass = "Jk*%43qAsXtU"
	dB = "pythonExpress"
	query = "create database " + dB + ";"
#	print(query) # Check Qurey is correct.
	getConnection = mysql.connector.connect(host = DbHost, username = DbUser, password = DbPass)#, database = dB)
	if getConnection:
		print("Connection Successfull")
		getCur = getConnection.cursor()
		getCur.execute(query)
except:
	print(str(sys.exc_info()[1]))