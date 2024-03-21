import matplotlib.pyplot as plt
import random 

numbers = [random.normalvariate(0, 1) for i in range(10000)]

plt.hist(numbers)

plt.show()


