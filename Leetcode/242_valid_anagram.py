from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# time complexity: O(N) N is the length of s or t
# space complexity: O(1)