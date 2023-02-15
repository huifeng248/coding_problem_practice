class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Algorithm

        # When going left to right, we'll remember the index prev of the last character C we've seen. Then the answer is i - prev.
        # When going right to left, we'll remember the index prev of the last character C we've seen. Then the answer is prev - i.
        # We take the minimum of these two answers to create our final answer.

        left_res = [None]*len(s)
        right_res = [None]*len(s)
        res = []
        
        prev = float('-inf')
        # check from left
        for i, char in enumerate(s):    
            if char == c:
                prev = i
            left_res[i] = i - prev
        å
        # check from right
        right_prev = float('inf')
        for j in range(len(s)-1, -1, -1):
            right_res[j] = float('inf')
            if s[j] == c:
                right_prev = j
            right_res[j] = right_prev - j
   
        for i in range(len(s)):
            ele = min(left_res[i], right_res[i])
            res.append(ele)
        return res

    # time complexity O(n)
    # space complexity O(n)


        



