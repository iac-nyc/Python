#!/usr/bin/env python

'''
iftekhar chowdhury
h.w. 8.1
'''

import os

for file in os.listdir('C:/Users/Iftekhar Chowdhury/Desktop/Python/Homework/hw8/bible'):
    if os.path.isfile(file): 
        file = os.path.join.listdir('.')
        file = open('Acts.txt')
    counter = 0
    for line in file:
        if 'Roman' in file:
            counter = counter + 1
            print "String found in file:  {}  times".format(counter) 
 
