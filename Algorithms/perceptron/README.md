# Perceptron
Single layer perceptron is the simplest Artificial Neural Network (ANN)

Is like Logistic Regression, a linear classifier

Differnece of Loss Function and activation function
    
you can either have classification as <0,1> or as <-1,1>

- if you take it as <-1,1> the it is **Rosenblatt's perceptron**, which uses the *signum* function as activation function 

### Weight updation:
    
w<sup>n+1</sup> = w<sup>n</sup> + alpha*(y - y_hat)*x

where 
- *n* is the iteration

- *alpha* is the learning rate

- *w* is weight

- *x* is the fetaure vector
## References:
- https://jtsulliv.github.io/perceptron/