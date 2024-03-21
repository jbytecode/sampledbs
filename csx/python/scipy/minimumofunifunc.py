import scipy.optimize as opt
import math

def f(x):
    return math.pow(x, 2.0) + 100

startingpoint = 5

result = opt.minimize(f, startingpoint)


print(result)

print(result.x)
