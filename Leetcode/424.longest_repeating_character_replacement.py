class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the sliding window keeps increase until we run out of k
        # after k is runout, we keep moving the left to right, until bring the k back to positive and r keep moving to right
        res = 0
        l = 0
        counter = {}
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) +1
            
            if r-l+1 - max(counter.values()) <= k:
                res = max(r - l + 1, res)
            else:
                counter[s[l]] -= 1
                l += 1
        return res
    

# time complexity: O(26n)
# space complexity: O(1), O(26)at most