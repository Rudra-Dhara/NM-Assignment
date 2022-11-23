import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('..')

#importing self defined functions
import Self_defined_functions.int_function as ifun
import Self_defined_functions.lag_interpole_fn as lag
import Self_defined_functions.root_fn as rt


a,b=np.loadtxt("data.dat",unpack=True)

#part a
# the function is defined by the lag.Lag_fn(x,a,b) teke the a, b list and x is the variable
print("############\nPart a")
x=2.5
print("The value of the function at x = {} is {}".format(x,lag.Lag_fn(x,a,b)))


#part b

x_tol=0.0000001
x_start1=0
x_start2=3 

print("\n\n############\nPart b")
print("The first root is: ",rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start1,x_tol,a,b))
print("The second root is: ",rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start2,x_tol,a,b))

#part c
n=100
l_limit=0
u_limit=4

intgn= ifun.int_simp(lag.Lag_fn,l_limit,u_limit,n,a,b)
print("\n\n#########\nPart c")
print("The value of the integration within the limit 0 to 3 is: ", intgn)

#part d
#derivative of a integral of a function is the function itself
#we use the above logic here

#defining the integral as 0 to x as
def F(x,a,b):
    n_div=100
    return ifun.int_simp(lag.Lag_fn,0,x,n_div,a,b)

nr_root=rt.NR_rt(F,lag.Lag_fn,-1,0.000001,a,b)
root_list=[nr_root]
x=-1
count=0 
while (x<=2):
    print("running...")
    x+=nr_root+1
    if abs(nr_root - rt.NR_rt(F,lag.Lag_fn,x,0.000001,a,b))> 0.00001:
        nr_root=rt.NR_rt(F,lag.Lag_fn,x,0.000001,a,b)
        root_list.append(nr_root)

        
    

print("\n\n########\nPart d")
print("The the values of x where the integration is 0, list of the roots:\n",root_list)

