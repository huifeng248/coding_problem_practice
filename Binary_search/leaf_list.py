class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
from collections import deque

def leaf_list(root):
  if root is None:
    return []
  stack = [root]
  res = []
  while stack:
    current = stack.pop()
    if current.left is None and current.right is None:
      res.append(current.val)
    
    if current.right is not None:
      stack.append(current.right) 
    if current.left is not None:
      stack.append(current.left)

  return res
    
  

# leaf list
# Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

leaf_list(a) # -> [ 'd', 'e', 'f' ] 
# test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

leaf_list(a) # -> [ 'd', 'g', 'h' ]
# test_02:
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

leaf_list(a) # -> [ 20, 1, 3, 54 ]
# test_03:
x = Node('x')

#      x

leaf_list(x) # -> [ 'x' ]
# test_04:
leaf_list(None) # -> [ ]


def leaf_list(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [root.val]
  
  return leaf_list(root.left) + leaf_list(root.right)




# solutions
# depth first (iterative)
def leaf_list(root):
  if root is None:
    return [ ]
  
  leaves = []
  
  stack = [ root ]
  while stack:
    current = stack.pop()
    
    if current.left is None and current.right is None:
      leaves.append(current.val)
      
    if current.right is not None:
      stack.append(current.right)
  
    if current.left is not None:
      stack.append(current.left)
  
  return leaves
# n = number of nodes
# Time: O(n)
# Space: O(n)
# depth first (recursive)
def leaf_list(root):
  leaves = []
  _leaf_list(root, leaves)
  return leaves

def _leaf_list(root, leaves):
  if root is None:
    return
  
  if root.left is None and root.right is None:
    leaves.append(root.val)
    
  _leaf_list(root.left, leaves)
  _leaf_list(root.right, leaves)  
# n = number of nodes
# Time: O(n)
# Space: O(n)