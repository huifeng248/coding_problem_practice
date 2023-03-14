class Solution:
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