import sys
sys.path.insert(0,'/home/rudra/assignment/assignment1/question5')
from fibo import fibo
import numpy as np
import matplotlib.pyplot as plt

def gold_ratio(n):
    assert n>0, "enter a natural number"

    return fibo(n+2)/fibo(n+1)
    #note fibo(1)=0 so we cannot devide by 0 so it starts deviding from fibo(2)



n=int(input("enter a large natural number: "))
assert n>0, "Please enter a natural number"
x=np.arange(1,n)

gold_r=[]

for i in x:
    gold_r.append(gold_ratio(i))
gold_r=np.array(gold_r)

print("The ratio ratio asymptotically reaching a constant value: ",gold_ratio(n))


plt.title("Plot for nth ratio of n+1 and nth fibonacci number")
plt.plot(x,gold_r)
plt.xlabel("n")
plt.ylabel("Ratio")
plt.grid()
plt.show()

