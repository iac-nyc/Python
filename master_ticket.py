TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE)+ SERVICE_CHARGE
# Run this code until we run out of tickets
while tickets_remaining >=1 :

        # Output how many tickets are remaining 
        print("There are {} tickets remaining.".format(tickets_remaining));
        
        #Gather user name
        user_name = input("What's your name?  ");
        #Prompt the user by name and ask how many tickets they would like to buy
        # Calculate the price of tickets
        number_of_ticket = input("{}, how many ticket's would like to buy? ".format(user_name));
        try:
            number_of_ticket= int(number_of_ticket)
            # Raise a ValueError if request is higer than available tickets
            if number_of_ticket > tickets_remaining:
                raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
        except ValueError as err:
            # Include a error text output
            print("Oh no, we ran into an issue. {}. Please try again!".format(err))
        else:    
            price = calculate_price(number_of_ticket)
            
            print("{}, total cost of the tickets will be ${}.".format(user_name, price));
            
            #Prompt user if they want to proceed. Y/N?
            should_proceed = input("Do you want to proceed? Y/N  ")
            
            # If they want to proceed
            if should_proceed.lower() == "y":
                # print out to the screen "SOLD!" to confirm purchase
                #TODO: Gather Credit card info and process
                print("SOLD!")
                # and then decrement the tickets remaining by the number of tickets purchased
                tickets_remaining = (tickets_remaining - number_of_ticket)
            # Otherwise ..
                # Thank them by name
                
            else:
                print("Thank you anyways, {}!".format(user_name))
# Notify the user tickets are sold out
print("Sorry, all tickets are sold out !")
        
