
#function for lagrange interpolation
# x is our variable, a = list of x[i], n= list of f(x[i])

def L(x,a,b):
    
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


