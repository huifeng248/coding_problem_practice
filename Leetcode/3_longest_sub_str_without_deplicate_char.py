# # brute force
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         max_len = 0
#         for i in range(len(s)):
#             visited = set()
#             for j in range(i, len(s), 1):
#                 # print("i", i, "j", j, s[j], "visited", visited)
#                 char = s[j]
#                 if char not in visited:
#                     visited.add(char)
#                     # print("visited", visited, len(visited))
#                 else:
#                     break
#             char_length = len(visited)
#             max_len = max(char_length, max_len)
#         return max_len
# # time complexity: O(N^2)
# # space complexity: O(N)

# # sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        visited = set()
        res = 0
        while end < len(s):
            if s[end] not in visited:
                visited.add(s[end])
                end += 1
                res = max(res, len(visited))
            else:
                visited.remove(s[start])
                start += 1
        return res

# time complexity: O(N)
# space complexity: O(N) n is for len of the visited set

# optimize sliding window using harsh table











