from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set()
  directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
  queue = deque([])
  queue.append((starting_row, starting_col, 0))
  while queue:
    row, column, level = queue.popleft()
    if (row, column) not in visited:
      visited.add((row, column))
        
      if grid[row][column] == "C":
        return level
      
      for point in directions:
        new_r = row + point[0]
        new_c = column + point[1]
        valid_row = 0 <=new_r < len(grid)
        valid_column = 0 <= new_c < len(grid[row])
        if valid_row and valid_column and (new_r, new_c) not in visited and grid[new_r][new_c] != "X":
          queue.append((new_r, new_c, level +1))
  return -1