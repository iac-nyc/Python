# Name : Iftekhar Chowdhury
# Date : Oct 31, 2015
# Homework 2.2

while True:
    input = raw_input("Please enter an integer: ")
    if input.isdigit() and int(input) > 0:
        break
    else:        
        print"Sorry, '{}' is not a valid positive integer".format(input)
        
    
user_input = int(input)
my_sum = 0
count = 0

while count <= user_input:    
    
    print " Count is {} and My Sum is {}".format(count,my_sum)
    print " Total is :{} ".format(my_sum)
    count = count + 1 
    my_sum = my_sum + count
   
  
    
    
   

   
                    

