def mean(vec):
    return sum(vec) / len(vec)

def ols(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    n = len(x)
    s_xy = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    s_xx = sum((x[i] - x_mean) ** 2 for i in range(n))
    b1 = s_xy / s_xx
    b0 = y_mean - b1 * x_mean
    return (b0, b1)

def predict(x, b0, b1):
    return b0 + b1 * x


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
b0, b1 = ols(x, y)
print(f"Intercept (b0): {b0}")
print(f"Slope (b1): {b1}")

