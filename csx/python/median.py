# Integer Division
# In Python, the // operator performs integer division, which means it divides two numbers and rounds down to the nearest whole number.
# >>> 10 // 2
# 5
# >>> 10 // 3
# 3
# >>> 10 // 4
# 2


def median(v):
    n = len(v)
    if n % 2 == 1:
        midpoint = n // 2
        return sorted(v)[midpoint]
    else:
        midpoint1 = n // 2
        midpoint2 = midpoint1 - 1
        return (sorted(v)[midpoint1] + sorted(v)[midpoint2]) / 2
    
print(median([1, 2, 3, 4, 5]))
print(median([1, 2, 3, 4, 5, 6]))
