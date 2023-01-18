def decompress_braces(string):
  stack = []
  nums = "123456789"
  letters = "abcdefghijklmnopqrstuvwxyz"
  temp = ""
  
  for char in string:
    if char in nums or char in letters:
      if char in nums:
        stack.append(int(char))
      else:
        stack.append(char)
    if char == "}":
      pop_letters(stack, "")
      # temp = ""
      # popped = stack.pop()
      # while popped not in nums:
      #   temp = popped + temp
      #   popped = stack.pop()
      # num = stack.pop()
      # temp = num * temp
      # stack.append(temp)
  return ''.join(stack)

def pop_letters(stack, temp=""):
  nums = "123456789"
  tail = stack.pop()
  print("tail", tail)
  if tail in range(0, 10, 1):
    temp = tail * temp
    print("####", temp)
    stack.append(temp)
    print(stack)
    return stack
  else:
    temp = tail + temp
    return pop_letters(stack, temp)
    
    
stack = ["aa", 3, "u", "y"]
# print(pop_letters(stack, ""))

print(decompress_braces("2{q}3{tu}v"))


# decompress braces
# Write a function, decompress_braces, that takes in a compressed string as an argument. The function should return the string decompressed.

# The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.

# You may assume that every number n is guaranteed to be an integer between 1 through 9.

# You may assume that the input is valid and the decompressed string will only contain alphabetic characters.

# test_00:
decompress_braces("2{q}3{tu}v")
# -> qqtututuv 
# test_01:
decompress_braces("ch3{ao}")
# -> chaoaoao
# test_02:
decompress_braces("2{y3{o}}s")
# -> yoooyooos
# test_03:
decompress_braces("z3{a2{xy}b}")
# -> zaxyxybaxyxybaxyxyb 
# test_04:
decompress_braces("2{3{r4{e}r}io}")
# -> reeeerreeeerreeeerioreeeerreeeerreeeerio 
# test_05:
decompress_braces("go3{spinn2{ing}s}")
# -> gospinningingsspinningingsspinningings 
# test_06:
decompress_braces("2{l2{if}azu}l")
# -> lififazulififazul 
# test_07:
decompress_braces("3{al4{ec}2{icia}}")
# -> alececececiciaiciaalececececiciaiciaalececececiciaicia 


# solution
# using a stack
def decompress_braces(string):
  numbers = '123456789'
  stack = []
  for char in string:
    if char in numbers:
      stack.append(int(char))
    else:
      if char == '}':
        segment = ''
        while isinstance(stack[-1], str):
          popped = stack.pop()
          segment = popped + segment
        num = stack.pop()
        stack.append(segment * num)
      elif char != '{':
        stack.append(char)
  return ''.join(stack)
# s = length of string
# m = count of brace pairs
# Time: O((9^m) * s)
# Space: O((9^m) * s)