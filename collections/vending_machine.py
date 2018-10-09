sodas=['Pepsi','Coke','Sprite']
chips=['Doritos','Fritos']
candy=['Snickers','m&m','Twizzlers']

while True:
    choice=input('Would you like Soda, Chips or Candy  >').lower()
    try:
        if choice == 'sodas':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()             
        elif choice == 'candy':
            snack = candi.pop()
        else:
            print("Sorry, didn't understand that") 
            continue
    except IndexError:
            print("We're all out of {}!".format(choice))
    else:
        print("Here is your {}: {}".format(choice,snack))
               
                