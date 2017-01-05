"""
https://projecteuler.net/problem=67
"""

triangle = []
memo = {}

with open("p067_triangle.txt", 'r') as f:
    for line in f:
        triangle.append([int(x) for x in line.strip().split(" ")])

def get_max_path(triangle, row, idx):
    try:
        if not (row, idx) in memo:
            memo[(row, idx)] = triangle[row][idx] + \
                max(get_max_path(triangle, row + 1, idx), 
                    get_max_path(triangle, row + 1, idx + 1))
        return memo[(row, idx)]
    except IndexError:
        return triangle[row][idx]

print(get_max_path(triangle, 0, 0))