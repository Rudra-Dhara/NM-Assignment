import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('..')

import Self_defined_functions.int_function as ifun
import Self_defined_functions.lag_interpole_fn as lag


a,b=np.loadtxt("data.dat",unpack=True)

#part a
# the function is defined by the lag.Lag_fn(x,a,b) teke the a, b list and x is the variable
print("############\nPart a")
x=2.5
print("The value of the function at x = {} is {}".format(x,lag.Lag_fn(x,a,b)))

print("\n\n############\nPart b")


x=np.linspace(-2.5,2.87,1000)

plt.plot(x,lag.Lag_fn(x,a,b),label="Interpolation")
#plt.plot(lag.Lag_diff(x,a,b),label="lag_differentiation")
plt.legend()
plt.grid()
plt.show()