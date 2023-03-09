class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_arr = sum(nums)
        prefix_dict = {}
        accu = 0
        for i in range(len(nums)):
            accu += nums[i]
            prefix_dict[i] = accu

        if sum_arr - nums[0] == 0:
            return 0
        
        for i in range(1, len(nums), 1):
            right_sum = sum_arr - prefix_dict[i]
            if right_sum == prefix_dict[i-1]:
                return i
        return -1


# time complexity O(N)
# space complexity O(N)

# optimal space complex solution 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        sum_arr = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = sum_arr - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            
            left_sum += nums[i]
            # left_sum += nums[i]
            # right_sum = sum_arr - left_sum
            # if right_sum == (left_sum - nums[i]):
            #     return i
        return -1

            



