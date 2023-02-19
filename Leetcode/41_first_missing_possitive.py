class Solution:
    def firstMissingPositive(self, nums):
        if len(nums) == 1:
            if nums[0] < 1:
                return 1
            elif nums[0] == 1:
                return 2
            elif nums[0]>1:
                return 1
        
        new_list = sorted(nums)
        print("sorted", new_list)
        max_num = new_list[-1]
        if max_num <= 0:
            return 1
        j = 1
        i = 0
        while i < len(nums) and j <= max_num +1:
            if new_list[i] <= 0:
                i += 1
            elif new_list[i] == j:
                i += 1
                j += 1
            elif new_list[i] > j:
                return j    
        return max_num + 1
            
        
        # for i in range(len(nums)):
        #     print("i", i, "num", nums[i])
        #     if new_list[i] <= 0:
        #         i += 1
        #     elif new_list[i] == nums_2[j]:
        #         i += 1
        #         j += 1
        #     elif new_list[i] > nums_2[j]:
        #         res = nums_2[j]
        #         return res
        # return max_num + 1     



# arr = [2147483647]
arr = [1,2,3,10,2147483647,9]
s = Solution()
print(s.firstMissingPositive(arr))
