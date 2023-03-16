from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = []

        queue = deque([(root, 0)])
        while queue:
            current, level = queue.popleft()
            if len(res) == level:
                res.append([current.val])
            else: 
                res[level].append(current.val)
            
            if current.left:
                queue.append([current.left, level +1])
            if current.right:
                queue.append([current.right, level+1])
        
        return res

# time complexity is O(n), where n is the total number of nodes in the input binary tree. This is because the function visits each node exactly once, and the popleft operation on the queue takes constant time.

# space complexity is also O(n), where n is the total number of nodes in the input binary tree. This is because the function uses a queue to store the nodes, and the maximum number of nodes that can be stored in the queue at any given time is the number of nodes in the widest level of the binary tree. In the worst case, when the input binary tree is a complete binary tree, the widest level will have n/2 nodes, so the space complexity will be O(n/2) = O(n).