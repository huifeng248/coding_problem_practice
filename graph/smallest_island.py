def minimum_island(grid):
  smallest = float("+inf")
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      size = calculate_island_size(grid, r, c, visited)
      # print(size, "node", (r,c), grid[r][c] )
      if size != 0 and size < smallest:
        smallest = size
  return smallest
  
def calculate_island_size(grid, r, c, visited):
  size = 0
  # print("~~~~~~~~", "node", (r,c), grid[r][c] )
  if r >= len(grid): return 0
  if c >= len(grid[r]): return 0
  if r < 0 or c < 0: return 0
  
  
  position = (r, c)
  if position in visited:
    return 0
  
  if grid[r][c] == "W": return 0
  
  size = 1
  visited.add((r, c))
  size += calculate_island_size(grid, r-1, c, visited)
  size += calculate_island_size(grid, r+1, c, visited)
  size += calculate_island_size(grid, r, c+1, visited)
  size += calculate_island_size(grid, r, c-1, visited)
  
  return size

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2)

# minimum island
# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.

# test_00:
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2
# test_01:
grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

minimum_island(grid) # -> 1
# test_02:
grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

minimum_island(grid) # -> 9
# test_03:
grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

minimum_island(grid) # -> 1

# solutions
# depth first
def minimum_island(grid):
  visited = set()
  min_size = float("inf")
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size = explore_size(grid, r, c, visited)
      if size > 0 and size < min_size:
        min_size = size
  return min_size

def explore_size(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return 0
  
  if grid[r][c] == 'W':
    return 0
  
  pos = (r, c)
  if pos in visited:
    return 0
  visited.add(pos)
  
  size = 1
  size += explore_size(grid, r - 1, c, visited)
  size += explore_size(grid, r + 1, c, visited)  
  size += explore_size(grid, r, c - 1, visited)
  size += explore_size(grid, r, c + 1, visited)
  return size
# r = number of rows
# c = number of columns
# Time: O(rc)
# Space: O(rc)