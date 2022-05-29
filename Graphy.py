import matplotlib.pyplot as plt
import numpy as np


preX=0
preY=0

lastpreX=0
lastpreY=0

x=5
y=int(input("Enter the total amount: "))

xpoints = np.array([preX,x])
ypoints = np.array([preY,y])

updateTrue = 0
updateTrue=int(input("Do you want to update the graph: "))

if(updateTrue==1):
    
    lastpreX=preX
    lastpreY=preY
    preX=x
    preY=y

    x=6
    y=int(input("Enter the total amount: "))

    xpoints=np.array([lastpreX,preX,x])
    ypoints=np.array([lastpreY,preY,y])


plt.plot(xpoints,ypoints)
plt.show()

