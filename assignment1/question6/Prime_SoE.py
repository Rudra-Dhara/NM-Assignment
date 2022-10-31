#"program that returns the list of all prime numbers less than or equal to a positive integer n, using Sieve of Eratosthenes."
def Siev(n):                                            
    n_list= list(range(2,n+1))

    p_list=[]

    for p in n_list:
        p_list.append(p)                    #p_list starts with the value 2, then it takes the next number
                                            #--- after removing it's multiple and so on which gives the list of prime numbest
        for i in range(2,n//p+1):
            if i*p_list[-1] in n_list:
                n_list.remove(i*p_list[-1])
    print('The list of prime numbers are:\n',p_list)


print("This program gives the all the prime numbers\nless than the number 200.")
     

Siev(200)             # so that it will give all the prime numbers less than or equal 200
