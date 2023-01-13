def befitting_brackets(string):
  stack = []
  bracket = {
    "{": "}",
    "[": "]",
    "(": ")"
  }
  
  for char in string:
    if char in bracket: 
      stack.append(bracket[char])
    else:
      if char in stack and stack[-1] == char:
        stack.pop()
      else: 
        return False 
  return len(stack) == 0
  
  
  
  
# def befitting_brackets(string):
#   count = {}
#   open_brackets = "({["
#   close_brackets = "]})"
#   count["("] = count["["] = count["{"] = 0
#   for index, char in enumerate(string):
#     print(index, char)
#     if char == "(":
#       count["("] += 1
#     elif char == ")":
#       count["("] -= 1
#       if count["("] < 0: return False
#       if string[index-1] in open_brackets and string[index-1] != "(": return False 
    
#     elif char == "[":
#       count["["] += 1
#     elif char == "]":
#       count["["] -= 1
#       if count["["] < 0: return False
#       if string[index-1] in open_brackets and string[index-1] != "[": return False 
    
#     elif char == "{":
#       count["{"] += 1
#     elif char == "}":
#       count["{"] -= 1
#       print("come here")
#       if count["{"] < 0: return False
#       if string[index-1] in open_brackets and string[index-1] != "{": return False 
    
#   return count["["] == count["{"] == count["("] == 0
    

  
print(befitting_brackets('[][}'))


# befitting brackets
# Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

# You may assume the string contains only characters: ( ) [ ] { }

# test_00:
befitting_brackets('(){}[](())') # -> True
# test_01:
befitting_brackets('({[]})') # -> True
# test_02:
befitting_brackets('[][}') # -> False
# test_03:
befitting_brackets('{[]}({}') # -> False
# test_04:
befitting_brackets('[]{}(}[]') # -> False
# test_05:
befitting_brackets('[]{}()[]') # -> True
# test_06:
befitting_brackets(']{}') # -> False
# test_07:
befitting_brackets('') # -> True
# test_08:
befitting_brackets("{[(}])") # -> False


# solution
# using a stack
def befitting_brackets(string):
  stack = []
  
  brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
  }
  
  for char in string:
    if char in brackets:
      stack.append(brackets[char])
    else:
      if stack and stack[-1] == char:
        stack.pop()
      else:
        return False
      
  return len(stack) == 0
# n = length of string
# Time: O(n)
# Space: O(n)
