class Solution:
    def minSubarray(self, nums, p) -> int:
        sum_l = sum(nums)        
        remainder = sum_l % p
        print("remainder", remainder)
        if remainder == 0:
            return 0
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append((prefix_sum[-1]+num) % p)
        
        print(prefix_sum)
        seen = {0:0}
        min_len = float('inf')
        for i in range(1, len(prefix_sum), 1):
            complement = (prefix_sum[i] - remainder) % p
            # print((prefix_sum[i] - remainder) % p, "i-", i, "ele-", prefix_sum[i], "comp-", complement, "seen key-", seen.keys())
            if complement in seen:
                sub_arr_len = i - seen[complement]
                min_len = min(min_len, sub_arr_len)
            seen[prefix_sum[i]] = i

      
        if min_len == len(nums): # min_len >= len(nums) also work, cause need to rule exausting all prefix 
            return -1
        else:
            return min_len

        


# nums = [8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]
# p = 148
nums = [1,2,3]
p = 7

s = Solution()
print(s.minSubarray(nums, p))


# time complexity is O(N), where N is the length of the input list nums.
# space complexity is O(p), which is the size of the seen dictionary. In the worst case, if all the prefix sums have distinct values, the dictionary will contain p key-value pairs.