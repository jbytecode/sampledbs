def myfunc(x):
    return x**2 - 9

def myfunc_prime(x):
    return 2*x

def newton_raphson(func, func_prime, x0, tol=1e-10, max_iter=100):
    for i in range(max_iter):
        oldvalue = x0 
        x0 = x0 - func(x0) / func_prime(x0)
        if abs(x0 - oldvalue) < tol:
            return x0
    return x0 

print(newton_raphson(myfunc, myfunc_prime, 1))