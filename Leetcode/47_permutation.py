class Solution:
    def permuteUnique(self, nums):
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                print("counter", counter)
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    print("before^^^ counter", counter, "comb", comb, "num", num)
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1
                    print("after backtrack^^^ counter", counter, "comb", comb, "num", num)
        
        def Counter(nums):
            dict = {}
            for num in nums:
                if num not in dict:
                    dict[num] = 1
                else:
                    dict[num] += 1
            # print(dict)
            return dict

        backtrack([], Counter(nums))

        return results


s = Solution()
print(s.permuteUnique([1,1,2]))