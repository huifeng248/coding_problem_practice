# using sliding window -- easy to follow
from collections import defaultdict, Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_count = Counter(words)
        word_len = len(words[0])
        window_len = word_len * len(words)
        res = []

        for i in range(len(s) - window_len + 1):
            sub_str = s[i: i+window_len]
            sub_str_counter = self.get_counter(sub_str, word_len)

            if sub_str_counter == word_count:
                res.append(i)
        return res
    
    def get_counter(self, sub_str, word_len):
        dict = {}
        for i in range(0, len(sub_str), word_len):
            chars = sub_str[i: i+word_len]
            if chars not in dict:
                dict[chars] = 0
            dict[chars] += 1
        return dict
#     The time complexity of the above code is O(NLM), where N is the length of the input string s, L is the length of each word in words, and M is the number of words in words.
# The space complexity is O(M), as we store the frequency of each word in words in a Counter. 

#     The time complexity of the above code is O(NLM), where N is the length of the input string s, L is the length of each word in words, and M is the number of words in words.

# The reason for this time complexity is that we loop through all possible starting indices of the sliding window word_length times, which takes O(L) time for each iteration. For each starting index, we use a sliding window of length substring_length, which takes O(M*L) time to extract all the words in the substring. We also use a Counter to count the frequency of each word in the substring, which takes O(M) time.

# Therefore, the total time complexity is O(NLM).

# The space complexity of the above code is also O(M), as we store the frequency of each word in words in a Counter. We also use a Counter to store the frequency of each word in the sliding window, which takes up to O(M) space. We also store the results in a list, which takes O(K) space where K is the number of valid starting indices. In the worst case, where all starting indices are valid, K can be up to N/L.

# Therefore, the total space complexity is O(M + K), which can be simplified to O(max(M, N/L)).
    

    # class Solution:
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     if not s or not words:
    #         return []
        
    #     word_count = Counter(words)
    #     word_length = len(words[0])
    #     substring_length = word_length * len(words)
    #     n = len(s)
        
    #     result = []
    #     for i in range(word_length):
    #         # Use a sliding window starting at index i
    #         left, right = i, i
    #         window_count = Counter()
    #         while right + word_length <= n:
    #             word = s[right:right+word_length]
    #             window_count[word] += 1
    #             right += word_length
                
        #         # If the window contains all words in the right count, add to result
        #         if right - left == substring_length:
        #             if window_count == word_count:
        #                 result.append(left)
                    
        #             # Move the window to the right
        #             left_word = s[left:left+word_length]
        #             window_count[left_word] -= 1
        #             if window_count[left_word] == 0:
        #                 del window_count[left_word]
        #             left += word_length
        
        # return result

    

                








# # most brute force Solution using permutation: time complexity is fatorial
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         arr_perms = self.permutation(words)
#         str_perms = []
#         k = len(words[0])
#         length = len(words)
#         str_length = k * length
#         for perm in arr_perms:
#             str_perm = "".join([i for i in perm])
#             str_perms.append(str_perm)
        
#         res = []
#         for i in range(len(s)):
#             if s[i: i+int(str_length)] in str_perms:
#                 res.append(i)
#         return res

#     def permutation(self, words):
#         if len(words) == 0:
#             return [[]]
#         first = words[0]
#         without_first = self.permutation(words[1:])
#         with_first = []
#         for perm in without_first:
#             for i in range(len(perm)+1):
#                 ele = [*perm[:i], first, *perm[i:]]
#                 with_first.append(ele)
#         return with_first

