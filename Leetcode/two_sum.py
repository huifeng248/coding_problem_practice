class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, num in enumerate(nums):
            if num not in diffs:
                comp = target - num
                diffs[comp] = i
            else:
                return [diffs[num], i]

# time complexity O(n)
# space complexity O(n)
