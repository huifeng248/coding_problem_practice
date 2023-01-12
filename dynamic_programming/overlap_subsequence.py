def overlap_subsequence(string_1, string_2, memo={}):
  pair = (string_1, string_2)
  
  if pair in memo:
    return memo[pair]
  
  if len(string_1)== 0 or len(string_2) == 0:
    return 0
  
  count = 0
  if string_1[0] == string_2[0]:
    count = 1 + overlap_subsequence(string_1[1:], string_2[1:])
  else:
    right = overlap_subsequence(string_1[1:], string_2)
    left = overlap_subsequence(string_1, string_2[1:])
    count = max(left, right)
    
    memo[pair] = count
  return count 

def overlap_subsequence(string_1, string_2, index_1=0, index_2=0, memo={}):
  key = (index_1, index_2)
  if key in memo:
    return memo[key]
  
  if index_1 == len(string_1) or index_2 == len(string_2):
    return 0
  
  count = 0
  if string_1[index_1] == string_2[index_2]:
    count = 1 + overlap_subsequence(string_1, string_2, index_1+1, index_2+1, memo)
  else:
    count = max(
    overlap_subsequence(string_1, string_2, index_1+1, index_2, memo),
    overlap_subsequence(string_1, string_2, index_1, index_2+1, memo)      
    )

  memo[key] = count
  return count 


# overlap subsequence
# Write a function, overlap_subsequence, that takes in two strings as arguments. The function should return the length of the longest overlapping subsequence.

# A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.

# test_00:
overlap_subsequence("dogs", "daogt") # -> 3
# test_01:
overlap_subsequence("xcyats", "criaotsi") # -> 4
# test_02:
overlap_subsequence("xfeqortsver", "feeeuavoeqr") # -> 5
# test_03:
overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave") # -> 11
# test_04:
overlap_subsequence(
  "mumblecorebeardleggingsauthenticunicorn",
  "succulentspughumblemeditationlocavore"
) # -> 15


# solution
# dynamic programming with memoization
def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, i, j, memo):
  key = (i, j)
  if key in memo:
    return memo[key]
  
  if i == len(string_1) or j == len(string_2):
    return 0
  
  if string_1[i] == string_2[j]:
    memo[key] = 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
  else:
    memo[key] = max(
      _overlap_subsequence(string_1, string_2, i + 1, j, memo),
      _overlap_subsequence(string_1, string_2, i, j + 1, memo)
    )
  return memo[key]
# n = length of str1
# m = length of str2
# Time: O(nm)
# Space: O(nm)