
def compute_error(m,b,X,Y):
    """ Computes the cumulative training error over the datafor a given set of parameters"""
    J = 0
    for i in range(0,len(X)):
        J += (Y[i] - ((m*X[i])+b))**2
    J *= (1/float(len(X)))
    return J

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

