def max_path_sum(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    return root.val + max(max_path_sum(root.left),  max_path_sum(root.right))


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def max_path_sum(root):
#   if root is None:
#     return float('-inf')
  
#   if root.left is None and root.right is None:
#     return root.val
  
#   max_left = max_path_sum(root.left)
#   max_right = max_path_sum(root.right)
  
#   return root.val + max(max_left, max_right)

def max_path_sum(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    return root.val + max(max_path_sum(root.left),  max_path_sum(root.right))


# depth first (recursive)
def max_path_sum(root):
  if root is None:
    return float("-inf")

  if root.left is None and root.right is None:
    return root.val

  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))

# n = number of nodes
# Time: O(n)
# Space: O(n)


# this BFS cannot solve the the path question
# def max_path_sum(root):
#   stack = deque([[root,0]])
#   arr = []
#   while stack:
#     current, level = stack.popleft()
#     if level == len(arr):
#       arr.append(current.val)
#     else:
#       temp = arr[level]
#       arr[level] = max(temp, current.val)
    
#     if current.left:
#       stack.append([current.left, level+1])
#     if current.right:
#       stack.append([current.right, level+1])
#     print("arr", arr)
#   return sum(arr)
    