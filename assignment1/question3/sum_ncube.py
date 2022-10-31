
def Sncube(n):  #function to give the sum of cube of n natural numbers
    assert (int(n) == n and n>=1), "Please Enter a natural number"
    x=0
    for i in range(1,n+1):
        x+=i**3
    return x

print("This is a program to find the sum of cubes of first n natural numbers\n")

x=int(input("Enter the nth number:"))

print("The sum of cubes of first",x,"natural number is = ",Sncube(x))

print("\n\nCalling the function to find the sum of cubes of 30 consecutive natural\nnumbers starting from 11 ")
print("\nWe will just do Sncube(40)-Sncube(10) to find the value")
print("Which is ",Sncube(40)-Sncube(10))