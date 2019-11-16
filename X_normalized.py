import numpy as nd
X = nd.random.random((5,5))

def normalize (X):
    print ('This is your random 5x5 ndarray: \n')
    print(X)
    print (' ------------------------------------------------------')
    
    # computing for the mean
    mean = X.mean ()
    print ('This is the mean of X ndarray: \n')
    print (mean)
    print (' ------------------------------------------------------')
    
    #computing for the standard deviation
    standardDev = X.std()
    print ('This is the standard deviation of X ndarray: \n')
    print (standardDev)
    print (' ------------------------------------------------------')
    
    #computing for the normalized X 
    Z = (X-mean)/standardDev
    print ('This is the Normalized ndarray X: \n')
    print (Z)
    print (' ------------------------------------------------------')