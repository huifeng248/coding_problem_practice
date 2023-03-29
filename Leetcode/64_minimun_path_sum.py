# dynamic programming depth

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #first col
        for i in range(1, m, 1):
            grid[i][0] += grid[i-1][0]
        # first row
        for i in range(1, n, 1):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, m, 1):
            for j in range(1, n, 1):
                right = grid[i][j-1]
                down = grid[i-1][j]
                grid[i][j] += min(right, down)
        
        return grid[m-1][n-1]

# time complexity: O(mn)
# space complexity:O(1)


# recusion 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        row = col = 0
        memo = {}

        min_val = self.find_min(row, col, grid, memo)
        return min_val
    
    def find_min(self, row, col, grid, memo):
        pos = (row, col)
        if pos in memo:
            return memo[pos]
        
        if row ==len(grid)-1 and col == len(grid[0])-1:
            return grid[row][col]
        
        # the key here is float not 0!!!
        if row >= len(grid) or col >= len(grid[0]):
            return float('inf')

        down = self.find_min(row+1, col, grid, memo)
        right = self.find_min(row, col+1, grid, memo)
        
        memo[pos] = grid[row][col] + min(down, right)
        return memo[pos]


# time complexity:O(mn), where m is the number of rows and n is the number of columns in the input grid. This is because the find_min() function is called once for each cell in the grid, and each call takes constant time to compute, except for the first call, which takes O(m+n) time. Therefore, the overall time complexity is O(mn).

# The space complexity of the updated solution is also O(mn), because we are storing the minimum path sum for each cell in a dictionary called memo. Since there are mn cells in the grid, the memo dictionary has O(mn) space complexity. Additionally, the recursive calls to find_min() also take up O(mn) space in the call stack, because the maximum depth of the recursion is m+n (the length of the longest path from the top left to the bottom right corner of the grid). Therefore, the overall space complexity is O(m*n).

s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(grid))
