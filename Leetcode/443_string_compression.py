from collections import deque
class Solution:
  # thoughts:
  # have a count to record the difference 
  # have two pointers, left for to write and i for look though the len
  # update the chair in index of write
  # another tip is to convert this to s and update the number count 
    def compress(self, chars: List[str]) -> int:
      write = 0
      i = 1
      count = 1
      while i < len(chars)+1:
        if i < len(chars) and chars[i] == chars[i-1]:
          i += 1
          count += 1
        # two senario would come to this 1) not equal 2) i equal to chars length
        else:
          chars[write] = chars[i-1]
          write += 1
          if count > 1:
            for c in str(count):
              chars[write] = c
              write += 1
          count = 1
          i+= 1
      return write

# time complexity: O(n) where n is the length of the input array, since we iterate through the array once. 
# space complexity: O(1) The space complexity is O(1), since we perform the compression in-place and only use a constant amount of additional memory (for the write and count variables).
      



                


