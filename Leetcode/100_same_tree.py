
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right


# solution two 

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if q.val != p.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right

# Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.

# Space complexity : O(N) in the worst case of completely unbalanced tree, to keep a recursion stack

        
        

# solution one 
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if p is None and q is None:
#             return True
        
#         if (not p and q) or (p and not q):
#             return False

#         if p.val != q.val:
#             return False 
        
#         stack_p = [[p, 0]]
#         stack_q = [[q, 0]]
#         while stack_p:
#             current_p, direction_p = stack_p.pop()
#             current_q, direction_q = stack_q.pop()

#             if current_p is None and current_q is None:
#                 continue
           
#             if current_p.val != current_q.val or direction_p != direction_q:
#                 return False
#             if current_p.left:
#                 stack_p.append([current_p.left, -1])
#             if current_p.right:
#                 stack_p.append([current_p.right, 1])

#             if current_q.left:
#                 stack_q.append([current_q.left, -1])
#             if current_q.right:
#                 stack_q.append([current_q.right, 1])

#         if not stack_p and stack_q:
#             return False

#         return True

# # Time complexity : O(N) since each node is visited exactly once.
# # Space complexity : O(N)in the worst case


# from collections import deque
# class Solution:
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """    
#         def check(p, q):
#             # if both are None
#             if not p and not q:
#                 return True
        #     # one of p and q is None
        #     if not q or not p:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     return True
        
        # deq = deque([(p, q),])
        # while deq:
        #     p, q = deq.popleft()
        #     if not check(p, q):
        #         return False
            
        #     if p:
        #         deq.append((p.left, q.left))
        #         deq.append((p.right, q.right))
                    
        # return True