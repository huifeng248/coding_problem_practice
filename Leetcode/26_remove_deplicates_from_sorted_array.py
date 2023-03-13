class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        j = 0
        i = 1

        while i < len(nums):
            next = nums[i]
            current = nums[j]
            if next > current:
                j += 1
                nums[j] = next
                i += 1
                
            if next == current:
                i += 1
        return j+1

# time complexity: O(N)
# space complexity: O(1)
