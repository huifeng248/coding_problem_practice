def breaking_boundaries(m, n, k, r, c):
  res = helper(m, n, k, r, c, 0, {})
  return res 


  
def helper(grid_row, grid_column, max_move, row, column, step, memo):
  key = (row, column, step)
  if key in memo:
    return memo[key]
  
  if (row <= -1 or row >= grid_row or column <= -1 or column >= grid_column) and step <= max_move:
    return 1
  if step == max_move+1:
    return 0
  

  dirs = [[1,0], [0,1], [-1, 0], [0, -1]]
  res = 0
  for pos in dirs:
    n_r = row + pos[0]
    n_c = column + pos[1]
    # print(n_r, n_c)
    res += helper(grid_row, grid_column, max_move, n_r, n_c, step+1, memo)
  
  memo[key] = res
  
  return res


# solution
# dynamic programming with memoization
def breaking_boundaries(m, n, k, r, c):
  return _breaking_boundaries(m, n, k, r, c, {})

def _breaking_boundaries(m, n, k, r, c, memo):
  key = (k, r, c)
  if key in memo:
    return memo[key]
  
  row_inbounds = 0 <= r < m
  col_inbounds = 0 <= c < n
  if not row_inbounds or not col_inbounds:
    return 1
  
  if k == 0:
    return 0
  
  count = 0
  
  deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for delta in deltas:
    d_row, d_col = delta
    count += _breaking_boundaries(m, n, k - 1, r + d_row, c + d_col, memo)
    
  memo[key] = count
  return count
# m = # rows
# n = # columns
# k = # moves
# Time: O(mnk)
# Space: O(mnk)