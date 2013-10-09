import random
import numpy as np

N=10
d=2
#Generate synthetic data
def generateData(X, y):
    i=0
    for i in range(0,N):
        datapoint = [random.uniform(-1,1), random.uniform(-1,1)]
        X[i] = datapoint
        if(datapoint[0] + datapoint[1] > 0):
            y[i] = 1
        else:
            y[i] = -1

#Calculate the hypothesis
def hypothesis(X,w):
    h = X*w.transpose()

    ###Should be a better way to do this
    #h = sign(X*w.transpose())
    for i in range(0,N):
        if h.item(i) >= 0:
            h[i] = 1
        else:
            h[i] = -1
    return h



X=[None]*N
y=[None]*N
generateData(X,y)

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
h = hypothesis(X,w)

#Number of iterations
iters = 400

for i in range(1, iters):
    h = hypothesis(X,w)
    j=0
    for j in range(0,10):
        #misclassification
        if not h.item(j) == y.item(j):
            w = np.add(w, ((X[j]*y.item(j))))

print "Input"
print X
print "Outputs y"
print y
print "Predictions h"
print h.transpose()

 


