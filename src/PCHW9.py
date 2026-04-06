#PCHW 9

import numpy as np

# Question 1: Subtract the column mean from each element
# Shape of result: same as input
def q1(arr):
    return arr - arr.mean(axis=0)

# Question 2: Divide each row by its row sum
# Shape of result: same as input
def q2(arr):
    return arr / arr.sum(axis=1, keepdims=True)

# Question 3: Mean across the last axis of a 3D array
# Shape of result: (n, m) — last dimension is removed
def q3(arr):
    return arr.mean(axis=-1)

# Question 4: Replace each column with the column minimum
# Shape of result: same as input
def q4(arr):
    return np.tile(arr.min(axis=0), (arr.shape[0], 1))

# Question 5: Return all values strictly between 5 and 12
def q5(arr):
    return arr[(arr > 5) & (arr < 12)]

# Question 6 (explanation in comments):
# arr - arr.mean(axis=1, keepdims=True)
#
# This works without copying data because of NumPy broadcasting.
# arr.mean(axis=1, keepdims=True) has shape (n, 1) when arr has shape (n, m).
# NumPy broadcasts the (n, 1) array across all m columns automatically,
# so the subtraction is computed element-wise without allocating a full copy
# of the mean array expanded to shape (n, m).

# Question 7 (explanation in comments):
# arr has shape (4, 3, 2).
# arr.mean(axis=1) -> shape (4, 2)   [middle dim removed]
# arr.mean(axis=2) -> shape (4, 3)   [last dim removed]
#
# Subtracting (4, 2) - (4, 3) raises an error because NumPy cannot broadcast
# these shapes together: the trailing dimensions 2 and 3 are not equal and
# neither is 1, so there is no valid broadcast rule that makes them compatible.
