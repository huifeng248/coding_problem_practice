# # DFS
# def minimum_island(grid):
#   minimum_island = float('+inf')
#   visited = set()
#   for row in range(len(grid)):
#     for column in range(len(grid[row])):
#       if grid[row][column] == "L":
#         size = get_island_size(row, column, grid, visited)
#         if size != 0:
#           minimum_island = min(minimum_island, size)
#   return minimum_island

# def get_island_size(row, column, grid, visited):
#   size = 0
#   stack = [(row, column)]
#   dirs = [[1,0], [-1,0], [0,-1], [0,1]]
#   while stack:
#     current = stack.pop()
#     r, c = current
#     if current not in visited and grid[r][c] == "L":
#       size += 1
#       visited.add(current)
      
#       for point in dirs:
#         new_r = r + point[0]
#         new_c = c + point[1]
#         valid_row = 0 <= new_r < len(grid)
#         valid_column = 0 <= new_c <len(grid[row])
#         if valid_column and valid_row and (new_r, new_c) not in visited:
#           stack.append((new_r, new_c))
#   return size

# recursive
def minimum_island(grid):
  minimum_island = float('+inf')
  visited = set()
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      if grid[row][column] == "L":
        size = get_island_size(row, column, grid, visited)
        if size != 0:
          minimum_island = min(minimum_island, size)
  return minimum_island
  
def get_island_size(row, column, grid, visited):
  if (row, column) in visited:
    return 0
  if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[row]):
    return 0
  if grid[row][column] == "W":
    return 0
  visited.add((row, column))
  size = 1
  size += get_island_size(row +1, column, grid, visited)
  size += get_island_size(row -1, column, grid, visited)
  size += get_island_size(row, column+1, grid, visited)
  size += get_island_size(row, column -1, grid, visited)
  return size