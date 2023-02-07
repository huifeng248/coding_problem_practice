class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# def build_tree_in_pre(in_order, pre_order):
#   if len(in_order) == 0:
#     return None
#   val = pre_order[0]
#   root = Node(val)
#   mid = in_order.index(val)
  # left_in = in_order[:mid]
#   right_in = in_order[mid+1:]
  # left_pre = pre_order[1:mid+1]
#   right_pre = pre_order[mid+1:]
#   root.left = build_tree_in_pre(left_in, left_pre)
#   root.right = build_tree_in_pre(right_in, right_pre)
#   return root

def build_tree_in_pre(in_order, pre_order):
  end = len(in_order)-1
  result = helper(in_order, pre_order, 0, end, 0, end)
  return result

def helper(in_order, pre_order, in_start, in_end, pre_start, pre_end):
  if in_end < in_start:
    return None
  # print("start", pre_start)
  val = pre_order[pre_start]
  root = Node(val)
  mid = in_order.index(val)
  left_size = mid - in_start
  left = helper(in_order, pre_order, in_start, mid-1, pre_start+1, pre_start+left_size)
  right = helper(in_order, pre_order, mid+1, in_end, pre_start+left_size+1, pre_end)
  root.left = left
  root.right = right  
  return root

build_tree_in_pre(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
)

# solution
# recursive with array copies
def build_tree_in_pre(in_order, pre_order):
  if len(in_order) == 0:
    return None
  value = pre_order[0]
  root = Node(value)
  mid = in_order.index(value)
  left_in_order = in_order[:mid]
  right_in_order = in_order[mid + 1:]
  left_size = len(left_in_order)
  left_pre_order = pre_order[1: 1 + left_size]
  right_pre_order = pre_order[1 + left_size:]
  root.left = build_tree_in_pre(left_in_order, left_pre_order)
  root.right = build_tree_in_pre(right_in_order, right_pre_order)
  return root
# n = length of array
# Time: O(n^2)
# Space: O(n^2)
# recursive in-place
def build_tree_in_pre(in_order, pre_order):
  return _build_tree_in_pre(in_order, pre_order, 0, len(in_order) - 1, 0, len(pre_order) - 1)
  
def _build_tree_in_pre(in_order, pre_order, in_start, in_end, pre_start, pre_end):
  if in_end < in_start:
    return None
  value = pre_order[pre_start]
  root = TreeNode(value)
  mid = in_order.index(value)
  left_size = mid - in_start
  root.left = _build_tree_in_pre(in_order, pre_order, in_start, mid - 1, pre_start + 1, pre_start + left_size)
  root.right = _build_tree_in_pre(in_order, pre_order, mid + 1, in_end, pre_start + left_size + 1, pre_end)
  return root
# n = length of array
# Time: O(n)
# Space: O(n)


# build tree in pre
# Write a function, build_tree_in_pre, that takes in a list of in-ordered values and a list of pre-ordered values for a binary tree. The function should build a binary tree that has the given in-order and pre-order traversal structure. The function should return the root of this tree.

# You can assume that the values of inorder and preorder are unique.

# test_00
build_tree_in_pre(
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ] 
)
#       y
#    /    \
#   z      x
# test_01
build_tree_in_pre(
  [ 'y', 'z', 'x' ],
  [ 'y', 'x', 'z' ] 
)
#       y
#        \
#         x
#        / 
#       z
# test_02
build_tree_in_pre(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
)
#       a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
# test_03
build_tree_in_pre(
  [ 't', 'u', 's', 'q', 'r', 'p' ],
  [ 'u', 't', 's', 'r', 'q', 'p' ] 
)
#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p