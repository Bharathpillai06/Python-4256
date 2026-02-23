"""4256: Day 5 - Preclass Problems
1) Write a function called star m(n) that takes an integer greater then 2 as
an argument and returns a matrix representation of a star graph on n nodes,
where node 0 is the central node."""

def star_m(n):
    if n <= 2:
        raise ValueError("Input must be an integer greater than 2.")
    
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(1, n):
        matrix[0][i] = 1  
        matrix[i][0] = 1  
    
    return matrix
print(star_m(5))

"""2) Write a function called star d(n) that takes an integer greater then 2 as
an argument and returns a dictionary representation of a star graph on n nodes,
where node 0 is the central node.
For example, star d(5) should return"""

def star_d(n):
    if n <= 2:
        raise ValueError("Input must be an integer greater than 2.")
    
    dict = {x: [] for x in range(n)}
    
    for i in range(1, n):
        dict[0].append(i)
        dict[i].append(0)
    
    return dict
print(star_d(5))

