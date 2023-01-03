from collections import deque
def best_bridge(grid):
  visited = set()
  arr = []

  for r in range(len(grid)):
    for c in range(len(grid[r])): 
      island = find_island(r, c, grid, visited) 
      if len(island) != 0:
        arr.append(island)
  main_island = arr[0]
  best_bridge = find_bridge(main_island, grid)
        
#       need to break twice to break out of for loop
    #   first_island = find_island(r, c, grid, visited)
    #   if len(first_island) != 0:
    #     break
    # if len(first_island) != 0:
    #   break
  # return first_island
      

  return best_bridge
    
  
def find_bridge(main_island, grid):
  queue = deque([])
  visited = set([tuple(i) for i in main_island])

  for pair in main_island:
    queue.append((pair, 0))
  
  while queue:
    current, level = queue.popleft()
    row, column = current
    
    
    if (row, column) not in visited and [row, column] not in main_island and grid[row][column] =="L":
      return level - 1
    visited.add((row, column))
    directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
    for delta in directions:
      neighbor_row, neighbor_column = row + delta[0], column + delta[1]
      
      valid_row = 0<=neighbor_row < len(grid)
      valid_column = 0 <= neighbor_column < len(grid[row])
      if valid_row and valid_column and (neighbor_row, neighbor_column) not in visited:
        queue.append(([neighbor_row,neighbor_column], level+1))  
    
  


# if island_arr is a pass down, then need to replace   
# island_arr += find_island(r+1, c, grid, visited)
# with find_island(r+1, c, grid, visited)
def find_island(r, c, grid, visited):
  island_arr = []
  if 0 > r or r >= len(grid) or 0 > c or c >=len(grid[r]):
    return []
  if (r, c) in visited:
    return []
  if grid[r][c] == "W":
    visited.add((r, c))
    return []

  island_arr.append([r, c])
  visited.add((r, c))
    
  # print("visited", visited)            
  # print("!!!!", island_arr)
  island_arr += find_island(r+1, c, grid, visited)
  island_arr += find_island(r-1, c, grid, visited)
  island_arr += find_island(r, c+1, grid, visited)
  island_arr += find_island(r, c-1, grid, visited)
  
  return island_arr