def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(multiply(3,10,2,10))


def add(*nums):
    total = 0
    for num in nums:
        total+= num
    return total
print(add(5,6))