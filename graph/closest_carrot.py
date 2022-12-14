from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  visited = set()
  
  queue = deque([([starting_row, starting_col], 0)])
  while queue:
    position, level = queue.popleft()
    row, column = position
    
    if grid[row][column] == "X":
      continue
    
    if (row, column) in visited:
      continue
    
    visited.add((row, column))
    
    directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
    print("level~~~~", level, "node:", (row, column), "sigbal", grid[row][column])
    for point in directions:
      n_r, n_c = row + point[0], column + point[1]
      
      if 0<=n_r and n_r < len(grid) and 0 <=n_c and n_c < len(grid[row]):
        
        queue.append(([n_r, n_c], level +1))
        if grid[n_r][n_c] == "C":
          return level + 1
  return -1

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 1, 2) # -> 4

# solutions
# breadth first
from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set([ (starting_row, starting_col) ])
  queue = deque([ (starting_row, starting_col, 0) ])
  while queue:
    row, col, distance = queue.popleft()
    
    if grid[row][col] == 'C':
      return distance
    
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col      
      pos = (neighbor_row, neighbor_col)
      row_inbounds = 0 <= neighbor_row < len(grid)
      col_inbounds = 0 <= neighbor_col < len(grid[0])
      if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] != 'X':
        visited.add(pos)
        queue.append((neighbor_row, neighbor_col, distance + 1))
        
  return -1
# r = number of rows
# c = number of columns
# Time: O(rc)
# Space: O(rc)
        
    
  
  