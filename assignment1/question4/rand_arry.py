# Program for random number generation 
"calling the function for array of random number generation generation"

import q4_fn as q4       #this import the predefined functions

print('Program to create an array of random numbers (between 0 and 10)\nof size n\n')

m=int(input("Enter the size of array (n): "))
assert m>=1   #make sure that the number is natural number

arr=q4.rand_list(m)

print("The array of ",m,"random numbers is: \n",arr)
