def myfunc(x):
    return x * x - 9

# x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
def secant_method(f, x0, x1, tol=1e-6, maxiter = 1000):
    for i in range(maxiter):
        x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        print(f"* iteration: {i}, x0: {x0}, x1: {x1}, x2: {x2}")
        if abs(x2 - x1) < tol:
            break
        x0 = x1 
        x1 = x2
    return x2

print(secant_method(myfunc, 0, 5))

# Output:
# * iteration: 0, x0: 0, x1: 5, x2: 1.8
# * iteration: 1, x0: 5, x1: 1.8, x2: 2.6470588235294117
# * iteration: 2, x0: 1.8, x1: 2.6470588235294117, x2: 3.095238095238095
# * iteration: 3, x0: 2.6470588235294117, x1: 3.095238095238095, x2: 2.9941463414634146
# * iteration: 4, x0: 3.095238095238095, x1: 2.9941463414634146, x2: 2.9999084486625875
# * iteration: 5, x0: 2.9941463414634146, x1: 2.9999084486625875, x2: 3.0000000894069685
# * iteration: 6, x0: 2.9999084486625875, x1: 3.0000000894069685, x2: 2.9999999999986358
# 2.9999999999986358

