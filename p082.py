'''
https://projecteuler.net/problem=82
'''


def memoize(f):
    memo = {}

    def helper(a, b, c, d=None):
        key = (b, c, d) # need to hash last_move too

        if key not in memo:
            memo[key] = f(a, b, c, d)

        return memo[key]

    return helper
    
@memoize
def dfs(matrix, row, col, last_move=None):
    if row < 0 or row >= len(matrix):
        return float("inf")

    if col >= len(matrix[0]):
        return 0
        
    min_sum = dfs(matrix, row, col + 1)
    
    if last_move != "u":
        min_sum = min(dfs(matrix, row + 1, col, "d"), min_sum)
    
    if last_move != "d":
        min_sum = min(dfs(matrix, row - 1, col, "u"), min_sum)
    
    return matrix[row][col] + min_sum


#matrix = [
#    [131, 673, 234, 103, 18],
#    [201, 96, 342, 965, 150],
#    [630, 803, 746, 422, 111],
#    [537, 699, 497, 121, 956],
#    [805, 732, 524, 37, 331]
#]
#
#matrix = [
#    [1, 0, 0],
#    [0, 0, 1],
#    [1, 1, 1],
#    [1, 1, 1],
#]

with open("p082_matrix.txt") as f:
    matrix = [[int(x) for x in line.split(",")] for line in f]

minimal_sum = float("inf")

for row in range(len(matrix)):
    minimal_sum = min(dfs(matrix, row, 0), minimal_sum)

print(minimal_sum)
