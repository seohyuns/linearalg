import numpy as np
import scipy as sp


#Part 2

#Question 8
a = np.matrix( ((1,2,3,4,5), (1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5)) )
a = a^3

print a

#Question9
a = np.matrix( ((2,4,5), (2,6,1),(-2,9,15),(12,0,15), (3,34,-52)) )
b = np.matrix( ((2,4,5,4), (2,6,1,4), (-2,9,15,4)) )

answer = (a*b).transpose()
print answer

#Question10
M = np.matrix( ((2,4,5), (2,6,1), (-2,9,15), (12,0,15), (3,34,-52)) )
print np.linalg.matrix_rank(M)

#Question11
M = np.matrix( ((1,0,1,3), (2,3,4,7), (-1,-3,-3,-4)) )
print np.linalg.matrix_rank(M)

