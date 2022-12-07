class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values(root):
  if root is None:
    return []
  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)
  return [root.val] + left_values + right_values

def depth_first_values(root):
  if root is None:
    return []
  stack = [root]
  result = []
  while stack:
    current = stack.pop()
    # print(current.val)
    result.append(current.val)
    if current.right is not None:
      stack.append(current.right)
    if current.left is not None:
      stack.append(current.left)
  return result





# depth first values
# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

# Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

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

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
# test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
# test_02:
a = Node('a')
#     a
depth_first_values(a) 
#   -> ['a']
# test_03:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b;
b.left = c;
c.right = d;
d.right = e;

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

depth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e']
# test_04:
depth_first_values(None) 
#   -> []


# solutions
# iterative
def depth_first_values(root):
  if not root:
    return []
  
  stack = [root]
  values = []
  
  while stack:
    node = stack.pop()
    values.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return values


# n = number of nodes
# Time: O(n)
# Space: O(n)
# recursive
def depth_first_values(root):
  if not root:
    return []
  
  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)
  return [ root.val, *left_values, *right_values ]
# n = number of nodes
# Time: O(n)
# Space: O(n)