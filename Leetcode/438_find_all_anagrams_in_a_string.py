from collections import Counter, defaultdict

# sliding window with harsh map

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        res = []
        p_counter = Counter(p)
        s_counter = Counter()
        i = 0

#because of sliding window, need to go to the end. 
        for i in range(len(s)):
            s_counter[s[i]] += 1
            
            if i >= len(p):
                #remove the left pointer
                s_counter[s[i-len(p)]] -= 1
                if s_counter[s[i-len(p)]] == 0:
                    del s_counter[s[i-len(p)]]
            # after the excluding the left, and adding the right, compare the array
            
            # print(s_counter, p_counter, s_counter == p_counter)
            if s_counter == p_counter:
                res.append(i - len(p)+1)
                print(res)
            
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


