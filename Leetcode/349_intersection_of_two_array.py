class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        set_1 = set(nums1)
        for num in nums2:
            if num in set_1:
                res.add(num)

        return list(res)

# Time complexity: O(m+n): m is the len of num1, and n is the len of num2
# Space complexity: O(m)): m is the len of num1
