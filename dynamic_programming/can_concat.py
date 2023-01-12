# def can_concat(s, words, memo={}):
#   if s in memo:
#     return memo[s]
#   if s in words:
#     return True
  
#   for word in words:
#     if word in s:
#       # print("word", word)
#       i = s.index(word)
#       length = len(word)
#       # print("slicing", s[:i]+s[i+length:])
#       if can_concat(s[:i]+s[i+length:], words, memo):
#         memo[s] = True
#         return True
#   memo[s] = False
#   return False 

def can_concat(s, words, memo={}):
  if s in memo:
    return memo[s]
  
  if len(s) == 0:
    return True
  
  for word in words:
    if s.startswith(word):
      suffix = len(word)
      if can_concat(s[suffix:], words, memo):
        memo[s] = True
        return True
  memo[s] = False
  return False 
      

# solution
# dynamic programming with memoization
def can_concat(s, words):
  return _can_concat(s, words, {})

def _can_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if s == '':
    return True
  
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      if _can_concat(suffix, words, memo) == True:
        memo[s] = True
        return True
      
  memo[s] = False
  return False
# s = length of string
# w = # of words
# Time: ~O(sw)
# Space: O(s)


      
  
    