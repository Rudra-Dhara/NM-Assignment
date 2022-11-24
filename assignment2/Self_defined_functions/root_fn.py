# this is function for root finding

def NR_rt(F,f,x,x_tol,*args):
    while abs(F(x,*args))>x_tol:
        x =x - F(x,*args)/f(x,*args)
    
    return x



