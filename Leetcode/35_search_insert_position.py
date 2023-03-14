class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        print("target", target)
        min_i = 0
        max_i = len(nums)-1
        while min_i <= max_i: 
            
            mid = (max_i + min_i)//2  
            # print("Min", min_i, "max", max_i, "mid", mid, "target", target, "middle", nums[mid])
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                min_i = mid +1 
            elif target < nums[mid]:
                max_i = mid -1
        return min_i


# Time complexity : O(log⁡N)
# Space complexity : O(1)