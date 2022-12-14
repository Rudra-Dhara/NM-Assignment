#function for lagrange interpolation
# x is our variable, a = list of x[i], n= list of f(x[i])
import numpy as np

#lagrange interpolation funciton
def Lag_fn(x,a,b):
    
    l=1
    sum=0
    for j in range(len(a)):

        l=1

        for i in range(len(a)):
            if j==i:
                continue
            l*= (x-a[i])/(a[j]-a[i])

        sum+= b[j]*l
    

    return sum


#derivative of interpolation funcion
def Lag_diff(x,a,b):
    sum=0
    for j in range(len(a)):

        diff_sum=0

        for k in range(len(a)):
            if k==j:
                continue
            l_diff=1
            for i in range(len(a)):
                if j==i or i==k:
                    continue
                l_diff*= (x-a[i])/(a[j]-a[i])

            l_diff= l_diff/(a[j]-a[k])
            diff_sum+=l_diff
            
        sum+= b[j]*diff_sum


    return sum


#This are some derivative function for getting out our coefficients
#this function is n**3 complexity so don't use it for large data point
def Lag_difn2(x,a,b):
    sum = 0

    for j in range(len(a)):
        sum_1=0

        for l in range(len(a)):
            if l==j:
                continue
            sum_2=0
            for w in range(len(a)):
                if w==j or w==l:
                    continue
                l_diff=1

                for i in range(len(a)):
                    if i==j or i==l or i==w:
                        continue
                    l_diff*= (x-a[i])/(a[j]-a[i])

                sum_2+=l_diff/(a[j]-a[w])

            sum_1+=sum_2/(a[j]-a[l])
        
        sum+=b[j]*sum_1
    
    return sum


#we use centered deference approcimation to find 1st
# it is correct upto O(h**4) 
def Lag_d2F(x,a,b):
    h=0.1
    d1f = (Lag_diff(x - 4*h,a,b)/280 - 4*Lag_diff(x - 3*h,a,b)/105 + Lag_diff(x - 2*h,a,b)/5 - 4*Lag_diff(x - h,a,b)/5
            + 4*Lag_diff(x + h,a,b)/5 - Lag_diff(x + 2*h,a,b)/5 + 4*Lag_diff(x + 3*h,a,b)/105 - Lag_diff(x + 4*h,a,b)/280)/h
    
    return d1f

# centered deference approximation of 2nd order
# give upto O(h**4) correct result
def Lag_d3F(x,a,b):
    h=0.5  
    d2f = (-Lag_diff(x - 4*h,a,b)/560 + 8*Lag_diff(x - 3*h,a,b)/315 - Lag_diff(x - 2*h,a,b)/5 + 8*Lag_diff(x - h,a,b)/5 
    - 205*Lag_diff(x,a,b)/72 + 8*Lag_diff(x + h,a,b)/5 - Lag_diff(x + 2*h,a,b)/5 + 8*Lag_diff(x + 3*h,a,b)/315 -Lag_diff(x + 4*h,a,b)/560 )/h**2 
    
    return d2f

def Lag_coeff(a,b):
    x_0 = Lag_fn(0,a,b)
    x_1 = Lag_diff(0,a,b)

    x_2 = Lag_d2F(0,a,b)/2

    x_3 = Lag_d3F(0,a,b)/6

    return [x_0,x_1,x_2,x_3]

