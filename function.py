def yell(text):
    text=text.upper();
    number_of_characters=len(text);
    result= text + "!" * (number_of_characters//2);
    print(result);
    
yell("You are doing great");
yell("Keep your code DRY; Don't Repeat Yourself!");
yell("Don't hasitate to ask for help");

#########
def display_blanks( word):
    blanks = "-" * len(word)
    print(blanks)

print("Puzzle 1:")
display_blanks("treehouse")
print("Puzzle 2:")
display_blanks( "python")