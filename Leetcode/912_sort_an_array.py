from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        res = self.merge(left, right)
        return res
    
    def merge(self, left, right):
        left = deque(left)
        right = deque(right)
        res = []
        while left and right:
            if left[0] <= right[0]:
                res.append(left[0])
                left.popleft()
            else:
                res.append(right[0])
                right.popleft()
        if left:
            res += left
        if right: 
            res += right
        return res
        
# time complexity: O(nlog(n))
# spece complexity: tbd


        