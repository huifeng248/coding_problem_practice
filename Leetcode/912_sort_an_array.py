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
# The time complexity of the given code is O(nlog(n)) because the merge sort algorithm is used to sort the input array. Merge sort has a time complexity of O(nlog(n)) in the worst-case scenario.
# The space complexity of the code is O(n) because the merge function creates two deques to store the left and right sub-arrays, each with a maximum size of n/2 elements. Additionally, the res list created to store the sorted result has a maximum size of n elements. Therefore, the total space complexity is O(n) due to the use of these data structures in the merge function.


        