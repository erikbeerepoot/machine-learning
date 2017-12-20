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
import plotting
import datahelpers
import ml_algorithms





def main():
    B = [
        random.gauss(0, 0.01),
        random.gauss(0, 0.01)
    ]

    a = float(0.00001)
    num_iterations = 50
    error = []

    X, Y = datahelpers.input.read_points('../../data/line.csv')

    for count in range(0,num_iterations):
        m, b = ml_algorithms.gradient_descent.step_gradient(B, X, Y, a)
        B = [m, b]

        error.append(ml_algorithms.gradient_descent.compute_error(m, b, X, Y))

        num_string = '%02d' % count

        plotting.line.save_line_plot(m, b, X, Y, '../../figs/gradient_descent/fig' + num_string,x_label='x',y_label='y')

    plotting.line.plot_parameter_space(X,Y,ml_algorithms.gradient_descent.compute_error,'../../figs/gradient_descent/error')


if __name__ == "__main__":
    main()




