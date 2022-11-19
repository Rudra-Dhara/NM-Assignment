# this is function for root finding

def NR_rt(F,f,x,x_tol):
    while abs(F(x))>x_tol:
        x =x - F(x)/f(x)
    
    return x

def F(x):
    return x**2 -10

def f(x):
    return 2*x

print(NR_rt(F,f,1,0.0000001))