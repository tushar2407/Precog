'''
implementation of dropout 
(Not recommended one)
'''
import numpy as  np
p = 0.5
def train_step(X):
    # forward pass for a 3 layer NN
    H1 = np.max(0, np.dot(W1, X)+b1)
    U1 = np.random.randn(*H1.shape) < p # first dropout mask
    H1 *= U1 # drop
    H2 = np.max(0, np.dot(W2, H1)+b2)
    U2 = np.random.randn(*H2) <p
    H2 *= U2
    out = np.dot(W3, H2)+b3

    # backward pass : compute gradients ---> not shown
    # update parameters --> not shown

def predict(X):
    H1 = np.max(0, np.dot(W1,X)+b1)*p # scale the activations
    H2 = np.max(0, np.dot(W2,H1)+b2)*p # scale the activations
    out = np.dot(W3, H2)+b3
