# Python Database Programming.

import sys
import mysql.connector

try:
  getHost = "localhost"
  getUsername = "developer"
  getPassword = "uGoUzOREkE58Iv1N"
  connectDB = mysql.connector.connect(host = getHost,user = getUsername,passwd = getPassword)
  print(str(connectDB))
except:
  print(str(sys.exc_info()[1]))
finally:
  exit()

