'''
https://projecteuler.net/problem=82
'''

import queue as Q


with open("p083_matrix.txt") as f:
    matrix = [[int(x) for x in line.split(",")] for line in f]

came_from = { (0, 0): None }
cost_so_far = { (0, 0): matrix[0][0] }
goal = (len(matrix) - 1, len(matrix[0]) - 1)
frontier = Q.PriorityQueue()
frontier.put((0, 0))

while frontier.qsize():
    curr = frontier.get()

    if curr == goal:
        print(cost_so_far[goal])
        break
    
    for neighbor in [(curr[0] - 1, curr[1]),(curr[0] + 1, curr[1]),(curr[0], curr[1] - 1),(curr[0], curr[1] + 1)]:
        if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < len(matrix) and neighbor[1] < len(matrix[1]):
            new_cost = cost_so_far[curr] + matrix[neighbor[0]][neighbor[1]]
            
            if not neighbor in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.put(neighbor)
                came_from[neighbor] = curr
