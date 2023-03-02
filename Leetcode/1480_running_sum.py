class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        run_sum = [None] * arr_len
        accu = 0
        for i in range(len(nums)):
            accu += nums[i]
            run_sum[i] = accu
        
        return run_sum

# time complexity O(n)
# space complexity O(n)