
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # this because the nums is sorted, the least if >0, then the rest must  >0, so skip
            if nums[i] > 0:
                break

            # if i is equal to last one, skip to avoid duplicat ones
            if i == 0 or nums[i-1] != nums[i]:
                self.two_sum(nums, i, res)
        
        return res
    
    def two_sum(self, nums, i, res):
        low, high = i+1, len(nums)-1
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            if sum < 0:
                low += 1
            elif sum >0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -=1
                while low < high and nums[low] == nums[low-1]:
                    low +=1
        
# Time Complexity: O(n2)\mathcal{O}(n^2)O(n 
# 2
#  ). twoSumII is O(n)\mathcal{O}(n)O(n), and we call it nnn times.

# Sorting the array takes O(nlog⁡n)\mathcal{O}(n\log{n})O(nlogn), so overall complexity is O(nlog⁡n+n2)\mathcal{O}(n\log{n} + n^2)O(nlogn+n 
# 2
#  ). This is asymptotically equivalent to O(n2)\mathcal{O}(n^2)O(n 
# 2
#  ).

# Space Complexity: from O(log⁡n)\mathcal{O}(\log{n})O(logn) to O(n)\mathcal{O}(n)O(n), depending on the implementation of the sorting algorithm. 



# back-tracking is too slow
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()

#         res = []
        
#         self.back_tracking(res, 0, nums, [])
    
#         return res
    
#     def back_tracking(self, res, start, nums, combination):
#         if len(combination) == 3 and sum(combination) == 0:
#             res.append(combination.copy())
#             return 
        

#         for i in range(start, len(nums)):
#             if i > start and nums[i] == nums[i-1]:
#                 continue
            
#             combination.append(nums[i])
#             self.back_tracking(res, i+1, nums, combination)
#             combination.pop()

