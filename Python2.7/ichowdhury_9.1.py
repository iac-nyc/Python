#!/usr/bin/env python

""" Iftekhar Chowdhury
    Homework: 9.1
    Date: 12/22/2015 """

class Square(object):
    
  def __init__(self, value):    
         self.value = 2

  def squareme(self):
    self.value = self.value * self.value

  def getme(self):
    return self.value

n1 = Square(2)
n2 = Square(2)
n3 = Square(2)


n1.squareme()
val1 = n1.getme()
print val1


n2.squareme()
n2.squareme()
val2 = n2.getme()
print val2
print n1.getme()

n3.squareme()
n3.squareme()
n3.squareme()
n3.squareme()
n3.squareme()
val3 = n3.getme()
print val3

print n1.getme()
print n2.getme()
print n3.getme()

