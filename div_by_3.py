import numpy as nd

#this is the original ndarray
array = nd.arange(1,101,1).reshape(10,10)

#this is the ndarray squares of the first 100 positive integers
A = array**2
print('Array A: \n', A)        
print ('\n Elements in array A that are divisible by 3: \n', A[A%3 == 0])


        