myset = set([1, 2, 3, 1, 1, 1, 2, 3, 3, 3])

print(myset)  # {1, 2, 3}

myotherset = {1, 2, 3, 1, 1, 1, 2, 3, 3, 3}

print(myset) # {1, 2, 3}

print(myset == myotherset)  # True

for element in myset:
    print(element)
