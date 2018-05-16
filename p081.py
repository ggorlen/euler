'''
https://projecteuler.net/problem=81

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 
matrix, from the top left to the bottom right by only moving right and down.
'''


memo = {}

def get_min_path(matrix, row, col):
    if row >= len(matrix) or col >= len(matrix[row]):
        return float('inf')

    if (row, col) in memo:
        return memo[(row, col)]

    a = get_min_path(matrix, row + 1, col)
    b = get_min_path(matrix, row, col + 1)
    memo[(row, col)] = matrix[row][col] + min(a, b)

    if a == float('inf') and b == float('inf'):
        memo[(row, col)] = matrix[row][col]
        
    return memo[(row, col)]


with open('p081_matrix.txt') as file:
    matrix = [list(map(int, line.strip().split(','))) for line in file]

print(get_min_path(matrix, 0, 0))
