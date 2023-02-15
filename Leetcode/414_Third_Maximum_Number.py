class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num_set = list(set(nums))
        num_set.sort(reverse=True)
        print("nums", num_set)
        if len(num_set) < 3:
            return num_set[0]
        else:
            return num_set[2]

        


   