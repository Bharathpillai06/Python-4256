""" Day 5 class """

from collections import deque


def cycle_m(n):
    mat = []
    for i in range(n):
        row = [0] * n
        row[(i - 1) % n] = 1
        row[(i + 1) % n] = 1
        mat.append(row)
    return mat


def cycle_d(n):
    return {i: {(i - 1) % n, (i + 1) % n} for i in range(n)}


def is_regular_m(mat):
    degrees = [sum(row) for row in mat]
    return len(set(degrees)) == 1


def is_regular_d(di):
    degrees = [len(neighbors) for neighbors in di.values()]
    return len(set(degrees)) == 1


def complete_bipartite_d(m, n):
    di = {}
    for i in range(m):
        di[i] = set(range(m, m + n))
    for j in range(m, m + n):
        di[j] = set(range(m))
    return di


def complete_bipartite_m(m, n):
    total = m + n
    mat = [[0] * total for _ in range(total)]
    for i in range(m):
        for j in range(m, m + n):
            mat[i][j] = 1
            mat[j][i] = 1
    return mat


def di_to_mat(di):
    n = len(di)
    mat = [[0] * n for _ in range(n)]
    for node, neighbors in di.items():
        for neighbor in neighbors:
            mat[node][neighbor] = 1
    return mat


def bfs_m(mat, start_node=0):
    n = len(mat)
    dist = [-1] * n
    dist[start_node] = 0
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        for neighbor in range(n):
            if mat[node][neighbor] == 1 and dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist
