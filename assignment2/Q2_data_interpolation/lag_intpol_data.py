import sys
import numpy as np
import matplotlib.pyplot as plt
import math as m
sys.path.append('..')

#importing self defined functions
import Self_defined_functions.int_function as ifun
import Self_defined_functions.lag_interpole_fn as lag
import Self_defined_functions.root_fn as rt

#importing and unpacking the data
a,b=np.loadtxt("data.dat",unpack=True)

a=np.array(a)
b=np.array(b)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#part a: finding the value at x=2.5
# the function is defined by the lag.Lag_fn(x,a,b) teke the a, b list and x is the variable
print("############\nPart a")
x=2.5
print("The value of the function at x = {} is {}".format(x,lag.Lag_fn(x,a,b)))




#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#part b: root finding using NR-Method

x_tol=0.0000001
x_start1=-3
root1= rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start1,x_tol,a,b)
rt_listb =[root1]

#depending on the function you may need to chage the jump of x start or the jump in the loop
#if x_start1 reacheas the value where the 1st order differential is very low then it can shoot to high value and may not give the root
while x_start1<=4:
    if abs(lag.Lag_diff(x_start1,a,b)) < 0.01:       # if the slope is almost parallel it will exclude the value 
        x_start1+=2
        continue

    if abs(rt_listb[-1]-rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start1,x_tol,a,b)) > 0.0001:
        rt_listb.append(rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start1,x_tol,a,b)) 
    x_start1+=2

print("\n\n############\nPart b")
print("\nThe the roots of the funciton are: ",rt_listb)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#part c: Using simpsion to integrate it from 0 to 4
n=100
l_limit=0
u_limit=4

intgn= ifun.int_simp(lag.Lag_fn,l_limit,u_limit,n,a,b)
print("\n\n#########\nPart c")
print("The value of the integration within the limit 0 to 3 is: ", intgn)


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#part d: finding the value of x where the integration 0 to x is 0
#derivative of a integral of a function is the function itself
#we use the above logic here

#defining the integral as 0 to x as
def F(x,a,b):
    n_div=100
    return ifun.int_simp(lag.Lag_fn,0,x,n_div,a,b)

nr_root=rt.NR_rt(F,lag.Lag_fn,-1,0.000001,a,b)
root_list=[nr_root]
x=-nr_root
count=0 
print("\n\n########\nPart d")
while (x<=2):
    print("running...")             #the code take long time to run so useing the print to show user that it is running
    x+=1
    if abs(nr_root - rt.NR_rt(F,lag.Lag_fn,x,0.000001,a,b))> 0.00001:
        nr_root=rt.NR_rt(F,lag.Lag_fn,x,0.000001,a,b)
        root_list.append(nr_root)

print("\nThe the values of x where the integration is 0, list of the roots:\n",root_list)



#------------------------------------------------------------------------------------------------------------------------------------------------------------
#part e: Finding the coefficient a, b, c, omega

coeff=lag.Lag_coeff(a,b)

print("\n\n########\nPart e")
print("The coefficient of x**0, x**1, x**2, x**3 are given by the list:\n",coeff)

#the coeff of x**0, x, x**2, x**3 according to the order
c1 = coeff[0]
k1 = coeff[1]
k2 = coeff[2]
k3 = coeff[3]

#function and its derivative for getting the value of omega
def F_om(x,c,k1,k2,k3):

    return (c*x**3)/6 - 0.5*k1*x**2 + x*k2 - k3

def f_om(x,c,k1,k2,k3):

    return (c*x**2)/2 - x*k1 + k2 +0*k3

omega = rt.NR_rt(F_om,f_om,0.2,0.00000000001,c1,k1,k2,k3) #solving using NR-Mehthod
b1= k1 - c1*omega

a1 = k2 - (c1*omega**2)/2 -b1*omega

print("\nThe a,b,c,omega are: \n",[a1,b1,c1,omega])


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#this part of the program to show  is used to show that out coefficient is quite close to the original value

def f_plt(x,a,b,c,omega):

    return (a*x**2 + b*x + c)*np.exp(omega*x)

#after the plot you will see the value is very accurate
plt.scatter(a,b)
plt.plot(a,f_plt(a,a1,b1,c1,omega),label="with centrel difference approximation",color='red')
plt.legend()
plt.grid()
plt.show()