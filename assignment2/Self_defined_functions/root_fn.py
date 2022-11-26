# this is function for root finding
#F is the function and f is it's derivative x_tol is the degree of accuracy and x_start is the starting point of the integral
def NR_rt(F,f,x_start,x_tol,*args):
    while abs(F(x_start,*args))>x_tol:
        x_start =x_start - F(x_start,*args)/f(x_start,*args)
    
    return x_start



