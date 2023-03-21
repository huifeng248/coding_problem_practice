# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        # if root == q:
        #     print("root-Q", root.val)
        #     return q
        # if root == p: 
        #     print("root-P", root.val)
        #     return p
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # print(left.val, right.val)
        if left and right:
            return root
        if left and not right:
            return left
        if right and not left:
            return right

        

        