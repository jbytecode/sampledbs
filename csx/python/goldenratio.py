def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

n = 30

fibonacci_numbers = [fibonacci(n) for n in range(n)]

print(fibonacci_numbers)

for i in range(1, n):
    gration = fibonacci_numbers[i] / fibonacci_numbers[i-1]
    print("Iteration: {}, Golden Ratio: {}".format(i, gration))
