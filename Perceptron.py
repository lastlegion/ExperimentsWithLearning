import random
import numpy as np
#Generate dataset X
N=10
i=0
X=[None]*N
y=[None]*N
d = 2
for i in range(0,N):
    datapoint = [random.uniform(-1,1), random.uniform(-1,1)]
    X[i] = datapoint
    if(datapoint[0] + datapoint[1] > 0):
        y[i] = 1
    else:
        y[i] = -1
#Prepend a column vector of Os to X
zeros = np.zeros((N, d+1))
zeros[:, 1:N+1] = X
X=zeros

#Create matrices
X = np.matrix(X)
y = np.matrix(y)
#Initialize weights
w = np.zeros((1,d+1))

#Hypothesis
h = X*w.transpose()
for i in range(0,N):
    if h.item(i) >= 0:
        h[i] = 1
    else:
        h[i] = -1

#Number of iterations
iters = 400

for i in range(1, iters):
    h = X*w.transpose()
    for i in range(0,N):
        if h.item(i) >=0:
            h[i] = 1
        else:
            h[i] = -1
    j=0
    for j in range(0,10):
        #misclassification
        if not h.item(j) == y.item(j):
            print "misclassification"
            print ((X[j]*y.item(j)))
            w = np.add(w, ((X[j]*y.item(j))))
print w
print X
print "Outputs y"
print y
print "Predictions h"
print h

 


