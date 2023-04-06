# most optimal solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1


# Space Complexity : O(1). Only constant space is used.

# Time Complexity: O(n). However, the total number of operations are optimal. The total operations (array writes) that code does is Number of non-0 elements.This gives us a much better best-case (when most of the elements are 0) complexity than last solution. However, the worst-case (when all elements are non-0) complexity for both the algorithms is same.
            


# # class Solution:
# fill the first half with all non-zeroes and the second half with all zeroes
#     def moveZeroes(self, nums: List[int]) -> None:
#         left = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[left] = nums[i]
#                 left += 1
        
#         for i in range(left, len(nums)):
#             nums[i] = 0

# time complexity: O(n)
# space complexity: O(1)

            



# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         left = 0
#         for i in range(len(nums)-1):
#             if nums[i] == 0 and nums[i+1] != 0:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#             elif nums[i] == 0 and nums[i+1] == 0:
#                 left = i+1
#                 while left < len(nums)-1 and nums[left] == 0:
#                     left += 1
#                 nums[i], nums[left] = nums[left], nums[i]
#         return None

# The time complexity of this code is O(n^2) in the worst case where all elements are 0s and the best case is O(n) when there are no 0s in the array. The space complexity is O(1) because the algorithm uses only a constant amount of extra space regardless of the input size.
            

