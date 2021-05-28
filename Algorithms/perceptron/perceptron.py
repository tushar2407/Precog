import numpy as np
import matplotlib.pyplot as plt

# NAND gate features
# note: x0 is a dummy variable for the bias term
#     x0  x1  x2
x = [[1., 0., 0.],                                  
    [1., 0., 1.],                                 
    [1., 1., 0.],                                  
    [1., 1., 1.]]

# Desired outputs
y = [1.,                                            
    1.,                                            
    1.,                                            
    0.]

def train(x, y, threshold, alpha, t):
    w = np.zeros(len(x[0]))             # weights
    n = 0
    yhat_vector = np.ones(len(y))       # vector for predictions
    errors = np.ones(len(y))            # vector for errors (actual-predicted)
    J = []                              # vector for SSE cost function
    while n<t:
        for i in range(0, len(x)):
            
            f = np.dot(x[i], w)

            if f > threshold:
                yhat = 1.
            else:
                yhat = 0.
            yhat_vector[i] = yhat

            for j in range(0, len(w)):
                w[j] = w[j] + alpha*(y[i] - yhat)*x[i][j]
            
            n+=1
        for i in range(0, len(y)):
            errors[i] = (y[i]-yhat_vector[i])**2
        J.append(0.5*np.sum(errors))
    return w, J

threshold = 0.0
alpha = 0.1
t = 50

print("weights are:\n ", train(x, y, threshold, alpha, t)[0])
print("sum of squared errors are:\n ", train(x, y, threshold, alpha, t)[1])

J = train(x, y, threshold, alpha, t)[1]     # pulling out the sum-of-squared errors from the tuple
epoch = np.linspace(1,len(J),len(J))

# %matplotlib inline  
plt.plot(epoch, J)
plt.xlabel('Epoch')
plt.ylabel('Sum-of-Squared Error')
plt.title('Perceptron Convergence')
plt.show()