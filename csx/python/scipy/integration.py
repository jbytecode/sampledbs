import scipy.integrate as integration
import math 

def f(x):
    return (1/math.sqrt(2 * math.pi)) * math.exp(-0.5 * x * x)

result, error  = integration.quad(f, -1, 1)

print(result)

