import matplotlib.pyplot as plt
import numpy as np


preX=0
preY=0

x=5
y=int(input("Enter the total amount: "))

xpoints = np.array([preX,x])
ypoints = np.array([preY,y])

plt.plot(xpoints,ypoints)
plt.show()