# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# from collections import deque
# def tree_levels(root):
#   if not root:
#     return []
  
#   queue = deque([root])
#   result = []
#   while queue:
#     result.append([i.val for i in queue])
    
#     next_level_queue = deque()
    
#     while queue:
#       current = queue.popleft()
    
#       if current.left is not None:
#         next_level_queue.append(current.left)
      
#       if current.right is not None:
#         next_level_queue.append(current.right)
  
#     queue = next_level_queue
  
#   return result 

# def tree_levels(root):
#   if root is None:
#     return []
#   result = []
#   stack = [(root, 0)]
  
#   while stack:
#     [current_node, level_num] = stack.pop()
#     if level_num == len(result):
#       result.append([current_node.val])
#     else:
#       result[level_num].append(current_node.val)
    
#     if current_node.right is not None:
#       stack.append((current_node.right, level_num +1))
      
#     if current_node.left is not None:
#       stack.append((current_node.left,level_num +1))
#   return result

# from collections import deque
# def tree_levels(root):
#   if root is None:
#     return []
  
#   queue = deque([[root, 0]])
#   result = []
  
#   while queue:
#     node, level_num = queue.popleft()
    
#     if len(result) == level_num:
#       result.append([node.val])
#     else:
#       result[level_num].append(node.val)
      
#     if node.left is not None:
#       queue.append([node.left, level_num+1])
#     if node.right is not None:
#       queue.append([node.right, level_num+1])
#   return result
  
def tree_levels(root):
  levels = []
  tree_levels_helper(root, levels, level_num=0)
  return levels

def tree_levels_helper(root, levels, level_num):
  if root is None:
    return []
  if len(levels) == level_num:
    levels.append([root.val])
  else:
    levels[level_num].append(root.val)
  
  tree_levels_helper(root.left, levels, level_num+1)
  tree_levels_helper(root.right, levels, level_num+1)
    
# tree levels
# Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree.

# test_00:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]
# test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
#   ['g', 'h', 'i']
# ]
    
# solutions
# breadth first (iterative)
from collections import deque
    
def tree_levels(root):
  if root is None:
    return []
  
  levels = []
  queue = deque([ (root, 0) ])
  while queue:
    current, level_num = queue.popleft()
    
    if len(levels) == level_num:
      levels.append([ current.val ])
    else:
      levels[level_num].append(current.val)
      
    if current.left is not None:
      queue.append((current.left, level_num + 1))
      
    if current.right is not None:
      queue.append((current.right, level_num + 1))
  
  return levels
# n = number of nodes
# Time: O(n)
# Space: O(n)
# depth first (recursive)
def tree_levels(root):
  levels = []
  _tree_levels(root, levels, 0)
  return levels
  
def _tree_levels(root, levels, level_num):
  if root is None:
    return
  
  if level_num == len(levels):
    levels.append([ root.val ])
  else:
    levels[level_num].append(root.val)
  
  _tree_levels(root.left, levels, level_num + 1)
  _tree_levels(root.right, levels, level_num + 1)  
# n = number of nodes
# Time: O(n)
# Space: O(n)  
                   
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  