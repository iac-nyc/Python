import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check");
    return math.ceil(total / number_of_people);


try:
    total_due = float(input("What's the total?  "));
    number_of_people = int(input("How many people? "));
    amount_due = split_check(total_due,number_of_people);
except ValueError as err:
    print("Please enter a valid value");
    print("({})".format(err));
else:
    print("Each person owes ${}".format(amount_due));