import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

def save_line_plot(m, b, X, Y, filename, title='',x_label='',y_label=''):
    """ Saves a line plot """
    y = []
    for idx in range(0,len(X)):
        x = X[idx]
        y.append((m*x)+b)

    plt.plot(X, y, 'r-')
    plt.plot(X, Y, 'b.')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(filename)
    plt.close()

def plot_parameter_space(X,Y,fn,filename,show):
    """ Plots the parameter space vs. error"""
    m = np.arange(-3, 3, 0.1)
    b = np.arange(0, 50, 0.1)
    m, b = np.meshgrid(m,b)
    zs = np.array([fn(m_i, b_i,X,Y) for m_i, b_i in zip(np.ravel(m), np.ravel(b))])
    Z = zs.reshape(m.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(m,b,Z,cmap='hot')
    plt.xlabel('m')
    plt.ylabel('b')
    plt.title('error')
    plt.savefig(filename)

    if show:
        plt.show()

    plt.close()