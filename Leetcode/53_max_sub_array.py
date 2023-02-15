class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # solution one : time complexity is n**2, space is one. this would run out of time limit/
        # if len(nums) == 1:
        #     return nums[0]
        
        # max_sum = float('-inf')
        # # current_sum = 0
        # i = 0
        # j = 0
        # for i in range(len(nums)):
        #     current_sum = 0
        #     for j in range(i, len(nums), 1):
        #         current_sum += nums[j]
        #         # current_sum = sum(nums[i:j+1])  this would add the the complexity due to copy arr
        #         max_sum = max(current_sum, max_sum)
        # return max_sum

    # solution two: time complexity is O(n), space is 1
        if len(nums) == 1:
            return nums[0]
        
        max_sum = nums[0]
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(current_sum, max_sum)
            current_sum = max(0, current_sum)
            

        return max_sum


     