import sys
sys.path.append("..") #lookint for sibling directory in assignment2

import Self_defined_functions.int_function as ifun
import math 

def f(x):
    return x*math.log(x)-x

a=1 #starting limit of the integral
b=3 #end limit of the ingegral
n=20 # number of part in the integral

intgn_simp= ifun.int_simp(f,a,b,n)
intgn_trap= ifun.int_trap(f,a,b,n)

print("""The value of integration of the function x ln x - x in the range [1,3] 
using\ntrapizoidal methed is {}\nSimpson's rule is {}\n\n############\n
this result is obtain by dividing the range in {} divitions. """.format(intgn_trap,intgn_simp,n)) 
