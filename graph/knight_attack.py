from collections import deque
def knight_attack(n, kr, kc, pr, pc):
  visited = set()
  
  queue = deque([(kr, kc, 0)])
  directions = [[-2, 1], [2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2],[-1, -2]]
  
  while queue:
    row, column, level = queue.popleft()
    # print("row", row, "column", column, "level:", level)
    
    if row == pr and column == pc:
      return level
    
    if (row, column) not in visited:
      visited.add((row, column))
    
      for point in directions:
        neighbor_row = row + point[0]
        neighbor_column = column + point[1]
        valid_row = 0<=neighbor_row< n
        valid_column = 0<= neighbor_column < n
      
        if valid_row and valid_column and (neighbor_row, neighbor_column) not in visited:
          queue.append((neighbor_row, neighbor_column, level+1))
  return None
   
print(knight_attack(8, 1, 1, 2, 2)) # -> 2



# favorite
# knight attack
# A knight and a pawn are on a chess board. Can you figure out the minimum number of moves required for the knight to travel to the same position of the pawn? On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction. This means that on a single move, a knight has eight possible positions it can move to.

# Write a function, knight_attack, that takes in 5 arguments:

# n, kr, kc, pr, pc

# n = the length of the chess board
# kr = the starting row of the knight
# kc = the starting column of the knight
# pr = the row of the pawn
# pc = the column of the pawn
# The function should return a number representing the minimum number of moves required for the knight to land ontop of the pawn. The knight cannot move out-of-bounds of the board. You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7. If it is not possible for the knight to attack the pawn, then return None.

# test_00:
knight_attack(8, 1, 1, 2, 2) # -> 2
# test_01:
knight_attack(8, 1, 1, 2, 3) # -> 1
# test_02:
knight_attack(8, 0, 3, 4, 2) # -> 3
# test_03:
knight_attack(8, 0, 3, 5, 2) # -> 4
# test_04:
knight_attack(24, 4, 7, 19, 20) # -> 10
# test_05:
knight_attack(100, 21, 10, 0, 0) # -> 11
# test_06:
knight_attack(3, 0, 0, 1, 2) # -> 1
# test_07:
knight_attack(3, 0, 0, 1, 1) # -> None

# solutions
from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  visited = set();
  visited.add((kr, kc))
  queue = deque([ (kr, kc, 0) ])
  while len(queue) > 0:
    r, c, step = queue.popleft();
    if (r, c) == (pr, pc):
      return step
    neighbors = get_knight_moves(n, r, c)
    for neighbor in neighbors:
      neighbor_row, neighbor_col = neighbor
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor_row, neighbor_col, step + 1))
  return None

def get_knight_moves(n, r, c):
  positions = [
    ( r + 2, c + 1 ),
    ( r - 2, c + 1 ),
    ( r + 2, c - 1 ),
    ( r - 2, c - 1 ),
    ( r + 1, c + 2 ),
    ( r - 1, c + 2 ),
    ( r + 1, c - 2 ),
    ( r - 1, c - 2 ),
  ]
  inbounds_positions = [];
  for pos in positions:
    new_row, new_col = pos
    if 0 <= new_row < n and 0 <= new_col < n:
      inbounds_positions.append(pos)
  return inbounds_positions
# n = length of the board
# Time: O(n^2)
# Space: O(n^2)