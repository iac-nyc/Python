number = int(input("Please enter a number: "))


# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************

if number % 3 == 0 and number % 5 == 0:
    print(number ," is a FizzBuzz number.")
elif number % 3== 0:
          print(number, " is a Fizz number")
elif number % 5==0:
    print(number, "is a Buzzy number")
else:
    print(number, "is neither a fizzy or a buzzy number")




















