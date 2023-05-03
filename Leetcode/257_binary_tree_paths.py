# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# interation 
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         stack = [[root, str(root.val)]]
#         res = []
#         while stack:
#             current, path = stack.pop()
#             if not current.left and not current.right:
#                 res.append(path)
#             if current.left:
#                 stack.append([current.left, path + "->" + str(current.left.val)])
#             if current.right:
#                 stack.append([current.right, path + "->"+ str(current.right.val)])
#         return res         

# Time complexity : O(N) since each node is visited exactly once.
# Space complexity : O(N) as we could keep up to the entire tree.

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.build_path(root, "", res)
        return res

    def build_path(self, root, path, res):
        if not root:
            return 
        if root:
            path += str(root.val)
        
        if not root.left and not root.right:
            res.append(path)
            return 
        
        self.build_path(root.left, path + "->", res)

        self.build_path(root.right, path + "->", res )

# Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
# Space complexity : O(N). Here we use the space for a stack call and for a paths list to store the answer. paths contains as many elements as leafs in the tree and hence couldn't be larger than log⁡N\log NlogN for the trees containing more than one element. Hence the space complexity is determined by a stack call. In the worst case, when the tree is completely unbalanced, e.g. each node has only one child node, the recursion call would occur NNN times (the height of the tree), therefore the storage to keep the call stack would be O(N)\mathcal{O}(N)O(N). But in the best case (the tree is balanced), the height of the tree would be log⁡(N). Therefore, the space complexity in this case would be O(log⁡(N)).
        



