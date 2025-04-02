def customsum(v):
    s = 0
    for i in v:
        s += i
    return s

def pysum(v):
    return sum(v)

a = [1, 2, 3, 4, 5]
print(customsum(a))
print(pysum(a))

