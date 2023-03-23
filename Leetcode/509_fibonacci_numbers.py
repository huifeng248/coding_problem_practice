class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n == 0: return 0
        if n == 1: return 1
        if n in memo:
            return memo[n]

        memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
    
    # time complexity: O(N) 
    # space complexity: O(N) for the size of stack and memo hash table in use. 