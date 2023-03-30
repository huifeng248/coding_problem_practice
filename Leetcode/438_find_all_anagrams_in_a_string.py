from collections import Counter, defaultdict

# sliding window with harsh map
# we keep increase the window size until P, and compare the two Counter
# when greater then P, we need to move left+1, and update the Counter_s and re-compare. 
# continue this process untill r reach the end.


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = Counter(p)
        counter_s = Counter()
        i = 0
        left = 0
        res = []
        for i in range(len(s)):
            if i < len(p):
                counter_s[s[i]]+=1
            else:
                counter_s[s[left]]-= 1
                counter_s[s[i]]+=1
                if counter_s[s[left]] == 0:
                    del counter_s[s[left]]
                left += 1
            
            if counter_p == counter_s:
                res.append(left)
        return res

# time complexity: O(N) N is the length of s
# space complexity: O(1) becase of limited 26 letters

# solution one: failue the time limit
# from collections import Counter
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         i = 0
#         res = []
#         word_dict = Counter(p)
        
#         for i in range(len(s)-len(p)+1):
#             if s[i] not in word_dict:
#                 i += 1
#             else:
#                 if self.is_anagrams(s, p, i):
#                     res.append(i)
#         return res

#     def is_anagrams(self, s, p, i):
#         word_dict = Counter(p)
#         j = i + len(p)
#         while i < j:
#             if s[i] in word_dict:
#                 word_dict[s[i]]-= 1
#                 if word_dict[s[i]] == 0:
#                     del word_dict[s[i]]
#                 if len(word_dict.keys()) == 0:
#                     return True
#                 i += 1
#             else:
#                 return False 
# time complexity: O(S*P), S is the len of s, and P is the len of p
# speace complexity:O(N), the len of hash map for p


