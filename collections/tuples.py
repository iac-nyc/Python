course_minutes={"Python": 323, "Django": 355,"JavaScript":599}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))
    
####    
    
alphabet = enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for index, letters in alphabet:
    print("{}: {}".format(index+1,letters))
    
#####    
def stringcases(my_string):
    return (my_string.upper(), my_string.lower(), my_string.title(), my_string[::-1])
print(stringcases("iftekhar ahmad chowdhury"))


###
def combo(iter1, iter2):
    output = []
    for i in range(0, len(iter1)):
        output += (iter1[i], iter2[i]),
    return output
print(combo([1, 2, 3], 'abc'))
    
    
    