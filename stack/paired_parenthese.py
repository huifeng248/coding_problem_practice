def paired_parentheses(string):
  count = {}
  count["("] = 0
  for char in string:
    if char == "(":
      count["("] += 1
    elif char == ")":
      count["("] -= 1
      if count["("] < 0:
        return False
      
  if count["("] == 0:
    return True
  else:
    return False 

# solution
# using a counter
def paired_parentheses(string):
  count = 0
  
  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      if count == 0:
        return False
      count -= 1
      
  return count == 0
# n = length of string
# Time: O(n)
# Space: O(1)

# paired parentheses
# Write a function, paired_parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

# You may assume the string contains only alphabetic characters, '(', or ')'.

# test_00:
paired_parentheses("(david)((abby))") # -> True
# test_01:
paired_parentheses("()rose(jeff") # -> False
# test_02:
paired_parentheses(")(") # -> False
# test_03:
paired_parentheses("()") # -> True
# test_04:
paired_parentheses("(((potato())))") # -> True
# test_05:
paired_parentheses("(())(water)()") # -> True
# test_06:
paired_parentheses("(())(water()()") # -> False
# test_07:
paired_parentheses("") # -> True
# test_08:
pairedParentheses("))()") # False