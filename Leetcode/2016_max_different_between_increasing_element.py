class Solution:
    
    def maximumDifference(self, nums: List[int]) -> int:
        i = 0
        diff = 0
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                diff = max(diff, nums[j]-nums[i])
            else:
                i = j
        return diff if diff != 0 else -1


# time complexity: O(1)
# space complexity: O(1)