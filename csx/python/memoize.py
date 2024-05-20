import functools
import time

@functools.cache
def calculate_double(num):
    time.sleep(1)
    return num * 2


print(calculate_double(2))
print(calculate_double(3))

print(calculate_double(2))
print(calculate_double(3))
