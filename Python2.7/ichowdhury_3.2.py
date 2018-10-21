""" Name: Iftekhar Chowdhury
    Date: Nov 10, 2015
    HW  : 3.2       """

#filename = 'C:\Users\Iftekhar Chowdhury\Desktop\sawyer.txt'

name = raw_input("Please enter a file name:")
filename = "C:/Users/Iftekhar Chowdhury/Desktop/"+ name
fh = open(filename)

text = fh.read()
new_text = len(text)
str_text = str(new_text)


lines = text.splitlines()
new_lines = len(lines)
str_lines = str(new_lines)


words = text.split()
new_words = len(words)
str_words = str(new_words)


print str_lines.rjust(8), str_words.rjust(8), str_text.rjust(8), filename
