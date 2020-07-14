import mysql.connector
import sys

try:
	DbHost = "localhost"
	DbUser = "developerfarazhashmi"
	DbPass = "Jk*%43qAsXtU"
	dB = "pythonExpress"
	connect = mysql.connector.connect(host = DbHost, username = DbUser, password = DbPass)
	if connect:
	  print("Connection successfull");
	  connectCursor = connect.cursor()
	  connectCursor.execute("create database "+dB+";")
	else:
		print("Database connection error occur.")
except:
	print(str(sys.exc_info()[1]))