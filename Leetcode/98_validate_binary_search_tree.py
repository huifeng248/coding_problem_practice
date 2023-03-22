# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        res = []
        self.build_arr(root, res)

        if self.sorted_arr(res):
            return True
        else:
            return False

    
    def build_arr(self, root, arr):
        if not root:
            return 
        print("root", root.val)
        if root.left:
            self.build_arr(root.left, arr)
        
        print("~~~~root", root.val)
        arr.append(root.val)
        
        if root.right:
            self.build_arr(root.right, arr)

        return arr



    def sorted_arr(self, arr):
        if len(arr) == 0:
            return True
        
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False 
        return True
        

    
# The time complexity of the given code is O(n), where n is the number of nodes in the binary tree. The build_arr function is called recursively on each node, and each node is visited once. In addition, the sorted_arr function performs a linear scan of the resulting array to check if it is sorted, which takes O(n) time in the worst case.

# The space complexity of the code is O(n) as well, where n is the number of nodes in the binary tree. This is because the build_arr function uses a list to store the node values in sorted order, which can have a maximum size of n. Additionally, since the build_arr function is called recursively on each node, the maximum depth of the recursive call stack is also O(n), which contributes to the overall space complexity.

        

