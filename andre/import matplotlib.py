import matplotlib
import matplotlib.pyplot as plit 
import numpy as np 

plt.axis ([0, 10, 0, 1])

for i in range (1000)
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()