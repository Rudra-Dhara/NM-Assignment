#function for lagrange interpolation
# x is our variable, a = list of x[i], n= list of f(x[i])

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

def Lag_diff(x,a,b):
    l=1
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
