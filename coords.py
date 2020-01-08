import numpy as np

# coordinates of 3 points in coordinate system 1 (CS 1) as column vectors
p1 = np.array([1,1,1]).reshape(-1,1)
p2 = np.array([1,4,1]).reshape(-1,1)
p3 = np.array([4,4,1]).reshape(-1,1)

P = np.concatenate((p1,p2,p3), axis=1) # combine into matrix

# coordinates of same 3 points in CS 2
q1 = np.array([2,2,1]).reshape(-1,1)
q2 = np.array([2,5,1]).reshape(-1,1)
q3 = np.array([5,5,1]).reshape(-1,1)

Q = np.concatenate((q1,q2,q3), axis=1) # combine into matrix

# AP = Q, where A is the transformation matrix
# therefore A = QP^-1

A = np.matmul(Q, np.linalg.inv(P))
AP = np.matmul(A, P)

# check the original equation AP = Q is satisfied
if (Q.all() == AP.all()):
    print("well that bit works....")
else:
    print("bollocks")

# if that works then Ap = q where p is any position vector in CS 1, and q is the equivalent position vector in CS 2
# likewise p = (A^-1)q, allowing conversion in the opposite direction
# if Bq = r converts from CS 2 to CS 3, then BAp = r converts from CS 1 to CS 3
