import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

x = np.linspace(-50,50,100)
bgn = 0
plt.ylim(0,50)
for i in range(5):
    y = x**2
    plt.plot(x,y)
    plt.xlim(bgn,bgn+1)
    plt.savefig('./pictuer/Quadratic_function_%d.png' % i)
    bgn += 0.1



    #print(f"a{bgn}");
