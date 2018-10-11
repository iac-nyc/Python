#Name: Iftekhar Chowdhury
#Date: Nov 10, 2015
#HW  : 3.1

while True:
    
    input = raw_input("Please enter 4 digit number: ")
    
    if input.isdigit() and len(input) == 4:
        break
    else:
        print "Sorry, '{}' is not a valid number.".format(input)
    

this_sum = 0

count = 0

filename = 'c:\users\Iftekhar Chowdhury\Desktop\FF_abbreviated.txt'

fh = open(filename)

for line in fh:
    
    year = line[0:4]
    
    if year == input:
        
        elements = line.split()
        
        new_value = float(elements[1])
        
        this_sum = float(this_sum + new_value)
        
        count = count + 1
        
        average = this_sum / count        
         
        print 'Counter: {}    Sum : {}    Average: {}'.format(count,this_sum ,average)
          


 
