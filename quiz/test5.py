
    def first_4(iterable):
    return iterable[0:4]

print(first_4([66, 333, 222, 1, 1234]))

def first_and_last_4(iterable):
    #return iterable[:4] + iterable[-4:len(iterable):1]
    return iterable[:4] + iterable[-4::1]
print(first_and_last_4([1, 2, 3, 4, 100,0,-4,-3,-2,-1]))

def odds(num):
    return num[1::2]
print(odds([1,2,3,4,5]));

def reverse_evens(iterable):
    #return iterable[-1: :-2]
    return iterable[::2][::-1]
print(reverse_evens([1,2,3,4,5]))

def sillycase(string):
    half = round(len(string)/2)
    return string[:half].lower() + string[half:].upper()
print(sillycase("treehouse"))
    
    
    
    
test_dict = {"a": 1, "b": 2, "a": 3}
print(test_dict["a"])