class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        res = []
        for i in range(0, len(nums)-1, 2):
            num = nums[i]
            char = nums[i+1]
            ele = [char for j in range(num)]
            res += ele
        return res 
    

# The time complexity of the expression "ele = [char for j in range(num)]" is O(num), where num is the length of the list that is being created.

# In this case, the expression is used inside a loop that runs n/2 times, where n is the length of the input list. Therefore, the overall time complexity of this code is O(n*num), which simplifies to O(n^2) in the worst case where all runs are of length 1.

# It's worth noting that the space complexity of this expression is also O(num), as it creates a list of length num. However, since the expression is only called a few times, and the dominant factor for the space complexity is the output list res, the overall space complexity of the code is O(n).