# selution three
def token_transform(s, tokens):
  i = 0
  j = 1
  res = ""
  while i < len(s):
    if s[i] != "$":
      res += s[i]
      i += 1
      j = i + 1
      
    elif s[i] == "$" and s[j] != "$":
      j += 1
    else:
      key = s[i:j+1]
      # value = token_transform(tokens[key], tokens)
      # tokens[key] = value
      # print("tokens", tokens)
      # res += value
      value = tokens[key]
      final_value = token_transform(value, tokens)
      tokens[key] = final_value
      res += final_value
      
      i = j+1
      j = i+1
  return res


# selution two -- this one is not as good as the first one 
# def token_transform(s, tokens, memo={}):
#   print("S", s)
#   if s in memo:
#     return memo[s]
#   i = 0
#   j = 1
#   res = ""
#   while i < len(s):
#     if s[i] != "$":
#       res += s[i]
#       i += 1
#       j = i + 1
      
#     elif s[i] == "$" and s[j] != "$":
#       j += 1
#     else:
#       key = s[i:j+1]
#       value = token_transform(tokens[key], tokens)
#       res += value
#       i = j+1
#       j = i+1
#   memo[s] = res
#   return res


# selution one
# def token_transform(s, tokens):
#   arr = s.split(" ")
#   for word in arr: 
#     if "$" in word:
#       new_s = replace_token(s, tokens)
#       print("comes here")
#       return token_transform(new_s, tokens)
#   return s
    


# def replace_token(s, tokens):
#   i = 0
#   j = 1
#   res = ""
#   while i < len(s):
#     if s[i] != "$":
#       res += s[i]
#       i += 1
#       j = i + 1
      
#     elif s[i] == "$" and s[j] != "$":
#       j += 1
#     else:
#       key = s[i:j+1]
#       res += tokens[key]
#       i = j+1
#       j = i+1
#   return res



# tokens = {
#   '$LOCATION$': '$ANIMAL$ park',
#   '$ANIMAL$': 'dog',
# }
# print(token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens))
# # -> 'Walk the dog in the dog park!'
      
tokens = {
  '$ADJECTIVE_1$': "quick",
  '$ADJECTIVE_2$': "eager",
  '$ADVERBS$': "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
  '$VERB$': "hopped $DIRECTION$",
  '$DIRECTION$': "North",
}
token_transform("the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward", tokens)

# tokens = {
#   '$0$': "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
#   '$1$': "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
#   '$2$': "$3$$3$$3$$3$$3$$3$$3$",
#   '$3$': "$4$$4$$4$$4$$4$$4$",
#   '$4$': "$5$$5$$5$$5$$5$",
#   '$5$': "$6$$6$$6$$6$",
#   '$6$': "$7$$7$$7$",
#   '$7$': "$8$$8$",
#   '$8$': "",
# }
# print(token_transform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens))
print(tokens)
# -> 'zzzzzzz'
  
      
      