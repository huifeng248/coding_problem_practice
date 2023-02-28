# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution one: recursion 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)

# time complexity O(n) n is the number of nodes, as we visit each node once
# space complexity is the height of the trees, if the tress is balance the space complexity would be O(log(n)), if the tree is completely unbalanced, it would be O(n).

# iteration solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [[root, 1]]
        depth = float('-inf')
        while stack:
            node, level = stack.pop()
            if level > depth:
                depth = level
            if node.left:
                stack.append([node.left, level+1])
            if node.right:
                stack.append([node.right, level +1])
        return depth
            
# time complexity O(n) n is the number of nodes, as we visit each node once
# space complexity is the height of the trees, if the tress is balance the space complexity would be O(log(n)), if the tree is completely unbalanced, it would be O(n).