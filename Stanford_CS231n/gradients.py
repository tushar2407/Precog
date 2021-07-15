import numpy as np
def eval_numerical_gradient(f, x):

    """
    f is the function which takes an array as input and given 'y' as output
    x is an np array of input values

    df(x)/dx = lim h->0( f(x+h)-f(x) )/h

    """

    fx = f(x)

    grad = np.zeros(x.shape)

    h = 0.00001

    itr = np.nditer(x, flags = ['multi_index'], op_flags = ['readwrite'])

    while not itr.finished:

        idx = itr.multi_index

        old_value = x[idx]

        x[idx] = old_value + h

        fxh = f(x)

        x[idx] = old_value

        grad[idx] = (fxh-fx)/h

        itr.iternext()

    return grad