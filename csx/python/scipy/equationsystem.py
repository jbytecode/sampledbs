import scipy.linalg as la

# 3x + 5y + 4z = 100
# 2x - 2y + 10z = 250
# x + y - 2z = 50

a = [
        [3, 5, 4],
        [2, -2, 10],
        [1, 1, -2]
    ]

b = [100, 250, 50]

result = la.solve(a, b)

print(result)

# [ 85.29411765 -32.35294118   1.47058824]

