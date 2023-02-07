def lexical_order(word_1, word_2, alphabet):
  for i in range(min(len(word_1), len(word_2))):
    if word_1[i] != word_2[i]:
      if alphabet.index(word_1[i]) < alphabet.index(word_2[i]):
        return True
      elif alphabet.index(word_1[i]) > alphabet.index(word_2[i]):
        print(word_1[i])
        return False
  
  if len(word_2) >=len(word_1):
    return True
  else:
    return False
  
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(lexical_order("backs", "backdoor", alphabet)) # -> False

def lexical_order(word_1, word_2, alphabet):
  length = max(len(word_1), len(word_2))
  for i in range(length): 
    value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf')
    value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')
    if value_1 < value_2:
      return True
    elif value_2 < value_1:
      return False
  return True
# n = length of shorter string
# Time: O(n)
# Space: O(1)

# exical order
# Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. The function should return True if the first word should appear before the second word if lexically-ordered according to the given alphabet order. If the second word should appear first, then return False.

# Note that the alphabet string may be any arbitrary string.

# Intuitively, Lexical Order is like "dictionary" order:

# You can assume that all characters are lowercase a-z.

# You can assume that the alphabet contains all 26 letters.

# test_00:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lexical_order("apple", "dock", alphabet) # -> True
# test_01:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lexical_order("apple", "ample", alphabet) # -> False