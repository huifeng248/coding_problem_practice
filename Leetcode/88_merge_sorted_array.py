class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # solution one: use build-in sort
        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        
        # nums1.sort()
    # time complexity nlog(n)
    # space o(1)

        # solution two: use three pointers and from the end
        pointer_1 = m-1
        pointer_2 = n-1

        for i in range(m+n-1, -1, -1):
            if pointer_2 < 0:
                break
            if pointer_1 >= 0 and nums1[pointer_1] >= nums2[pointer_2]:
                nums1[i] = nums1[pointer_1]
                pointer_1 -= 1
            else:
                nums1[i] = nums2[pointer_2]
                pointer_2 -= 1
   # time complexity n
    # space o(1)
            