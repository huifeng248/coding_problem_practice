class Solution:
    # think of this like the wave
    # as long as the right is greater then left, keep increase the righ and update res for max
    # if left is greater and right. move left to right, cause we need to start another cycle for increase the right, and mark the res again. 
    def maxProfit(self, prices: List[int]) -> int:
        buy_i = 0
        diff = 0
        for sell_i in range(len(prices)):
            if prices[sell_i] > prices[buy_i]:
                diff = max(diff, prices[sell_i] -prices[buy_i])
            else:
                buy_i = sell_i
        return diff

# time complexity: O(N), n is the length of price
# space complexity: O(1)