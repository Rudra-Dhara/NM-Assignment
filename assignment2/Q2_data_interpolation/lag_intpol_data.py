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

root1=rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start1,x_tol,a,b)
root2=rt.NR_rt(lag.Lag_fn,lag.Lag_diff,x_start2,x_tol,a,b)

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

def F_om(x,c,k1,k2,k3):

    return (c*x**3)/6 - 0.5*k1*x**2 + x*k2 - k3

def f_om(x,c,k1,k2,k3):

    return (c*x**2)/2 - x*k1 + k2 +0*k3

omega = rt.NR_rt(F_om,f_om,0.2,0.00000001,c1,k1,k2,k3)
b1= k1 - c1*omega

a1 = k2 - (c1*omega**2)/2 -b1*omega

print("\nThe a,b,c,omega are: \n",[a1,b1,c1,omega])

#another method to calculate part e
#using the roots
#we use roots of the equation as the root of quadratic equation as the quadratic equation has no roots
# we have the closed form function of first derivative k1
#we will use those to find the a,b,c,omega
# we know the value of c

a2= c1/(root1*root2)

b2 = -a2*(root2+root1)

omega2 = (k1 - b2)/c1
print("\nWe have calculated the value from the roots for the function. Here we are getting the better value\n")
print("With out using heigher order derivative, the value of a, b, c, omega:\n",[a2,b2,c1,omega2])



def f_plt(x,a,b,c,omega):

    return (a*x**2 + b*x + c)*np.exp(omega*x)


#now condider a,b,c are correct now we want to reestimate omega again
# we use intarpolated value at x=1 to find the omega





plt.scatter(a,b)
plt.plot(a,f_plt(a,a1,b1,c1,omega),label="with forward difference approximation",color='red')
plt.plot(a,f_plt(a,a2,b2,c1,omega2),label="using the rootsroots",color="black")
plt.legend()

plt.show()