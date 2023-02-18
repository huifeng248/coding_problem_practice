class Solution:

    def decodeString(self, s:str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0
        for char in s:
            if char.isalpha():
                cur_str += char
                print("letter", char)
            elif char.isdigit():
                cur_num = cur_num * 10 + int(char)
                print("digit", char)
            elif char == "[":
                stack.append(cur_str)
                stack.append(cur_num)
                cur_num = 0
                cur_str = ""
                print("stack after [", stack)
            elif char == "]":
                print("stack ]", stack)
                num_multi = stack.pop()
                pre_str = stack.pop()
                print("cur_str", cur_str, "prev_str", pre_str, "num_multi", num_multi, "stack", stack)
                cur_str = pre_str + num_multi * cur_str
        return cur_str
            
s = "2[ee]2[3[a2[c]]]"
# s = "2[abc]3[cd]ef"
# s = "3[a]2[bc]"           
    
sample = Solution()
print(sample.decodeString(s))
