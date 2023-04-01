# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        # if root.left and root.right:
        temp = root.right
        root.right = root.left 
        root.left = temp
        
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    
    # time complexity: O(n)
    # space complexity: O(n)
