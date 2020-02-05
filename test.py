from __future__ import division, print_function, unicode_literals
import math
import numpy as np 
import matplotlib.pyplot as plt
def grad(x):
    return 2*x+ 5*np.cos(x)

def cost(x):
    return x**2 + 5*np.sin(x)
def myGD1(eta, x0):
    x = [x0]
    print ("x = ", x)
    for it in range(100):
        x_new = x[-1] - eta*grad(x[-1])
        print ("x_new = ", x_new)
        print ("x[-1]",x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)

(x1, it1) = myGD1(.1, -5)
print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], cost(x1[-1]), it1))