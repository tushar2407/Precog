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

'''
CIFAR-10 dataset
'''


def CIFAR_10_Loss(W):
    return L(X_train, Y_train, W) ## Loss function depends on the type of classifier you wish to use

W = np.random.rand(10,3073) * 0.001 # Random weight vector
df = eval_numerical_gradient(CIFAR_10_Loss, W)

## The gradient tells us the slope along every dimension
loss_original = CIFAR_10_Loss(W)
print(f"original loss : {loss_original}")

for step_size_log in [ -10,-9,-8,-7,-6,-5,-4,-3,-2,-1]:
    step_size =  10 ** step_size_log

    W_new = W - df*step_size

    loss_new = CIFAR_10_Loss(W_new)

    print(f"for step size {step_size} new loss is {loss_new")

