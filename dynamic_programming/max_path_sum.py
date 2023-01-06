def max_path_sum(grid, r = 0, c = 0, memo={}):
  pos = (r,  c)
  if pos in memo:
    return memo[pos]
  
  if r == len(grid) or c ==len(grid[0]):
    return 0
  if r == len(grid)-1 and c == len(grid[0])-1:
    return grid[r][c]

  
  path = grid[r][c]
  
  down = max_path_sum(grid, r+1, c, memo)
  right = max_path_sum(grid, r, c+1, memo)
  path += max(down, right)
  memo[pos] = path
  return path

# max path sum
# Write a function, max_path_sum, that takes in a grid as an argument. The function should return the maximum sum possible by traveling a path from the top-left corner to the bottom-right corner. You may only travel through the grid by moving down or right.

# You can assume that all numbers are non-negative.

# test_00:
grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
max_path_sum(grid) # -> 18
# test_01:
grid = [
  [1, 2, 8,  1],
  [3, 1, 12, 10],
  [4, 0, 6,  3],
]
max_path_sum(grid) # -> 36
# test_02:
grid = [
  [1, 2, 8, 1],
  [3, 10, 12, 10],
  [4, 0, 6, 3],
]
max_path_sum(grid) # -> 39
# test_03:
grid = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
max_path_sum(grid) # -> 27
# test_04:
grid = [
  [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
  [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
  [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
max_path_sum(grid) # -> 56