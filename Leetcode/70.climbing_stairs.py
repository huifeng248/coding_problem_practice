class Solution:
    def climbStairs(self, n: int) -> int:
        memo =  {}
        return self.calculating_ways(0, n, memo)
    
    def calculating_ways(self, i, n, memo):
        if i in memo:
            return memo[i]
        
        # means it has pass n step, it's not a valid way
        if i > n:
            return 0
        
        #mean it has reach n steps, it's a valid way, need to add to the result.
        if i == n:
            return 1
        
        memo[i] = self.calculating_ways(i+1, n, memo) + self.calculating_ways(i+2, n, memo)
        return memo[i]
    


# time complexity: O(n)
# space complexity: O(n)
