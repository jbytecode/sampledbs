import math 

def normal(x):
    return (1/math.sqrt(2*math.pi))*math.exp(-0.5*x*x)

def integrate(f, a, b, eps):
    sum = 0.0
    x = a 
    while x < b:
        sum += f(x)*eps
        x += eps
    return sum 

print(integrate(normal, -1.96, 1.96, 0.0001))

# Output: 0.9500100536071496