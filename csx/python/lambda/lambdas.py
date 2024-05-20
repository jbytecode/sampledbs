mylist = [1, 2, 3, 4, 5]

# Use lambda to define an anonymous function
# that takes a single argument and returns
# the argument multiplied by 2
result = list(map(lambda x: x * 2, mylist))

print(result)  # Output: [2, 4, 6, 8, 10]

# Use lambda to define an anonymous function
# that takes two arguments and returns the sum
result = list(map(lambda x, y: x + y, mylist, mylist))

print(result)  # Output: [2, 4, 6, 8, 10]

# Use lambda to filter out even numbers 
result = list(filter(lambda x: x % 2 == 0, mylist))

print(result)  # Output: [2, 4]



def myfunc(x):
    return x * 2

result = list(map(myfunc, mylist))
print(result)  # Output: [2, 4, 6, 8, 10]