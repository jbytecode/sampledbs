import multipledispatch

@multipledispatch.dispatch(int, int)
def add(x, y):
    return x + y

@multipledispatch.dispatch(float, float)
def add(x, y):
    return x + y

@multipledispatch.dispatch(str, str)
def add(x, y):
    return x + " " + y



print(add(1, 2)) # 3
print(add(1.1, 2.2)) # 3.3
print(add("hello", "world")) # hello world

