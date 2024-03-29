import math

def get_delta(a, b, c):
    return b ** 2 - 4 * a * c

def number_of_roots(a, b, c):
    delta = get_delta(a, b, c)
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0
    
def get_roots(a, b, c):
    delta = get_delta(a, b, c)
    if delta < 0:
        return None
    elif delta == 0:
        return (-b + math.sqrt(delta)) / (2 * a)
    else:
        return (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)
    
def get_maxmin_of_parabola(a, b, c):
    x = -b / (2 * a)
    y = a * math.pow(x, 2) + b * x + c
    return x, y

# example
p1 = 1
p2 = -3
p3 = 2
print(number_of_roots(p1, p2, p3))
print(get_roots(p1, p2, p3))
print(get_maxmin_of_parabola(p1, p2, p3))