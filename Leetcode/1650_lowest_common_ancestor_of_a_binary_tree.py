from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_parent = []
        q_parent = []

        self.get_parant(p, p_parent)
        self.get_parant(q, q_parent)

        set_one = set(p_parent)
        for node in q_parent:
            if node in set_one:
                return node
    

    def get_parant(self, child_node, arr):
        current = child_node
        while current:
            arr.append(current)
            current = current.parent
        
        return arr


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
b.parent = a
c.right = f
c.parent = a
e.left = g
e.parent = b
e.right = h
h.parent = e

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
s = Solution()
print(s.lowestCommonAncestor(e, b))