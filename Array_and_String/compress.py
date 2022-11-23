# compress
# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

# test_00:
# compress('ccaaatsss') # -> '2c3at3s'
# test_01:
# compress('ssssbbz') # -> '4s2bz'
# test_02:
# compress('ppoppppp') # -> '2po5p'
# test_03:
# compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
# test_04:
# compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); 
# # -> '127y'


def compress(s):
  s += "#"
  res = ''
  i = 0
  j = 0
  
  while j < len(s):
    if s[i] == s[j]:
      j += 1
    
    else:
      count = j-i
      if count == 1:
        res += s[i]
      else:
        res += str(count) + s[i]
      i = j
  return res


solution
using two pointers
def compress(s):
  s += '!'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1  
    else:
      num = j - i
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num)) 
        result.append(s[i])
      i = j
    
  return ''.join(result)


# n = length of string
# Time: O(n)
# Space: O(n)