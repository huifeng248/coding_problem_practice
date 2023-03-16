class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
        
        # print(char_dict)
        values = sorted(char_dict.values())
        # print(values)
        
        res = 0
        add_odd = False
        for i in range(len(values)-1, -1, -1):
            value = values[i]
            # print(value)
            if value % 2 == 0:
                res += value
            else:
                res += (value - 1)
                add_odd = True
            
        if add_odd:
            res += 1

        return res

# time complexity: O(N)
# space complexity:O(1), the space is the dict to store the number of the unique of char in s, since it's fixed, max 52. it's O(1)