"""
https://projecteuler.net/problem=96
"""


def solve(grid, row=0, col=0):

    if grid[row][col] == 0: # This square is awaiting a solution
        for n in range(1, len(grid)+1):
            
            # If this is a legal move, make it
            if legal_move(grid, row, col, n):
                grid[row][col] = n

                # Move to the next square
                if col < len(grid) - 1:
                    if solve(grid, row, col+1):
                        return True
                elif row < len(grid) - 1:
                    if solve(grid, row+1, 0):
                        return True
                else: # No squares left--puzzle is solved
                    return True
                
        # Backtrack and undo
        grid[row][col] = 0

    else: # Move to the next square
        if col < len(grid) - 1:
            if solve(grid, row, col+1):
                return True
        elif row < len(grid) - 1:
            if solve(grid, row+1, 0):
                return True
        else: # No squares left--puzzle is solved
            return True
        

def legal_move(grid, row, col, num):
    column = [grid[x][col] for x in range(len(grid))]
    box_row, box_col = row // 3 * 3, col // 3 * 3
    box = []
    for i in range(3):
        for j in range(3):
            box.append(grid[box_row + i][box_col + j])
    return num not in grid[row] and num not in column and num not in box

    
with open("p096_sudoku.txt") as puzzles:
    total = 0 
    puzzle = []
    counter = 1
    for line in puzzles:
        try:
            puzzle.append([int(x) for x in line.strip()])
        except ValueError:
            puzzle = []
        if len(puzzle) == 9:    
            print("solving puzzle " + str(counter))
            counter += 1
            solve(puzzle)
            num = ""
            for n in range(3):
                num += str(puzzle[0][n])
            total += int(num)    
    print(total)
