import numpy as np

# Vector is a liste of features

# Person fetatures in a 3 dimensions space
# [height, weightm, age]
person = np.array([1.78, 70, 32]);

# Matrix is a 2D array of coords

# For example this is a 3x3 matrix
M =     np.array([[0,0], [0, 1], [0, 2],
                [0, 1], [1, 1], [2, 1],
                [0, 2], [1, 2], [2, 2]]);

# Vector difference

# For example beetween M[0] and M[5]

diff =  np.abs(M[0] - M[5]);
diff2D = np.sqrt(diff[0] ** 2 + diff[1] ** 2);

print("Difference beetween M[0] and M[5] = ", diff2D);

# Scalar multiplication

scalarMultiplicationParam = 42;
scalarMultiplicationResult = scalarMultiplicationParam * M[5];
print("scalarMultiplicationResult of ", M[5], " by ", scalarMultiplicationParam, " = ", scalarMultiplicationResult);

# Scalar product

dotProduct = np.dot(M[7], M[8]);

print("dot product of ", M[7], " by ", M[8], " = ", dotProduct);