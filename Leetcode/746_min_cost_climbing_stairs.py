class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]* len(cost)
        dp[0], dp[1]= cost[0], cost[1]
        for i in range(2, len(cost), 1):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])

#time complexity: O(n)
#space complexity: O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        i = 0
        j = 1
        memo = {}
        start_0 = self.find_min_cost(i, cost, memo)
        start_1 = self.find_min_cost(j, cost, memo)
        return min(start_0, start_1)
        return start_0
    
    def find_min_cost(self, index, cost, memo):
        if index in memo:
            return memo[index]
        if index == len(cost)-1:
            return cost[-1]
        if index >=len(cost):
            return 0
        
        step_one = self.find_min_cost(index+1, cost, memo)+cost[index]
        step_two = self.find_min_cost(index+2, cost, memo)+ cost[index]
        memo[index] = min(step_one, step_two)
        return memo[index]

# time complexity: O(N), where n is the length of the input cost list.
# space complexity:O(N), where n is the length of the input cost list. 