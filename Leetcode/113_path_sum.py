# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive 
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.find_path(root, [root.val], root.val, targetSum, res)
        return res
    def find_path(self, current, path, accu, targetSum, res):
        if not current:
            return 
        
      
        if not current.right and not current.left and accu == targetSum:
            res.append(path)
            return 
        
        if current.left:
            self.find_path(current.left, path+[current.left.val], accu+current.left.val, targetSum, res)
        if current.right:
            self.find_path(current.right, path+[current.right.val], accu+current.right.val, targetSum, res)

        




#iteration
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         if not root:
#             return []
#         stack = [[root, [root.val]]]
#         res = []
#         while stack:
#             current, path = stack.pop()
#             total = sum(path)
            
#             if total == targetSum and not current.left and not current.right:
#                 res.append(path)
                
#             else:
#                 if current.left:
#                     stack.append([current.left, path+[current.left.val]])
#                 if current.right:
#                     stack.append([current.right, path+[current.right.val]])
        
#         return res

# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         if not root:
#             return []
#         res = []
#         stack = [[root, [root.val]]]
#         while stack:
#             current, path = stack.pop()
#             total = sum(path)
#             if not current.left and not current.right and total == targetSum:
#                 res.append(path)
            
#             if current.left:
#                 stack.append([current.left, path+[current.left.val]])
#             if current.right:
#                 stack.append([current.right, path+[current.right.val]])
        
#         return res


# more optimized iteration solution 
# def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
#         ans = []
        
#         if not root:
#             return ans
        
#         stack = [(root,targetSum,[])]
        
#         while stack:
            
#             node, cur_sum, path = stack.pop()
            
#             cur_sum -= node.val
#             path = path + [node.val]
            
#             if not node.left and not node.right and cur_sum == 0:
#                 ans.append(path)
            
#             if node.left:
#                 stack.append((node.left,cur_sum,path))
#             if node.right:
#                 stack.append((node.right,cur_sum,path))
        
#         return ans