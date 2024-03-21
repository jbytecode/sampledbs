import scipy.optimize as opt
import math

def f(x):
    return math.pow(x[0] - 3.14159265, 2.0) + math.pow(x[1] - 2.71828, 2.0)

startingpoint = [5, 5]

result = opt.minimize(f, startingpoint)


print(result)

print(result.x)

#  message: Optimization terminated successfully.
#   success: True
#    status: 0
#       fun: 1.2977905700660667e-14
#         x: [ 3.142e+00  2.718e+00]
#       nit: 2
#       jac: [-1.856e-07 -9.341e-08]
#  hess_inv: [[ 8.006e-01 -2.448e-01]
#             [-2.448e-01  6.994e-01]]
#      nfev: 9
#      njev: 3
# [3.14159255 2.71827995]

