def best_bridge(grid):
  result = []
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == 'L' and (r, c) not in visited:
        first_island = find_island(grid, r, c, visited)
        result.append(first_island)
  return result


def find_island(grid, row, column, visited):
  res = []
  stack = [(row, column)]
  while stack:
    r, c = stack.pop()
#     this filter out the visited, and avoid infinite loop.
    if (r, c) in visited:
      continue
  
    visited.add((r,c))
  
    if grid[r][c] == "W":
      continue
    
    res.append((r, c))
    
    directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
    for delta in directions:
      neighbor_row, neighbor_column = r + delta[0], c + delta[1]
      
      valid_row = 0<=neighbor_row < len(grid)
      valid_column = 0 <= neighbor_column < len(grid[r])
      if valid_row and valid_column and (neighbor_row, neighbor_column) not in visited:
        stack.append((neighbor_row,neighbor_column))   
        
  return res
  
  
  





# def best_bridge(grid):
#   visited = set()
#   island_arrs = []
#   for row in range(len(grid)):
#     for column in range(len(grid[row])):
#       island_res = find_island(grid, row, column, visited)
#       if len(island_res):
#         island_arrs.append(island_res)
#   first_island = island_arrs[0]
  
#   shortest_bridge = find_bridge(grid, first_island)
#   return first_island

# from collections import deque
# def find_bridge(grid, first_island):
#   visited = set([tuple(i) for i in first_island ])
  
#   queue = deque()
#   for position in first_island:
#     queue.append([tuple(position), 0])
  
#   while queue:
#     current_postition, level = queue.popleft()
#     row, column = current_postition
    
#     # print("current_postition", current_postition, level)
#     if current_postition not in visited and grid[row][column] == "L":
#       return level -1
    
#     visited.add(current_postition)
#     directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
#     for delta in directions:
#       neighbor_row, neighbor_column = row + delta[0], column + delta[1]
#       valid_row = 0<=neighbor_row < len(grid) 
#       valid_column = 0 <=neighbor_column <len(grid[0])

      
#       if valid_row and valid_column and (neighbor_row,neighbor_column) not in visited:
        
#         queue.append([(neighbor_row, neighbor_column), level+1])   
      

# def find_island(grid, row, column, visited):
#   res = []
#   stack = [(row, column)]
#   while stack:
#     row, column = stack.pop()
#     if (row, column) in visited:
#       continue
  
#     if grid[row][column] == "W":
#       continue
# #     after filtering, the qualified points will be added to result and visited to avoid double count
#     visited.add((row, column))
#     res.append([row, column])
  
#     directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
# #     this keep adding neighbor point into the stack
#     for point in directions:
#       n_r, n_c = row + point[0], column+point[1]
      
#       valid_row = 0<=n_r < len(grid) 
#       valid_column = 0 <=n_c <len(grid[row])
      
#       if valid_row and valid_column:
#         if (n_r, n_c) not in visited:
#           stack.append([n_r, n_c])
          
#   return res
        
grid = [
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W", "W", "W", "L"],
]
print(best_bridge(grid)) # -> 1
    
  
  
  