import random

import datahelpers
import plotting
import ml_algorithms

def resample_batch(X,Y,n):
    """ Sample n datapoints from X & Y"""
    sample_range = random.sample(range(len(X)),n)
    return [float(X[i]) for i in sample_range], [float(Y[i]) for i in sample_range]

def main():
    X, Y = datahelpers.input.read_points('../../data/line-dense.csv')
    num_iterations = 2000
    batch_size = 50
    a = float(0.00001)
    B = [float(0), float(7)]
    error = []


    #plotting.line.plot_parameter_space(X, Y, ml_algorithms.gradient_descent.compute_error,'../../figs/mini_batch_gradient_descent/error',True)

    for it in range(0,num_iterations):
        X_sample, Y_sample = resample_batch(X, Y, batch_size)

        m, b = ml_algorithms.gradient_descent.step_gradient(B, X_sample, Y_sample, a)
        B = [m, b]


        error.append(ml_algorithms.gradient_descent.compute_error(m, b, X, Y))

        num_string = '%04d' % it

        if it % 25 == 0:
            plotting.line.save_line_plot(m, b, X_sample, Y_sample, '../../figs/mini_batch_gradient_descent/fig' + num_string, x_label='x', y_label='y')
            print('%s:%s' %(it,B))



if __name__ == "__main__":
    main()
