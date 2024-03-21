import scipy.linalg as la
import numpy as np

myones = np.ones(5)
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

A = np.vstack([myones, x]).T

betahats = la.inv(A.transpose().dot(A)).dot(A.transpose()).dot(y)

print("Beta hats: {} ".format(betahats))
