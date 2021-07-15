'''
sigmoid function :

    sig(x) = 1/(1+exp(-x))

    d(sig(x))
    -------     =  (1-sig(x))*sig(x)
      dx

In general form:

    sig(x) = 1/( 1 + exp( -( w0*x0+w1*x1+w2 ) ) )

    d(sig(x))
    -------     =  (1-sig(x))*sig(x)
      dx
'''
import math

w = [1,2,3]
x = [1,2]

dot = w[0]*x[0]+w[1]*x[1]+w[2]
f = 1.0 / (1 + math.exp(-dot))

ddot = (1-f)*f

dx = [w[0]*ddot, w[1]*ddot] ## backprop into x

dw = [x[0]*ddot, x[1]*ddot, 1.0*ddot] ## backprop into w

