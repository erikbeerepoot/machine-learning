# Using the standard sum of the squares formulation, we can come up with a loss fn:
#
# Equation for a line:
#
#    y = mx + b
#
# Given we have a labeled dataset of X = { (x1,y1), ... (xn,yn):
#
#    J = (1/N)*sum[1 -> n]((y - (mx + b))^2)
#
# and gradients:
#
#    df_dm += -(2/N)*x*(y - ((m*x) + b))
#    df_db += -(2/N)*(y - ((m*x) + b))

import random
import csv

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def compute_error(m,b,X,Y):
    """ Computes the cumulative training error over the data for a given set of parameters"""
    J = 0
    for i in range(0,len(X)):
        J += (Y[i] - ((m*X[i])+b))**2
    J *= (1/float(len(X)))
    return J

def save_line_plot(m, b, X, Y, filename, title='',x_label='',y_label=''):
    """ Saves a line plot """
    y = []
    for idx in range(0,len(X)):
        x = X[idx]
        y.append((m*x)+b)

    plt.plot(X, y, 'r.')
    plt.plot(X, Y, 'b.')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(filename)
    plt.close()


def plot_parameter_space(X,Y):
    """ Plots the parameter space vs. error"""
    error = []

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    m = np.arange(-3,3,0.1)
    b = np.arange(0,50,0.1)
    m, b = np.meshgrid(m,b)
    zs = np.array([compute_error(m_i, b_i,X,Y) for m_i, b_i in zip(np.ravel(m), np.ravel(b))])
    Z = zs.reshape(m.shape)
    surf = ax.plot_surface(m,b,Z,cmap='hot')
    plt.xlabel('m')
    plt.ylabel('b')
    plt.title('error')
    plt.savefig('../../../figs/gradient_descent/error')
    plt.show()


def step_gradient(B, X, Y, a):
    """ Computes the gradient for a specific parameter set """
    m = float(B[0])
    b = float(B[1])
    N = float(len(X))

    df_dm = 0
    df_db = 0
    for i in range(0,len(X)):
        x = X[i]
        y = Y[i]
        df_dm += -(2/N)*x*(y - ((m*x) + b))
        df_db += -(2/N)*(y - ((m*x) + b))

    new_m = m - a*df_dm
    new_b = b - a*df_db
    return new_m, new_b


def main():
    B = [
        random.gauss(0, 0.01),
        random.gauss(0, 0.01)
    ]
    X = []
    Y = []
    a = float(0.00001)
    num_iterations = 50
    error = []

    with open('../../../data/line.csv') as csvfile:
        datareader = csv.reader(csvfile,delimiter=',')
        for row in datareader:
            X.append(float(row[0]))
            Y.append(float(row[1]))

    for count in range(0,num_iterations):
        m, b = step_gradient(B, X, Y, a)
        B = [m, b]

        error.append(compute_error(m, b, X, Y))

        num_string = '%02d' % count
        save_line_plot(m, b, X, Y, '../../../figs/gradient_descent/fig' + num_string,x_label='x',y_label='y')

    plot_parameter_space(X,Y)

if __name__ == "__main__":
    main()




