#!/usr/bin/env python

## hw:7.2
## Iftekhar Chowdhury

db = "C:\Users\Iftekhar Chowdhury\Desktop\Python\Homework\hw7\student_db.txt"

elist = [x.split(':')[:1] for x in open(db).readlines()[1:]]

print elist





