# DFS
# def island_count(grid):
#   count = 0
#   visited = set()
#   for row in range(len(grid)):
#     for column in range(len(grid[row])):
#       if find_island(row, column, grid, visited):
#         count += 1
#   return count 

# def find_island(row, column, grid, visited):
#   if grid[row][column] == "W" or (row, column) in visited:
#     return False
  
#   stack = [(row, column)]
#   directions = [[0,1], [0,-1], [1,0], [-1,0]]
#   while stack:
#     current = stack.pop()
#     r, c = current
#     if current not in visited  and grid[r][c] == "L":
#       visited.add(current)
#       for point in directions:
#         new_r = r + point[0]
#         new_c = c + point[1]
#         valid_row = 0 <= new_r < len(grid)
#         valid_col = 0 <= new_c < len(grid[row])
#         if valid_col and valid_row and (new_r, new_c) not in visited:
#           stack.append((new_r, new_c))
#   return True
          
# recursive
def island_count(grid):
  count = 0
  visited = set()
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      if find_island(row, column, grid, visited):
        count += 1
  return count 

def find_island(row, column, grid, visited):
  if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[row]):
    return False
  if (row, column) in visited:
    return False
  if grid[row][column] == "W":
    return False
#   the visited set only add the land, so that we would not traverse the same land again
  visited.add((row, column))
  find_island(row+1, column, grid, visited)
  find_island(row-1, column, grid, visited)
  find_island(row, column-1, grid, visited)
  find_island(row, column+1, grid, visited)
  return True