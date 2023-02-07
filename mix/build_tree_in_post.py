class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_post(in_order, post_order):
  if len(in_order) == 0:
    return None
  
  val = post_order[-1]
  root = Node(val)
  mid = in_order.index(val)
  left_in_order = in_order[:mid]
  right_in_order = in_order[mid+1:]
  left_post_order = post_order[:mid]
  # print("left", len(left_in_order), "mid", mid)
  # right_post_order = post_order[len(left_in_order):-1]
  # print("right", post_order[len(left_in_order):-1])
  # print("right_mid", post_order[mid:-1])
  right_post_order = post_order[mid:-1]
  root.left = build_tree_in_post(left_in_order, left_post_order)
  root.right = build_tree_in_post(right_in_order, right_post_order)
  
  
  return root

build_tree_in_post(
  [ 'd', 'b', 'e', 'a', 'f', 'c', 'g' ],
  [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
)


# build tree in post
# Write a function, build_tree_in_post, that takes in a list of in-ordered values and a list of post-ordered values for a binary tree. The function should build a binary tree that has the given in-order and post-order traversal structure. The function should return the root of this tree.

# You can assume that the values of inorder and postorder are unique.

# test_00
build_tree_in_post(
  [ 'y', 'x', 'z' ],
  [ 'y', 'z', 'x' ] 
)
#       x
#    /    \
#   y      z
# test_01
build_tree_in_post(
  [ 'd', 'b', 'e', 'a', 'f', 'c', 'g' ],
  [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
)
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g
# test_02
build_tree_in_post(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
)
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
# test_03
build_tree_in_post(
  ['m', 'n'],
  ['m', 'n']
)
#       n
#     /
#    m
# test_04
build_tree_in_post(
  ['n', 'm'],
  ['m', 'n']
)
#     n
#      \
#       m