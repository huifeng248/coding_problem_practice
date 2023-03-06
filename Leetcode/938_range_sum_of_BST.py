# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        arr = []
        res = 0
        nums = self.dfs(root, arr, low, high)
        print(nums)
        # for num in nums:
        #     if num >= low and num <= high:
        #         res += num
        # return res
        return sum(nums)


    def dfs(self, root, arr, low, high):
        if not root:
            return 
        
        if root.val >= low:
            self.dfs(root.left, arr, low, high)
        # arr.append(root.val)
        if root.val >= low and root.val <= high:
            arr.append(root.val)
        if root.val <= high:
            self.dfs(root.right, arr, low, high)
        return arr
    
