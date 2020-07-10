#/usr/bin/python

# Python Official: https://www.python.org/
# The Python Tutorial: https://docs.python.org/3/tutorial/
# Very First Program Using Python Programming Language.
import functions as fncts
#import ipaddress
import sys
import numpy
class helloWorld:
  def __init__(self):
    self.greeting = "Hello "
#World"
  def greetings(self):
    print(fncts.todayTheDateIs())
    """Hello`
         To
           ALL!"""
    getName = fncts.userInput()
    print(self.greeting+getName)
    print(str(dir(ipaddress)))
  def test(self):
    text = "Python"
    leng = len(text)
    print(text + " = " + str(leng) +" characters.")
  def nextChapter(self):
    #C: Create (Done)
    #U: Update (Done)
    #R: Read (Done)
    #D: Delete (Done)
    print("Continue From: Python MongoDB @ url(https://www.w3schools.com/python/python_mongodb_getstarted.asp).")
    print("How To Install and Set Up a Local Programming Environment for Python 3 @ url(https://www.digitalocean.com/community/tutorial_series/how-to-install-and-set-up-a-local-programming-environment-for-python-3)")

try:
  hW = helloWorld() # Class Hello World Object.
  #hW.greetings() # Class Hello World Method Greetings Called.
  #hW.test() # Another Python CLass Method.
  hW.nextChapter()
except:
  print(sys.exc_info()[1])
finally:
  print("BYE BYE...")
  exit()