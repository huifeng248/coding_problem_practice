# def minimum_island(grid):
#   smallest = float("+inf")
#   visited = set()
#   for r in range(len(grid)):
#     for c in range(len(grid[r])):
#       size = calculate_island_size(grid, r, c, visited)
#       # print(size, "node", (r,c), grid[r][c] )
#       if size != 0 and size < smallest:
#         smallest = size
#   return smallest
  
# def calculate_island_size(grid, r, c, visited):
#   size = 0
#   # print("~~~~~~~~", "node", (r,c), grid[r][c] )
#   if r >= len(grid): return 0
#   if c >= len(grid[r]): return 0
#   if r < 0 or c < 0: return 0
  
  
#   position = (r, c)
#   if position in visited:
#     return 0
  
#   if grid[r][c] == "W": return 0
  
#   size = 1
#   visited.add((r, c))
#   size += calculate_island_size(grid, r-1, c, visited)
#   size += calculate_island_size(grid, r+1, c, visited)
#   size += calculate_island_size(grid, r, c+1, visited)
#   size += calculate_island_size(grid, r, c-1, visited)
  
#   return size

# BFS
# from collections import deque 
# def minimum_island(grid):
#   smallest = float("+inf")
#   visited = set()
#   for r in range(len(grid)):
#     for c in range(len(grid[r])):
#       if grid[r][c] == 'L' and (r, c) not in visited:
#         size = calculate_island_size(grid, r, c, visited)
#         smallest = min(smallest, size)
#   return smallest

# def calculate_island_size(grid, r, c, visited):
#   queue = deque()
#   queue.append((r, c))
  
#   size = 0
#   dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#   while queue:
#     print(queue)
#     cur = queue.popleft()
#     if cur in visited:
#       continue

#     size += 1
#     visited.add(cur)
#     for d in dirs:      
#       n_r, n_c = cur[0] + d[0], cur[1] + d[1] 
      
#       if n_r < 0 or n_r >= len(grid):
#         continue
#       if n_c < 0 or n_c >= len(grid[0]):
#         continue
#       if grid[n_r][n_c] == 'W':
#         continue
      
#       queue.append((n_r, n_c))
  
#   return size
# DFS
def minimum_island(grid):
  visited = set()
  smallest = float('+inf')
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      size = calculate_island_size(grid, r, c, visited)
      # print(size)
      if size != 0 and size < smallest:
        smallest = size
  return smallest

def calculate_island_size(grid, r, c, visited):
  size = 0
  stack = [(r, c)]
  directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
  while stack:
    row, column = stack.pop()
    if (row, column) in visited:
      continue
    
    if grid[row][column] == "W":
      continue
    
    visited.add((row, column))
    size += 1
    for point in directions:
      node_row, node_column = row + point[0], column+ point[1]
      if node_row >=0 and node_row <len(grid) and node_column >= 0 and node_column < len(grid[row]):
        stack.append((node_row, node_column))
  return size
    
    
  
grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(minimum_island(grid)) # -> 2)

