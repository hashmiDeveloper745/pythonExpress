# Python Database Programming.

import sys
import mysql.connector

try:
  getHost = "localhost"
  getUsername = "developerfarazhashmi"
  getPassword = "Jk*%43qAsXtU"
  getDatabase = "testPython"
  getAuthPlugin='mysql_native_password'
  connectDB = mysql.connector.connect(host = getHost,user = getUsername,passwd = getPassword)#, database = getDatabase, auth_plugin = getAuthPlugin)
  dbCursor = connectDB.cursor()
  dbCursor.execute("show databases;");
  res = dbCursor.fetchall();
  for result in res:
    print(result);
except:
  print(str(sys.exc_info()[1]))
finally:
  exit()

