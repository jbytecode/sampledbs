def myfunction(x):
    return x * x - 9 

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def bisection(f, a, b, eps = 0.000001):
    if sign(f(a)) == sign(f(b)):
        print("The function must change sign in the interval [a, b]")
        return None

    while abs(a - b) > eps:
        c = (a + b) / 2
        if sign(f(c)) == sign(f(a)):
            a = c
        else:
            b = c
    return c

result = bisection(myfunction, 0, 5)
print("The root is approximately:", result)
# The root is approximately: 3.000000000000001
