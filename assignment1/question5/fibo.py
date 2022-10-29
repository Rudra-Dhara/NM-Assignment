def fibo(n: int):                                        # fibonacci function using recursion only take natural number as input
    assert (int(n)==n and n>=1), "INVALID ENTRY FRACTINAL NUMBER!please enter a natural number"
    
    a1=0
    a2=1
    x=0
    
    if n>2:

        for i in range(2,n):
            x=a1+a2
            a1=a2
            a2=x
        return x

    elif n==2:
        return a2
    else:
        return a1

"this function gives fibonacci series as 0,1,1,2,3,5,8,..."