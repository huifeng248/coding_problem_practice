class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def is_binary_search_tree(root):
  # if root is None:
  #   return True

  return helper(root, float('-inf'), float('inf'))

def helper(root, lower, upper):
  if not root:
    return True
  
  if lower > root.val or upper < root.val:
    return False
  print("root", root.val, "lower", lower, "upper", upper,)
  
  left_wing = helper(root.left, lower, root.val-1) 
  print("left~~~~","root", root.val, "lower:", lower, "upper:", upper,"left_wing:", left_wing)
  
  right_wing = helper(root.right, root.val, upper)
  print("right~~~~","root", root.val, "lower:", lower, "upper:", upper,"right_wing:", right_wing)
  
  
  return left_wing and right_wing
  # return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)


a = Node(12)
b = Node(5)
c = Node(19)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     19
#  / \   / \
# 3   9 19   



print(is_binary_search_tree(a)) # -> T