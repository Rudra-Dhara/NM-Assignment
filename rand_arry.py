# Program for random number generation 
import random as rn
import numpy as np

print('Program to create an array of random numbers (between 0 and 10)\nof size n\n')

n=int(input("Enter the size of array (n): "))
assert n>=1   #make sure that the number is natural number

x=[]

for i in range(n):
    x.append(rn.uniform(0,10))  #this append a random real number between 0 and 10

arr=np.array(x)  #making the list to a numpy array

print("The array of ",n,"random numbers is: \n",arr)
