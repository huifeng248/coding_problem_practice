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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        counter = {}
        res = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            #instead of using if, it should be while, cause we need to keep shrink the window until the deplicative is excluded. 
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            res = max(r - l+1, res)
        return res












