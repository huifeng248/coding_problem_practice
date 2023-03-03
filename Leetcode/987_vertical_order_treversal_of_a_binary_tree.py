# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # node_list = []
        row = 0
        col = 0
        node_list = self.get_nodes(root, {}, row, col)

        res = []
        keys = sorted(node_list.keys())
        print(keys)

        for key in keys:
            num_point = len(node_list[key])
            if num_point == 1:
                res.append([node_list[key][0][2]])

            else:
                sorted_sub_list = sorted(node_list[key])
                temp = []
                
                for point in sorted_sub_list:
                    temp.append(point[2])
                res.append(temp)
        return res


    def get_nodes(self, root, node_list, row, col):
        if not root:
            return 
        
        if col not in node_list:
            node_list[col] = []
        node_list[col].append([col, row, root.val])
        
        self.get_nodes(root.left, node_list, row+1, col-1)
        self.get_nodes(root.right, node_list, row+1, col+1)
        return node_list

# time complexity: O(nlog(n) for the sorting
# space complexity: O(M) M is the number of columns 