def fibo(n: int):                                        # fibonacci function using recursion only take natural number as input
    assert int(n)==n, "INVALID ENTRY FRACTINAL NUMBER!please enter a natural number"
    if n>2:
        return fibo(n-1) + fibo(n-2)
    elif n==1 or n==2:
        return 1
    else:
        print("INVALID ENTRY -ve NUMBER! Pease enter a natural number")

