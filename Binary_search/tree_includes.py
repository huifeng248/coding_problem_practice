class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# def tree_includes(root, target):
#   if root is None:
#     return False
  
#   values = set([])
#   stack = [root]
#   while stack:
#     current = stack.pop()
#     values.add(current.val)
#     if target in values:
#       return True
    
#     if current.left is not None: 
#       stack.append(current.left)
#     if current.right is not None:
#       stack.append(current.right)
#   return False
def tree_includes(root, target):
  if root is None:
    return False
  
  if root.val == target:
    return True
  else:
    return tree_includes(root.left, target) or tree_includes(root.right, target) 
  
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

print(tree_includes(a, "e")) # -> True
# tree includes
# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

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

tree_includes(a, "e") # -> True
# test_01:
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
tree_includes(a, "a") # -> True
# test_02:
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

tree_includes(a, "n") # -> False
# test_03:
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

tree_includes(a, "f") # -> True
# test_04:
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

tree_includes(a, "p") # -> False
# test_05:
tree_includes(None, "b") # -> False


# solutions
# breadth first search
from collections import deque

def tree_includes(root, target):
  if not root:
    return False
  
  queue = deque([ root ])
  
  while queue:
    node = queue.popleft()
    
    if node.val == target:
      return True
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return False
# n = number of nodes
# Time: O(n)
# Space: O(n)
# depth first search
def tree_includes(root, target):
  if not root:
    return False
  
  if root.val == target:
    return True
  
  return tree_includes(root.left, target) or tree_includes(root.right, target)
# n = number of nodes
# Time: O(n)
# Space: O(n)