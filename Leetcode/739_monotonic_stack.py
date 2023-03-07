def monotonicStack(nums):
    n = len(nums)
    stack = []
    
    for i in range(n):
        while len(stack) > 0 and stack[-1] >= nums[i]:
            stack.pop()
        
        stack.append(nums[i])
    
    return stack


nums = [2, 3, 7, 24, 4, 6, 19]
print(monotonicStack(nums))

class Solution:
    def dailyTemperatures(self, temp):
        st = []
        n = len(temp)
        answer = [0] * n

        for i in range(n):
            while st and temp[st[-1]] < temp[i]:
                print("stack", st, "i", i)
                answer[st[-1]] = i - st[-1]
                print("answer", answer)
                st.pop()
            st.append(i)
        return answer
    
s = Solution()
print(s.dailyTemperatures(nums))

#  Monotonic Stack

# # naive Solution: time out for some cases

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         if len(temperatures) == 1:
#             return [0]
#         res = []
#         i = 0
#         for i in range(len(temperatures)):
#             interval = 1
#             j = i+1
        #     while j < len(temperatures) and temperatures[j] <= temperatures[i]:
        #         j += 1
        #         interval +=1
            
        #     if j == len(temperatures):
        #         res.append(0)
        #     else:
        #         # print(res)
        #         res.append(interval)
        # return res


# solution 2
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
#         stack = []
#         for index, temp in enumerate(temperatures):
#             while stack and temperatures[stack[-1]] < temp:
#                 prev_day = stack.pop()
#                 res[prev_day] = index - prev_day
#             stack.append(index)
#         return res

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)
        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
# time complexity: O(N): each element can only be added to the stack once, which means the stack is limited to NNN pops. 

# Space complexity: O(N): If the input was non-increasing, then no element would ever be popped from the stack, and the stack would grow to a size of N elements at the end.

# Note: answer does not count towards the space complexity because space used for the output format does not count.
