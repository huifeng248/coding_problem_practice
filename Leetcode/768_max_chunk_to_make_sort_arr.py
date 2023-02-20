class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # count the number of max in the chunk. the previous chunk's max must be smaller than the next chunk's smallest
        max_num = arr[0]
        stack = []
        for i in arr:
            if  i >= max_num:
                stack.append(i)
                max_num = i
            else: 
                top = stack[-1]
                while len(stack) > 0 and stack[-1]> i:
                    stack.pop()
                
                stack.append(top)
        return len(stack)

# time comeplexity: O(n)
# space comeplexity: O(n)

    
    
arr = [1,0,1,3,2]
s = Solution()
print(s.maxChunksToSorted(arr))