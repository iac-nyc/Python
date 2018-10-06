def display_wishlist(display_name, wishes):
    items = wishes.copy()
    print(display_name + ":")
    suggested_gift = items.pop(0)
    print("====>", suggested_gift, "<=====") 
    # Return a slice of the list from the 2nd element on...
    for item in items:
        print("* " + item)
    print()
    
    
books= [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

games = [
    "hadodo",
    "cricket",
    "footbal"
]

##print("Books: ")
##for book in books:
   ## print("*" + book)
    
display_wishlist("Books",books)  
display_wishlist("Games",games)
display_wishlist("Games",games)
    
    
    
    
    
    
    