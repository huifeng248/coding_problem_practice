class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(grid[0])):
            self.find_excape(0, i, grid, res)
        return res
    
    def find_excape(self, row, col, grid, res):
        # if it can go down the bottom boundary, the ball can drop
        if row == len(grid):
            res.append(col)
            return 
        
        adj_col = col + grid[row][col]
        
        # if the adj_col is out of bound, return -1 or if the adj col is not equal to the origal return -1
        if adj_col < 0 or adj_col >len(grid[0])-1 or (grid[row][col] != grid[row][adj_col]):
            res.append(-1)
            return 
        
        return self.find_excape(row+1, adj_col, grid, res)


# time complexity: O(m*n),  This is because we need to iterate through every column in the first row to determine the final position of each ball.


# space complexity: O(m) the number of rows, which is the maximun depth of the recursive call

        

        


