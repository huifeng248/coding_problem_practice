# from collections import defaultdict
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # dict = defaultdict(list)
#         if k == len(nums):
#             return nums
#         dict = {}
#         for num in nums:
#             if num not in dict:
#                 dict[num] = 0
#             dict[num] += 1
        
#         # print(dict.items())
#         sorted_dict = sorted(dict.items(), key = lambda x: x[1], reverse=True)
#         sorted_keys = [i[0] for i in sorted_dict]
#         return sorted_keys[:k]

# time O(Nlog(n))
# space O(N)

# Optimal solution 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums        

        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
        
        # buckets = [[] for _ in range(len(nums))] creates a list of separate empty list objects, while buckets = [[]] * len(nums) creates a list of references to the same empty list object is due to the way Python handles list initialization
        buckets = [[] for i in range(len(nums)+1)]
    
        for key in dict.keys():
            value = dict[key]
            buckets[value].append(key)

        flatten = []
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]) != 0:
                #extend used to spread the array, and append it to the list, cause * cannot use here.
                flatten.extend(buckets[i])
        return flatten[:k]


# time O(N)
# space O(N) 