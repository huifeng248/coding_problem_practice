# solution 4 
def string_search(grid, s):
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if find_string(r, c, grid, s, set(), 0):
        return True
  return False 

def find_string(r, c, grid, s, visited, index):
  if index == len(s):
    return True
  
  valid_row = 0 <= r < len(grid)
  valid_column = 0 <= c < len(grid[0])
  
  pos = (r, c)
  if pos in visited:
    return False
  # visited.add(pos)
  
  if not valid_row or not valid_column:
    return False
  
  char = grid[r][c]
  if char != s[index]:
    # visited.remove(pos)
    return False
  
  # index += 1
  visited.add(pos)
  # grid[r][c] = "*"
  # print("up", (r, c), grid[r][c])
  
  res = find_string(r+1, c, grid, s, visited, index+1) or find_string(r-1, c, grid, s, visited, index+1) or find_string(r, c+1, grid, s, visited, index+1) or find_string(r, c-1, grid, s, visited, index+1)

  # grid[r][c] = char
  # print("down", (r, c), grid[r][c])
  visited.remove(pos)
  return res

    

# # solution three -- working but the logit not so clear
# def string_search(grid, s):
#   visited = set()
#   for r in range(len(grid)):
#     for c in range(len(grid[r])):
#       if grid[r][c] == s[0]:
#         if helper(r, c, grid, s, visited):
#           return True
#   return False

# def helper(row, column, grid, s, visited):
#   stack = [(row, column)]
#   i = 0
#   while stack:
#     # print("stack", stack)
#     r, c = stack.pop()
#     current = (r, c)
#     if current not in visited: 
#       visited.add(current)
#     if grid[r][c] == s[i]:
#       i += 1
#       if i == len(s):
#         return True
#       else:
#         dirs = [[1,0], [-1,0], [0,1],[0, -1]]
#         for point in dirs:
#           n_r = r + point[0]
#           n_c = c + point[1]
#           valid_row = 0 <=n_r < len(grid)
#           valid_column = 0 <= n_c <len(grid[0])
#             # why this line is not working
#           # if valid_row and valid_column and (n_r, n_c) not in visited: 
#           if valid_row and valid_column:
#             stack.append((n_r, n_c))
#   return False 

# # solution one  --working
# def string_search(grid, s):
#   visited = set()
#   for r in range(len(grid)):
#     for c in range(len(grid[0])):    
#       if dfs(grid, r, c, s):
#         return True
#   return False

# def dfs(grid, r, c, s):
#   if s == '':
#     return True
  
#   row_inbounds = 0 <= r < len(grid)
#   col_inbounds = 0 <= c < len(grid[0])
#   if not row_inbounds or not col_inbounds:
#     return False
  
#   char = grid[r][c]
#   if char != s[0]:
#     return False
  
#   suffix = s[1:]
  
#   grid[r][c] = '*'
  
#   result = dfs(grid, r + 1, c, suffix) or dfs(grid, r - 1, c, suffix) or dfs(grid, r, c + 1, suffix) or dfs(grid, r, c - 1, suffix)
#   grid[r][c] = char
#   return result

# solution two --working 
# def string_search(grid, s):
#   # visited = set()  must not put visited in as a argument, as it need to create copy for its branch
#   for r in range(len(grid)):
#     for c in range(len(grid[0])):    
#       if dfs(grid, r, c, s, set()):
#         return True
#   return False

# def dfs(grid, r, c, s, visited):
#   if s == "":
#     return True
  
#   pos = (r, c)
#   if pos in visited:
#     return False
#   visited.add(pos)
  
#   valid_row = 0 <= r < len(grid)
#   valid_column = 0 <= c < len(grid[0])
#   if not valid_column or not valid_row:
#     return False
#   if grid[r][c] != s[0]:
#     return False
#   s = s[1:]
#   # print((r, c), "visited", visited) crate copy of visited set is the key, and the time complexity is n, as add one item at a time
#   return dfs(grid, r-1, c, s, visited.copy()) or dfs(grid, r+1, c, s, visited.copy()) or dfs(grid, r, c-1, s, visited.copy()) or dfs(grid, r, c+1, s, visited.copy())
    

grid = [
  ['a', 'b', 'a'],
  ['t', 'x', 'x'],
  ['x', 'x', 'x'],
];
print(string_search(grid, 'abat')) # -> true


# string search
# Write a function, string_search, that takes in a grid of letters and a string as arguments. The function should return a boolean indicating whether or not the string can be found in the grid as a path by connecting horizontal or vertical positions. The path can begin at any position, but you cannot reuse a position more than once in the path.

# You can assume that all letters are lowercase and alphabetic.

# test_00:
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'hello') # -> True
# test_01:
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'proxy') # -> True
# test_02:
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'rolling') # -> False
# test_03:
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'z', 'm']
]
string_search(grid, 'zoo') # -> False
# test_04:
grid = [
  ['q', 'w', 'h', 'i', 'j'],
  ['q', 'e', 'r', 'o', 'p'],
  ['h', 'y', 't', 'x', 'z'],
  ['k', 'o', 'm', 'o', 'p']
]
string_search(grid, 'qwerty') # -> True
# test_05:
grid = [ 
  [ 'f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p' ], 
  [ 'o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v' ], 
  [ 'g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n' ], 
  [ 'a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm' ], 
  [ 'm', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c' ], 
  [ 'q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z' ], 
  [ 'd', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k' ], 
  [ 'f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w' ], 
  [ 'p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i' ], 
  [ 'l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q' ] 
]
string_search(grid, 'paprika') # -> True
# test_06:
grid = [
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h' ],
]
string_search(grid, 'ssssssssssh') # -> False
# test_07:
grid = [
  ['a', 'b', 'a'],
  ['t', 'x', 'x'],
  ['x', 'x', 'x'],
];
string_search(grid, 'abat') # -> true
    
        