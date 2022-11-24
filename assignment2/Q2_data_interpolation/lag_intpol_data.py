import sys
import numpy as np
import matplotlib.pyplot as plt
import math as m
sys.path.append('..')

#importing self defined functions
import Self_defined_functions.int_function as ifun
import Self_defined_functions.lag_interpole_fn as lag
import Self_defined_functions.root_fn as rt


a,b=np.loadtxt("data.dat",unpack=True)

a=np.array(a)
b=np.array(b)

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
print("\n\n########\nPart d")
while (x<=2):
    print("running...")             #the code take long time to run so useing the print
    x+=nr_root+1
    if abs(nr_root - rt.NR_rt(F,lag.Lag_fn,x,0.000001,a,b))> 0.00001:
        nr_root=rt.NR_rt(F,lag.Lag_fn,x,0.000001,a,b)
        root_list.append(nr_root)

        
    


#print("The the values of x where the integration is 0, list of the roots:\n",root_list)

#part e

coeff=lag.Lag_coeff(a,b)

print("\n\n########\nPart e")
print("The coefficient of x**0, x**1, x**2, x**3 are given by the list:\n",coeff)

global c1
c1 = coeff[0]
k1 = coeff[1]
k2 = coeff[2]
k3 = coeff[3]

def F_om(x,c,k2,k3):

    return (c*x**3)/6 + x*k2 - k3

def f_om(x,c,k2,k3):

    return (c*x**2)/2 + k2 +0*k3

omega = rt.NR_rt(F_om,f_om,0,0.000001,c1,k2,k3)
b1= k1 - c1*omega

a1 = k2 + (c1*omega**2)/2 -k1*omega

print("\nThe a,b,c,omega are:(first approxiamtion) \n",[a1,b1,c1,omega])

#now condider a,b,c are correct now we want to reestimate omega again
# we use intarpolated value at x=1 to find the omega
global lag_one
lag_one = lag.Lag_fn(-1,a,b)
def omega_od1(x,a1,b1,c1):
    return (a1 - b1 + c1)*m.exp(-x) - lag_one

def df_omega_od1(x,a1,b1,c1):
    return -(a1 - b1 + c1)*m.exp(-1*x)
#updated variavles
omega1 = rt.NR_rt(omega_od1,df_omega_od1,-1,0.0000001,a1,b1,c1)

b2= k1 - c1*omega1
a2 = k2 + (c1*omega1**2)/2 -k1*omega1

#updating k2 as 2nd order deriviative can contain some explicit errors

k2 = a2 + b2*omega1 + c1*omega1**2/6
#2nd time approximation
omega1 = rt.NR_rt(omega_od1,df_omega_od1,-1,0.0000001,a2,b2,c1)


print("\nThe updated a,b,c,omega are:(2nd approximation) \n",[a2,b2,c1,omega1])

omega2 = rt.NR_rt(omega_od1,df_omega_od1,-1,0.0000001,a2,b2,c1)

b3= k1 - c1*omega2
a3 = k2 + (c1*omega2**2)/2 -k1*omega2

#3rd time approximation
for i in range(3):                          #as 3 parameter is updating more than 3 itteration is giving large errors
    omega2 = rt.NR_rt(omega_od1,df_omega_od1,-1,0.0000001,a3,b3,c1)

    b3= k1 - c1*omega2
    a3 = k2 + (c1*omega2**2)/2 -k1*omega2
    k2 = a3 + b3*omega2 + c1*omega2**2/6    

#up to this point we consider the coefficient are well calculated except omega
#so we want to improve the value of omega

def f_plt(x,a,b,c,omega):

    return (a*x**2 + b*x + c)*np.exp(omega*x)

print("after 3rd approximation we are getting the value of the coefficients are:\n",[a3,b3,c1,omega2])
# 4th order approximation that only the value of a3 and omega2 have some errosr

global lag_4
lag_4 = lag.Lag_fn(-1,a,b)
def omega_od1(x,a1,b1,c1):
    return (a1 + b1 + c1)*m.exp(omega) - lag_4

def df_omega_od1(x,a1,b1,c1):
    return -(a1 - b1 + c1)*m.exp(-1*x)

 

plt.scatter(a,b)
plt.plot(a,f_plt(a,a3,b3,c1,omega2),label="3rd oreder")
plt.plot(a,f_plt(a,1,b3,c1,0.2),label="3rd")
plt.legend()

plt.show()