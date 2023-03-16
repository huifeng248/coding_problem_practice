class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        

        min_i = 0
        max_i = len(nums) -1
        while min_i <= max_i:
            mid = (min_i + max_i) //2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                min_i = mid +1
            else:
                max_i = mid -1
        return -1

# time complexity: (log(n))
# space complexity: (O(1))