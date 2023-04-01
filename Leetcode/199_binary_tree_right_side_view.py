# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([[root, 0]]) 
        res = []
        while queue:   
            current, level = queue.popleft()
            if level == len(res):
                res.append(current.val)
            if current.right:
                queue.append([current.right, level+1])
            if current.left:
                queue.append([current.left, level+1])
        return res


# time complexity: O(N)
# space complexity: O(N)
