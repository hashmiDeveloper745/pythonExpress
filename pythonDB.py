# Python Database Programming.

# Python
# C = Create
# U = Update
# R = Read
# D = Delete

import sys
import mysql.connector
getHost = "localhost"
getUsername = "developerfarazhashmi"
getPassword = "Jk*%43qAsXtU"
getDatabase = "pythonExpress"
getAuthPlugin='mysql_native_password'
def connectDatabase():
  try:
    connectDB = mysql.connector.connect(host= getHost,username = getUsername, password = getPassword, database = getDatabase)
    return connectDB
  except:
    print(str(sys.exc_info()[1]))
def createDatabase(DBN):
  try:
    getDatabaseConnection = connectDatabase()
    getCursor = getDatabaseConnection.cursor()
    query = "create database "+DBN+";"
    getCursor.execute(query)
    print("Database "+DBN+" created successfully")
  except:
    print("Error: "+str(sys.exc_info()[1]))
def createTable(TableName):
  try:
    getCon = connectDatabase()
    cur = getCon.cursor()
    query = "create table "+TableName+";"
    cur.execute(query)
    print("Table "+TableName+" has been created successfully.")
  except:
    print("Error: "+str(sys.exc_info()[1]))
def showDatabase():
  try:
    getDatabaseConnection = connectDatabase()
    getCursor = getDatabaseConnection.cursor()
    query = "show databases;"
    getCursor.execute(query)
    databasList = getCursor.fetchall()
    for dbs in databasList:
      print("Database: "+str(dbs)+";")
  except:
    print("Error: "+str(sys.exc_info()[1]))
def showTables(dbs):
  try:
    getDatabaseConnection = connectDatabase()
    getCursor = getDatabaseConnection.cursor()
    query = "use "+dbs+";"
    getCursor.execute(query)
    query = "show tables"
    getCursor.execute(query)
    databasList = getCursor.fetchall()
    for dbs in databasList:
      print("Database: "+str(dbs)+";")
  except:
    print("Error: "+str(sys.exc_info()[1]))
  