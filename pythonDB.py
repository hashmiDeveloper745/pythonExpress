# Python Database Programming.

import sys
import mysql.connector

try:
  getHost = "localhost"
  getUsername = "developerfarazhashmi"
  getPassword = "Jk*%43qAsXtU"
  getDatabase = "pythonExpress"
  getAuthPlugin='mysql_native_password'
  connectDB = mysql.connector.connect(host= getHost,username = getUsername, password = getPassword, database = getDatabase)
  DBCursor = connectDB.cursor()
  sqlQuery = "show tables;"
  DBCursor.execute(sqlQuery)
  result = DBCursor.fetchall()
  if len(result) == 0:
    print("There are no tables found!")
  else:
    for res in result:
      print(res)
except:
  print(str(sys.exc_info()[1]))
finally:
  exit()

