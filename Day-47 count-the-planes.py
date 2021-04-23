# This is my solution for AlgoDaily problem Count the Planes
# Located at https://algodaily.com/challenges/count-the-planes

def num_of_planes(grid):
    ships = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'P':
                ships += 1
                dfs(grid, row, col)
    return ships

def dfs(matrix, rows, columns):
    stack = [(rows, columns)]
    
    while stack:
        rows, columns = stack.pop()
        
        for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            cell = (rows + y, columns + x)
            if cell[0] >= 0 and cell[1] >= 0 and cell[1] < len(matrix[0]) and cell[0] < len(matrix):
                if matrix[cell[0]][cell[1]] == 'P':
                    matrix[cell[0]][cell[1]] = 'T'
                    stack.append(cell)