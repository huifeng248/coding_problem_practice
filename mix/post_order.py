# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def post_order(root, values=[]):
  if root is None:
    return []
  
  post_order(root.left, values)
  post_order(root.right, values)
  values.append(root.val)
  return values
  