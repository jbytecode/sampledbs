def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    
print(f"sign(10) = {sign(10)}")
print(f"sign(-10) = {sign(-10)}")
print(f"sign(0) = {sign(0)}")
