#!/usr/bin/env python

student = "C:\Users\Iftekhar Chowdhury\Desktop\Python\student_db.txt"

mydict = {}


for line in open(student).readlines()[1:]:
  
    id,address,city,state,zip = line.split(':')
    
    mystr = "\nid #:  {}\nAddress: {}\nCity: {}\nState: {}\nZip: {}".format(id,address,city,state,zip)
    
    mydict[id] = mystr
    
    

while True:
    
    user_input = raw_input('Please enter an id (" q " for quit ) : ')
    
    if user_input == 'q':
        
        break
    
    if user_input  in mydict:
        
        print 'The address for : "{}" is :{}'.format(user_input,mydict[user_input])
        
    else:
        
         print 'This id:  "{}" does not exist'.format(user_input)
 
 

