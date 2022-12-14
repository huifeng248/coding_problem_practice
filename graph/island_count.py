def island_count(grid):
  visited = set()
  count = 0
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      if explore_grid(grid, row, column, visited):
        print(row, column, "count", count)
        count += 1
  return count 
          
def explore_grid(grid, row, column, visited):
  if (row, column) in visited:
    return False
  
  if row >= len(grid): 
    return False
  if column >= len(grid[row]): 
    return False
  if row < 0 or column < 0: 
    return False 
  
  if grid[row][column] == "W": return False 
  
  visited.add((row, column))
  
  explore_grid(grid, row+1, column, visited)
  explore_grid(grid, row-1, column, visited)
  explore_grid(grid, row, column+1, visited)
  explore_grid(grid, row, column-1, visited)
  
  return True 




grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3


# solutions
# depth first
def island_count(grid):
  visited = set()
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore(grid, r, c, visited) == True:
        count += 1
  return count

def explore(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return False
  
  if grid[r][c] == 'W':
    return False
  
  pos = (r, c)
  if pos in visited:
    return False
  visited.add(pos)
  
  explore(grid, r - 1, c, visited)
  explore(grid, r + 1, c, visited)  
  explore(grid, r, c - 1, visited)
  explore(grid, r, c + 1, visited)
  
  return True
# r = number of rows
# c = number of columns
# Time: O(rc)
# Space: O(rc)
  
        
      