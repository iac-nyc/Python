
# kwargs = key word arguments
def packer(name=None, **kwargs):
    print(kwargs)
    
    
def unpacker(first_name=None,last_name=None):
    if first_name and last_name:
        print("Hi {} {}".format(first_name,last_name))
    else:
        print("Hi no name!")
    
    
packer(name="iftekhar",num=99, spanish_inquisition=None)
unpacker(**{"last_name": "Chowdhury", "first_name":"Iftekhar"})

def favorite_food(dict):
    return "Hi, I'm {name} and I love to eat {food}!".format()

def unpacker(name=None,food=None):
    if name and food:
        print("Hi, I'm {} and I love to eat {}!".format(name,food))
    else:
        print("Hi no name!")
unpacker(**{"name": "Kenneth", "food":"tacos"})