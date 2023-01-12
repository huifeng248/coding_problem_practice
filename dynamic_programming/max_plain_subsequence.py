def max_palin_subsequence(string):
  return _max_palin_subsequence(string, start=0, end=len(string)-1, memo={})

def _max_palin_subsequence(string, start, end, memo={}):
  pos = (start, end)
  if pos in memo:
    return memo[pos]
  
  if start == end:
    return 1
  if start > end:
    return 0
  
  count = 0
  if string[start] == string[end]:
    count = _max_palin_subsequence(string, start+1, end-1, memo) + 2
  else:
    right = _max_palin_subsequence(string, start+1, end, memo)
    left = _max_palin_subsequence(string, start, end-1, memo)
    count = max(left, right)
    
  memo[pos] =count 
  return count 


# def max_palin_subsequence(string, memo={}):
#   if string in memo:
#     return memo[string]
  
#   if len(string) == 0:
#     return 0
#   if len(string) == 1:
#     return 1
  
#   count = 0
#   if string[0] == string[-1]:
#     count = max_palin_subsequence(string[1:-1]) + 2
#   else:
#     right = max_palin_subsequence(string[1:])
#     left = max_palin_subsequence(string[:-1])
#     count = max(left, right)
  
#   memo[string] = count
#   return count 


# print(max_palin_subsequence("luwxult")) 
# print(is_palin("lolt"))

# max palin subsequence
# Write a function, max_palin_subsequence, that takes in a string as an argument. The function should return the length of the longest subsequence of the string that is also a palindrome.

# A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.

# test_00:
max_palin_subsequence("luwxult") # -> 5
# test_01:
max_palin_subsequence("xyzaxxzy") # -> 6
# test_02:
max_palin_subsequence("lol") # -> 3
# test_03:
max_palin_subsequence("boabcdefop") # -> 3
# test_04:
max_palin_subsequence("z") # -> 1
# test_05:
max_palin_subsequence("chartreusepugvicefree") # -> 7
# test_06:
max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") # -> 15
# test_07:
max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") # -> 31


# solution
# dynamic programming with memoization
def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, i, j, memo):
  key = (i, j)
  
  if key in memo:
    return memo[key]
  
  if i == j:
    return 1
  
  if i > j:
    return 0
  
  if string[i] == string[j]:
    memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
  else:
    memo[key] = max(
      _max_palin_subsequence(string, i + 1, j, memo),
      _max_palin_subsequence(string, i, j - 1, memo)
    )
    
  return memo[key]
# n = length of the string
# Time: O(n^2)
# Space: O(n^2)