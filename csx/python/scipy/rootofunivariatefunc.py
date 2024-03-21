import scipy.optimize as opt

def f(x):
    return x * x - 100

startingpoint = 2
myroot = opt.root(f, startingpoint)

print(myroot)
print(myroot.x)

#  message: The solution converged.
#  success: True
#   status: 1
#      fun: [ 0.000e+00]
#        x: [ 1.000e+01]
#     nfev: 11
#     fjac: [[-1.000e+00]]
#        r: [-2.000e+01]
#      qtf: [ 1.663e-10]
# [10.]

