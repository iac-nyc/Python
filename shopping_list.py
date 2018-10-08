# create a new empty list named shopping_list
# create a function named add_to_list that declared a parameter named item
# add the item to the list

shopping_list = []
def add_to_list(item):
    shopping_list.append(item)
    print("Added! List has {} items.".format(len(shopping_list)))
    
def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' to ask for help
    Enter 'SHOW'
    """)
def show_list():
    print("Here is your list: ")
    for item in shopping_list:
        print(item)
    
show_help()
while True:
    new_item = input(">")
    
    if new_item =="DONE":
        break
    elif new_item=="HELP":
        show_help()
        continue
    elif new_item =="SHOW":
        show_list()
        continue
        
        # call add_to_list with a new item
    add_to_list(new_item)
    
    
show_list()    
   