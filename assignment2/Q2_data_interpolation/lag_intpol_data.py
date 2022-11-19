import sys
import numpy as np
import matplotlib.pyplot as plt

x,y=np.loadtxt("data.dat",unpack=True)

print(x)
print(y)

plt.plot(x,y)
plt.show()

#print(df)