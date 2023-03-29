class Solution:
    def decodeString(self, s:str) -> str:
        cur_digit = 0
        cur_str = ""
        stack = []
        for char in s:
            if char.isdigit():
                cur_digit = cur_digit*10 + int(char)
            elif char == "[":
                stack.append((cur_digit, cur_str))
                cur_digit = 0
                cur_str = ""
            elif char == "]":
                # the naming for these two is the key
                num, prev_str = stack.pop()
                cur_str = prev_str + num*cur_str
            else:
                cur_str += char
        return cur_str
# The time complexity of this algorithm is O(N), where N is the length of the input string, as we iterate through the string character by character. 
# The space complexity is also O(N), as the maximum size of the stack is proportional to the length of the input string.   