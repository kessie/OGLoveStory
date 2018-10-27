#!/usr/bin/python

class Fraudengine:
   def __init__(self, username, password):
      self.username = username
      self.password = password
      
   
   def CheckFraud(self):
     return "CheckFraud" + self.username
     return "CheckFraud" + self.password

   def Checkgood(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

