def nesting_score(string):
  stack = []
  for char in string:
    if char == "[":
      stack.append(0)
    else: 
      # char == "]" 
      if stack[-1] == 0:
        stack.pop()
        stack.append(1)
      else:
        temp = 0
        popped = stack.pop()
        while popped != 0:
          temp += popped
          popped = stack.pop()
        
        stack.append(temp * 2)

  return sum(stack)


# solution
# using a stack
def nesting_score(string):
  stack = [0]
  
  for char in string:
    if char == '[':
      stack.append(0)
    else:
      popped = stack.pop()
      if popped == 0:
        stack[-1] += 1
      else:
        stack[-1] += 2 * popped
  
  return stack[0]
# n = length of string
# Time: O(n)
# Space: O(n)