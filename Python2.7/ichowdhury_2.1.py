# Name : Iftekhar Chowdhury
# Date : Oct 31, 2015
# Homework 2.1

while True:
    input = raw_input("Please enter an integer: ")
    if input.isdigit() and int(input) >0 :
        break
       
    else:
        
        print"Sorry, '{}' is not a valid integer.".format(input)
        
    print "Counting from 1 to 100 by {}'s".format(user_input)    
user_input= int(input)
count = 1

while count<=100:
    count = count + 1
    if count % user_input == 0:
       
        print count

   
                    

