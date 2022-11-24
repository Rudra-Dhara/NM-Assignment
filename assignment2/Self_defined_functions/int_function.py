#This is a self defined module for integration
#Here I defined many metheds of integration you can intutiavely understand the method by looking the name of the method of integration
#eg. int_mid is for mid point method.

#Almost all function take the argument in form of (f,a,b,n) stands for (function,starting limit, ending limit, number of steps)
#only gauss quadratur and romborg higher order method take different argument


#midoint method
def int_mid(f,a,b,n):
    sum=0
    h= (b-a)/n
    for i in range(n):
        sum+= f(a+(i+0.5)*h)
    intgn = sum*h

    return intgn


#trapizoidal method
def int_trap(f,a,b,n):
    sum=(f(a)+f(b))/2
    h= (b-a)/n

    for i in range(1,n):
        sum+=f(a+i*h)
    intgn=sum*h

    return intgn


#simpsons 1/3 method
def int_simp(f,a,b,n,*args):
    if(n%2!=0):
        n+=1
    sum=(f(a,*args)+f(b,*args))
    h= (b-a)/n

    for i in range(1,n,2):
        sum+= 4*f(a+i*h,*args) 
    
    for i in range(2,n,2):
        sum+= 2*f(a+i*h,*args)

    intgn=sum*h/3

    return intgn


#romborg method taking only one correction
def int_romb_first(f,a,b,n):
    if n%2!=0:
        n+=1
    I2=int_trap(f,a,b,n)
    I1=int_trap(f,a,b,n//2)

    intgn=(4*I2 - I1)/3
    return intgn


#romborg nth order corretrion method
#k denote the order of correction to be included
def int_romb_n(f,a,b,n,k):
    if k>1:
        I1=int_romb_n(f,a,b,n,k-1)
        I2=int_romb_n(f,a,b,n//2,k-1)

        return ((4**k)*I1 - I2)/(4**k -1)

    else :
        
        return int_romb_first(f,a,b,n)

#gauss quadrature method using 3 point for 5 degree polinomial
#no division of of the limit
def int_gsquad_deg3(f,a,b):
    w=[5/9,8/9,5/9]
    x=[-0.774597,0,0.774597]
    sum=0

    for i in  range(len(x)):
        y=(a+b)/2 + ((b-a)/2)*x[i]
        sum+=  w[i]*f(y)
    sum*=(b-a)/2

    return sum    



#gauss quadrature method using 3 point for 5 degree polinomial 
# with deviding the limit into n small parts    
def int_gsquad_bypart(f,a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(n):
        sum+=int_gsquad_deg3(f,a+i*h,a+(i+1)*h)
        print(a+i*h,a+(i+1)*h)
    
    return sum


