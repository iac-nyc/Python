print("A")
try:
    result = "test" + 5
    print("B")
except ValueError:
    print("C")
except TypeError:
    print("D")
else:
    print("E")
print("F")


#############
def suggest(product_idea):
    result=len(product_idea)
    if result <= 3:
        raise ValueError("The idea should be more than 3 charcters long");
    return product_idea + "inator"