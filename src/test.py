from mpl_toolkits import mplot3d
#matplotlib inline
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import time
def fun(x, y):
    return x**2 + y**2 +1
X = np.random.rand(100, 3)*10
Y = np.random.rand(100, 3)*5

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(X[:, 0], X[:, 1], X[:, 2])
x = y = np.arange(-2.0, 10.0, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array(fun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_surface(X, Y, Z, cmap=cm.hot, alpha=0.5, linewidth=0)

fig.show()

for i in range(0, 20):
    plt.pause(1)
    Y = np.random.rand(100, 3)*5
    print(Y)
    q = [1,2,3]
    w = [1,3,2]
    sc._offsets3d = (q,w,np.array(fun(np.ravel(q), np.ravel(w))) )
    plt.draw()
