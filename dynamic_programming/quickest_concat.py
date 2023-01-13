def quickest_concat(s, words):
  res = _quickest_concat(s, words, {})
  if res == float('inf'):
    return -1
  else:
    return res

def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if len(s) == 0:
    return 0
  
  count = 0
  max_count = float('inf')
  for word in words:
    
    if s.startswith(word):
      # print("s", s, "word", word)
      length = len(word)
      count = 1 + _quickest_concat(s[length:], words, memo)
      print("count", count)
  
      max_count = min(max_count, count)
  memo[s] = max_count
  return max_count


# quickest concat
# Write a function, quickest_concat, that takes in a string and a list of words as arguments. The function should return the minimum number of words needed to build the string by concatenating words of the list.

# You may use words of the list as many times as needed.

# test_00:
quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) # -> 2
# test_01:
quickest_concat('caution', ['ion', 'caut', 'caution']) # -> 1
# test_02:
quickest_concat('respondorreact', ['re', 'or', 'spond', 'act', 'respond']) # -> 4
# test_03:
quickest_concat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']) # -> 3
# test_04:
quickest_concat('simchacindy', ['sim', 'simcha', 'acindy']) # -> -1
# test_05:
quickest_concat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu']) # -> 2
# test_06:
quickest_concat('rongbetty', ['wrong', 'bet']) # -> -1
# test_07:
quickest_concat('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', ['u', 'uu', 'uuu', 'uuuu', 'uuuuu']) # -> 7


# solution
# dynamic programming with memoization
def quickest_concat(s, words):
  result = _quickest_concat(s, words, {})
  if result == float('inf'):
    return -1
  else:
    return result

def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if s == '':
    return 0
  
  min_words = float('inf')
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      attempt = 1 + _quickest_concat(suffix, words, memo)
      min_words = min(attempt, min_words)
  
  memo[s] = min_words
  return min_words
# s = length of string
# w = # of words
# Time: ~O(sw)
# Space: O(s)