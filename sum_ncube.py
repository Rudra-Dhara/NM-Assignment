
def Sncube(n):  #function to give the sum of cube of n natural numbers
    if n>1:
        return n**3 + Sncube(n-1)
    elif n==1:
        return 1
    else:
        print("Entered number is less than one, Please enter a natural number")

print("This is a program to find the sum of cubes of first n natural numbers\n")

x=int(input("Enter the nth number:"))

print("The sum of cubes of first ",x,"natural number is = ",Sncube(x))