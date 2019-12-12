#/usr/bin/python
# functions.py
import datetime
import platform
import os
class functions:
  dicts = {1,2,4,5,6,7,8,9,0}
  def __init__():
    print("Hello")
def userInput():
  someText = str(input("Enter any text string: "))
  return someText
def todayTheDateIs():
  getDate = (datetime.datetime(2019,2,14))
  makeText = (str(platform.system())+": "+str(getDate.strftime("%A, %B - %d - %Y")))
  return makeText
def getTheYear():
  getDate = datetime.datetime(2019,1,1)
  fetchYear = getDate
  return (fetchYear)
def letsRead(fileName):
  getFile = str(fileName)
  q = open(getFile,"rt")
  print(q.read())
def letsWrite(fieName):
  getFile = str(fieName)
  p = open(getFile,"w")
def letsUpdate(fileName):
  getFile = str(fileName)
  y = open(getFile,"a")
def letsCreateFile(fileName, exte):
  getFile = str(fileName)
  getExtension = str(exte)
  n = open(getFile+getExtension,"x")
def removeIt(fileName):
  getFile = str(fileName)
  os.path.exists(getFile)

