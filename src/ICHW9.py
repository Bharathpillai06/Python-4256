import numpy as np


# Question 1
arr.mean(axis=0)                     
arr.mean(axis=1)                    
arr.mean(axis=2)                      
arr.mean(axis=2, keepdims=True)       
arr - arr.mean(axis=2, keepdims=True) 


# Question 2
def divide_rowsum(arr):
    return arr / arr.sum(axis=1, keepdims=True)


# Question 3
def col_center(arr):
    return arr - arr.mean(axis=0)


# Question 4
def center_last_axis(arr):
    return arr - arr.mean(axis=-1, keepdims=True)


# Question 5
def max_mask(arr):
    return arr == arr.max(axis=-1, keepdims=True)


# Question 7
def above_row_mean(arr):
    mask = arr > arr.mean(axis=1, keepdims=True)
    return np.where(mask, arr, 0)


# Question 8
def normalize_last_axis(arr):
    return arr / arr.sum(axis=-1, keepdims=True)


# Question 9
def threshold_3d(arr, cutoff):
    return (arr >= cutoff).astype(int)


# Question 10
def subtract_global_and_row(arr):
    step1 = arr - arr.mean()
    return step1 - step1.mean(axis=1, keepdims=True)
