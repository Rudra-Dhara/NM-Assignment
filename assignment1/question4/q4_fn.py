import random as rn
import numpy as np

"The function part"

def rand_list(n): #return the list of random number of size n
    x=[]

    for i in range(n):
        x.append(rn.uniform(0,10))  #this append a random real number between 0 and 10
    return np.array(x)              #output as array


def min_list(x):       #give minimum number in a list
    a=x[0]
    n=len(x)
    
    for i in range(n):
        if x[i]<a:
            a=x[i]
    return a     #o/p as array


def list_sort(x):       #sorting function give out put as array
    a=[]
    x=x.tolist()
    n=len(x)

    for i in range(n):
        a.append(min_list(x))
        x.remove(min_list(x))
    return np.array(a)       #o/p as array