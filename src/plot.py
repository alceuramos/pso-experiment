import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt
from matplotlib import cm

class Plot(object):
    """docstring for Plot."""
    def __init__(self):
        super(Plot, self).__init__()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.sc = self.ax.scatter([],[],[])

    def fun(self,x, y):
        return x**2 + y**2 +1
    def startPlot(self):
        print('startPlot')
        x = y = np.arange(-10.0, 10.0, 0.05)
        X, Y = np.meshgrid(x, y)
        zs = np.array(self.fun(np.ravel(X), np.ravel(Y)))
        Z = zs.reshape(X.shape)

        plt.ion()

        self.ax.set_xlabel('X Label')
        self.ax.set_ylabel('Y Label')
        self.ax.set_zlabel('Z Label')
        self.ax.plot_surface(X, Y, Z, cmap=cm.hot, alpha=0.5, linewidth=0)

        self.fig.show()
        plt.draw()
    def updatePlot(self, x, y, z):
        self.sc._offsets3d = (x,y,z)
        plt.draw()
        plt.pause(0.01)
