"""Directions
In this lab, you will work with grayscale images represented as matrices of integers from 0
to 255.
For every question, write a NumPy solution (no loops).
For Questions 1, 2, 3, and 11, also write a list-comprehension solution.
Assume NumPy is already imported as np and NumPy functions receive NumPy arrays."""

import numpy as np
import pandas as pd

# Question 1
def brighten(image, amount):
    return np.minimum(image + amount, 255)

# Question 2
def  threshold(image, thresh):
    return np.where(image < thresh, 0, 255)

# Question 3
def invert(matrix):
    return 255 - np.array(matrix)

# Question 4
def flip_lr(image):
    return np.flip(image, axis=1)

#Questuion 5
def flip_tb(image):
    return np.flip(image, axis=0)

#Question 6
def row_means(image):
    return np.mean(image, axis=1)

#Question 7
def row_center(image):
    x = np.mean(image, axis=1)
    return image - x[:, np.newaxis]

#Question 8
def col_max(image):
    return np.max(image, axis=0)

import numpy as np

#Question 9
def col_max_image(image):
    
    max_values = np.max(image, axis=0)
    
    image[:] = max_values
    
    return image

#Question 10
def col_compare(image):

    max_values = np.max(image, axis=0)
    image[:] = np.where(image == max_values, True, False)
    return image

#Question 11
def combine(image1, image2):
    return np.where(image1, image1+image2, image2+image1)
    
#Question 12
def difference(image1, image2):
    return np.abs(image1 - image2)

#Question 13
def suppress(image):
    return np.where(image < np.mean(image), 0, image)

#Question 14
"""Explain shapes of:
arr.mean(axis=1)
arr.mean(axis=1, keepdims=True)"""

# arr.mean(axis=1) returns a 1D array containing the mean of each row, resulting in a shape of (n,).
# arr.mean(axis=1, keepdims=True) returns a 2D array where the mean of each row is retained as a single column, resulting in a shape of (n, 1).


#Question 15
"""Explain:
• np.tile
• why NumPy is faster"""

#constructs a new array by repeating an input array A, reps times.
# NumPy is faster than pure Python because it is implemented in C making it closer to memory

#Question 16
def brighten(image, amount):
    return image[[[image + amount if image + amount <= 255 else 255 for pixel in row] for row in image]]

def  threshold(image, thresh):
    return image[[[image if pixel < thresh else 255 for pixel in row] for row in image]]

def invert(matrix):
    return matrix[[[255 - pixel for pixel in row] for row in matrix]]

def combine(image1, image2):
    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(image1, image2)]
