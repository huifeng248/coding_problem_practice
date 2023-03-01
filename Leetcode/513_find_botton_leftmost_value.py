from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    # BFS, the leftmost value will appear first, and the level if greater than the max_level, leftmost value would be updated.
        max_level = float('-inf')
        left_most = root.val
        queue = deque([(root, 0)])

        while queue:
            current, level = queue.popleft()

            if level > max_level:
                max_level = level
                left_most = current.val

            if current.left:
                queue.append((current.left, level +1 ))
            if current.right:
                queue.append((current.right, level+1))

        return left_most


# time complexity: O(n), n is the number of nodes
# space complexity: O(n), n is the number of nodes
