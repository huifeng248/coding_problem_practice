class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        path = self.find_unique(0, 0, m, n, memo)
        return path
    
    def find_unique(self, row, col, m, n, memo):
        pos = (row, col)
        if pos in memo:
            return memo[pos]
        if row == m - 1 and col == n - 1:
            return 1
        
        if row >=m or col >= n:
            return 0
        
        down = self.find_unique(row+1, col, m, n, memo)
        right = self.find_unique(row, col+1, m, n, memo)
        memo[pos] = down + right
        return memo[pos]

# time complexity: O(m*n), each call goes through the complete grid of m*n cells exactly once. The uniquePaths function makes a single call to find_unique, so its time complexity 
# space complexity: O(m*n), The space complexity of the given code is O(mn) as we are using memoization to store the results of subproblems in the memo dictionary, which can have up to m*n key-value pairs. Additionally, each recursive call uses some space on the stack, but the maximum depth of the recursive call stack is limited to m+n-1, which is the number of steps required to reach the bottom-right corner from the top-left corner. Therefore, the overall space complexity of the algorithm is O(mn).
    