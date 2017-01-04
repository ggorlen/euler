"""
https://projecteuler.net/problem=18
"""

triangle = []

with open("p018_triangle.txt", 'r') as f:
    for line in f:
        triangle.append([int(x) for x in line.strip().split(" ")])

def get_max_path(triangle, row, idx):
    try:
        return triangle[row][idx] + \
               max(get_max_path(triangle, row + 1, idx), 
                   get_max_path(triangle, row + 1, idx + 1))
    except IndexError:
        return triangle[row][idx]
    
print(get_max_path(triangle, 0, 0))