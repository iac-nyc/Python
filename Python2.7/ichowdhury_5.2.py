#!/usr/bin/env python

"""Iftekhar Chowdhury
H.W. 5.2"""
# Sorting working  properly.


ff = "C:\Users\Iftekhar Chowdhury\Desktop\Python\F-F_Research_Data_Factors_daily.txt"
fh = open(ff)
line = fh.readlines()
data = line[5:-2]
mydict = {}

for line in data:    
    year = line[0:4]  
    columns = line.split()        
    mkt_rf = float(columns[1])
    if year  not in mydict:
            mydict[year] = 0.0
    mydict[year] = mydict[year] + mkt_rf        
           
while True:
    
    user_input = int(raw_input("please enter number of results desired: "))
            
    direction = raw_input("Select 'top' or 'bottom' results: ")  
        
    if  direction == 'top':
        this_reverse = True
    else:
        this_reverse = False
    if user_input > len(mydict):        
               exit("Wrong! Number of result you requested is greater than Dict")
    else:
        break
     
sorted_keys = sorted(mydict,key = mydict.get,reverse = this_reverse)
 
for key in sorted_keys:
    
    print "{} : {}".format(key,mydict[key])
    
 
