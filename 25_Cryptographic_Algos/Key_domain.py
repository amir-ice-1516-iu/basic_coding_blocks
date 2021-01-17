# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

import random


def Operate(Operators, Key_length=8):

       
    # Make data.
    #X = np.arange(1, 256, 1)
    #Key = [23,56,87,123,233,69,170,29]
    Key = []
    for _ in range(Key_length):
        Key.append(random.randint(1,255))
    if len(Key):
        X = np.array(Key)
    else:
        X = np.arange(1,255,1)
    #print(X)
    Y = np.arange(1, 255, 1)
    #print(Y)
    X, Y = np.meshgrid(X, Y)
    #print(type(X),type(Y))
    #print(X.ndim)
    for Operator in Operators:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        R = eval("X"+Operator+"Y")
        Z = R
        #print(type(Z))
        #print(Z[0].ndim)
        
        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)
        
        # Customize the z axis.
        #ax.set_zlim(0, 256)
        #ax.zaxis.set_major_locator(LinearLocator(10))
        #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        
        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.title("X"+Operator+"Y"+" [Keys: "+str(Key_length)+"]")
        
        plt.show()

KL = [0]
#Ops = ["|","&","^","%","+","-","*","/"]
Ops=["^"]
for K in KL:
    Operate(Ops, K)


