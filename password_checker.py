import sys

MASTER_PASSWORD = "opensessame";

password=input("Enter the password: ");
attempt =1;
while password != MASTER_PASSWORD:
    if attempt > 2:
        sys.exit("Too many invalid password attempts");
    password=input("Try again " );
    attempt +=1;
print("Welcome to Ali Baba's secret Treasure cave!!!");