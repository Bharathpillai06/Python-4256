from time import time

import numpy as np
# Question 1
# List comprehension solution   
li = list(range(1000000))
result = [x + 5 for x in li]
print(result)

# NumPy solution
arr = np.array(li)      
result = arr + 5
print(result)

# Question 2
# List comprehension solution
result = [x > 10 for x in li]
print(result)

# NumPy solution
result = arr > 10
print(result)

# Question 3
# List comprehension solution
result = [x ** 2 for x in li]
print(result)
# NumPy solution
result = arr ** 2
print(result)
# Question 4
# List comprehension solution
li2 = list(range(1000000, 2000000))
result = [x + y for x, y in zip(li, li2)]
print(result)
# NumPy solution
arr2 = np.array(li2)
result = arr + arr2
print(result)
# Question 5
# Timing list comprehension solution for Question 1
start = time()
result = [x + 5 for x in li]
end = time()
print(end - start)
# Timing NumPy solution for Question 1
start = time()
result = arr + 5
end = time()
print(end - start)
