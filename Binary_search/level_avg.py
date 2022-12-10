class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def level_averages(root):
  value_arr = get_twoD_arr(root)
  return calculate_avg(value_arr)


def get_twoD_arr(root):
  if root is None:
    return []
  stack = [[root, 0]]
  res_arr = []
  while stack:
    [node, level] = stack.pop()
    if len(res_arr) == level:
      res_arr.append([node.val])
    else:
      res_arr[level].append(node.val)
  
    if node.left is not None:
      stack.append([node.left, level+1])
    if node.right is not None:
      stack.append([node.right, level+1])
  return res_arr
    
def calculate_avg(arr):
  res = []
  for sub_arr in arr:
    sub_arr_avg = sum(sub_arr)/len(sub_arr)
    res.append(sub_arr_avg)
  return res

print(calculate_avg([[3], [11,4], [4, -2, 1]]))
    
# level averages
# Write a function, level_averages, that takes in the root of a binary tree that contains number values. The function should return a list containing the average value of each level.

# test_00:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

level_averages(a) # -> [ 3, 7.5, 1 ] 
# test_01:
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

level_averages(a) # -> [ 5, 32.5, 17.5, 2 ] 
# test_02:
a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(45)
g = Node(-1)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0     45
#     /       \
#    -1       -2

level_averages(a) # -> [ -1, -5.5, 14, -1.5 ]
# test_03:
q = Node(13)
r = Node(4)
s = Node(2)
t = Node(9)
u = Node(2)
v = Node(42)

q.left = r
q.right = s
r.right = t
t.left = u
u.right = v

#        13
#      /   \
#     4     2
#      \
#       9
#      /
#     2
#    /
#   42

level_averages(q) # -> [ 13, 3, 9, 2, 42 ]
# test_04:
level_averages(None) # -> [ ]

from statistics import mean

def level_averages(root):
  levels = []
  fill_levels(root, levels, 0)
  
  avgs = []
  for level in levels:
    avgs.append(mean(level))
  return avgs
    
def fill_levels(root, levels, level_num):
  if root is None:
    return
  
  if level_num == len(levels):
    levels.append([ root.val ])
  else:
    levels[level_num].append(root.val)
  
  fill_levels(root.left, levels, level_num + 1)
  fill_levels(root.right, levels, level_num + 1)
# n = number of nodes
# Time: O(n)
# Space: O(n)