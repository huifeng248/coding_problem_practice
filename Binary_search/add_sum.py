


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# def tree_sum(root):
#   if root is None:
#     return 0
#   return root.val + tree_sum(root.left) + tree_sum(root.right)

# DFS
# def tree_sum(root):
#   if root is None:
#     return 0
  
#   res = 0
#   stack = [root]
#   while stack:
#     current = stack.pop()
#     res += current.val
#     if current.left is not None:
#       stack.append(current.left)
#     if current.right is not None:
#       stack.append(current.right)
      
#   return res

# BFS
# def tree_sum(root):
#   if root is None:
#     return 0
  
#   res = 0
#   queue = [root]
#   while queue:
#     current = queue.pop(0)
#     res += current.val
#     if current.left is not None:
#       queue.append(current.left)
#     if current.right is not None:
#       queue.append(current.right)
#   return res

# optimal bfs
from collections import deque
def tree_sum(root):
  if root is None:
    return 0
  
  res = 0
  queue = deque([root])
  while queue:
    current = queue.popleft()
    res += current.val
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return res

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

tree_sum(a) # -> 21


# tree sum
# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

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

tree_sum(a) # -> 21
# test_01:
a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

tree_sum(a) # -> 10
# test_02:
tree_sum(None) # -> 0


# solutions
# depth first
def tree_sum(root):
  if root is None:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)
# n = number of nodes
# Time: O(n)
# Space: O(n)
# breadth first
from collections import deque

def tree_sum(root):
  if not root:
    return 0

  queue = deque([ root ])
  total_sum = 0
  while queue:
    node = queue.popleft()

    total_sum += node.val

    if node.left:
      queue.append(node.left)

    if node.right:
      queue.append(node.right)

  return total_sum
# n = number of nodes
# Time: O(n)
# Space: O(n)