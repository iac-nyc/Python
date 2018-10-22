#!/usr/bin/env python

while True:
    year_input = raw_input("Please select a year: ")
    
    if year_input.isdigit and len(year_input) == 4:
        
        break
    
    else:
        print "Sorry, '{}' is not a valid year.".format(year_input)
     
   
filename = "C:/Users/Iftekhar Chowdhury/Desktop/Python/F-F_Research_Data_Factors_daily.txt"

fh = open(filename)

wanted_lines = fh.readlines()

data = wanted_lines[5:-2]

factor_list = []

for line in data:
    
    year = line[0:4]
    
    if year == year_input:
        
        columns = line.split()
        
        mkt_rf = float(columns[1])
        
        factor_list.append(mkt_rf)
        
        for mkt_rf in data:
            if 'mkt-rf' not in factor_list:
               
                average =  sum(factor_list)/ len(factor_list)
                median_index = len(factor_list)/2.0
                
print  "{} (mkt-rf) : Average  {}  Values  {} and Median Value {} ".format(year_input, average,  len(factor_list), median_index)        
    
