# Name : Iftekhar Chowdhury
# Date : Oct 31, 2015
# Homework 2.3
sample_text = """ And since you know how you cannot see yourself,
so well as by reflection, I, your glass,
will modestly discover to yourself,
that of yourself which you yet know not of. """

search_string = raw_input ('Please enter a text to replace:')
new_string = raw_input ('Please enter the replacement text: ')

count = sample_text.count(search_string)
print "{} replacements made".format(count)

new_text = sample_text.replace(search_string, new_string)

print new_text
