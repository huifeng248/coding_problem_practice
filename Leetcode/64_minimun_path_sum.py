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




s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(grid))
