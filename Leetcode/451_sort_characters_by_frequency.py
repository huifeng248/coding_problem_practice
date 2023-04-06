from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        pairs = sorted(counter.items(), key= lambda x: (-x[1], x[0]))
        res = ""
        for pair in pairs:
            num = int(pair[1])
            char = pair[0]
            res += (num * char)
        
        return res

# time complexity: nlog(n)
# space complexity: O(n)
# The time complexity of this code is O(nlogn), where n is the length of the input string s. This is because we first create a Counter object to count the frequency of each character, which takes O(n) time. We then sort the pairs in descending order of frequency, which takes O(nlogn) time. Finally, we loop over the sorted pairs to construct the output string, which takes O(n) time.

# The space complexity of this code is also O(n), where n is the length of the input string s. This is because we create a Counter object that stores the count of each character, which can potentially have n distinct keys. We also create a list of pairs that stores these counts, which can have up to n elements. The final output string can be as long as the input string s.