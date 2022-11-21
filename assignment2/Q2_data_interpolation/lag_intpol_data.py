import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('..')

import Self_defined_functions.int_function as ifun
import Self_defined_functions.lag_interpole_fn as lag
import Self_defined_functions.root_fn as rt


a,b=np.loadtxt("data.dat",unpack=True)

#part a
# the function is defined by the lag.Lag_fn(x,a,b) teke the a, b list and x is the variable
print("############\nPart a")
x=2.5
print("The value of the function at x = {} is {}".format(x,lag.Lag_fn(x,a,b)))

print("\n\n############\nPart b")
#part b

x_tol=0.0001
x_start1=0
x_start2=3 
print("The first root is: ",rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start1,x_tol,a,b))
print("The first root is: ",rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start2,x_tol,a,b))









x=np.linspace(-4,4,100)


plt.plot(x,lag.Lag_fn(x,a,b),label="Interpolation")
plt.plot(x,lag.Lag_diff(x,a,b),label="lag_differentiation")
plt.scatter(a,b)
plt.legend()
plt.grid()
plt.show()