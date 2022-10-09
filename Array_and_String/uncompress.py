# uncompress
# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

# <number><char>

# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

# test_00:
# uncompress("2c3a1t") # -> 'ccaaat'
# test_01:
# uncompress("4s2b") # -> 'ssssbb'
# test_02:
# uncompress("2p1o5p") # -> 'ppoppppp'
# test_03:
# uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
# test_04:
# uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'


def uncompress(s):
  # res = ""
  res = []
  letter_idx = 0
  number_idx = 0
  numbers = "0123456789"
  
  for letter_idx in range(0, len(s)):
    if s[letter_idx] in numbers:
      letter_idx += 1
    else:
      num = s[int(number_idx): int(letter_idx)]
      # res += int(num) * s[letter_idx]
      res.append(int(num) * s[letter_idx])
      letter_idx += 1
      number_idx = letter_idx
  return ("").join(res)
  
  print(uncompress("12y5t"))
  
  
#   solution
# using two pointers
def uncompress(s):
  numbers = '0123456789'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:      
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1
      i = j
      
  return ''.join(result)
# n = number of groups
# m = max num found in any group
# Time: O(n*m)
# Space: O(n*m)