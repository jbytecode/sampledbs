# Define an array (specifically a list in Python)
a = [1, 2, 3, 4, 5]

# type of a 
print(type(a))
# The output of the code above will be:
# <class 'list'>

# Access the first element of the array
print(a[0])

# Access the last element of the array
print(a[-1])

# Append elements to the array
a.append(6)

# Count the number of occurrences of an element in the array
print(a.count(6))

# Find the index of an element in the array
a.index(3)

# Pop the last element of the array
a.pop()
print(a)

# Remove an element of the array
a.remove(5)
a.remove(4)
a.remove(3)
print(a)
# The output of the code above will be:
# [1, 2]

# Clear the array
a.clear()
print(a)

# Insert elements
a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)
a.insert(3, 4)
print(a)
# The output of the code above will be:
# [1, 2, 3, 4]

# Sort the array
a.sort()

# Reverse the array
a.reverse()
print(a)
# The output of the code above will be:
# [4, 3, 2, 1]
