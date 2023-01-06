# def count_paths(grid, row = 0, column = 0, memo={}):
#   pos = (row, column)
#   if pos in memo:
#     return memo[pos]
  
#   if row == len(grid) or column == len(grid[0]):
#     return 0
 
#   if grid[row][column] == "X":
#     return 0
  
#   if row == len(grid) - 1 and column == len(grid[0])-1:
#     return 1
  
#   res = count_paths(grid, row+1, column, memo) + count_paths(grid, row, column+1, memo)
#   memo[pos] = res
#   return memo[pos]
  



def count_paths(grid, start = [0, 0], memo={}):

  end = [len(grid)-1, len(grid[0])-1]
  path = 0
  row, column = start

  if (row, column) in memo:
    return memo[(row, column)]
  if start == end:
    return 1
  
  if row == len(grid) or column == len(grid[0]):
    return 0
  
  directions = [[1, 0], [0, 1]]
 
  for point in directions:
    neighbor_row = row + point[0]
    neighbor_column = column + point[1]
    valid_row = 0<= neighbor_row < len(grid)
    valid_column = 0 <= neighbor_column < len(grid[0])
    
    if valid_column and valid_row and grid[neighbor_row][neighbor_column] != "X":
      path += count_paths(grid, [neighbor_row, neighbor_column], memo)
  
  memo[(row, column)] = path
  return  memo[(row, column)]
    
  
# grid = [
#   ["O", "O", "X"],
#   ["O", "O", "O"],
#   ["O", "O", "O"],
# ]
# print(count_paths(grid)) # -> 2
