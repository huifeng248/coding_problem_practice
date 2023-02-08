def token_replace(s, tokens):
  i = 0 
  j = i+1
  # res = ""
  res = []
  while i < len(s):
    if s[i] != "$":
      
      # res += s[i]
      res.append(s[i])
      # print("res", res)
      i += 1
      j += 1
      print(i, j)
    else:
      # print("comes here")
      while s[j] != "$":
        j +=1
        # print("j", j)
      key = s[i:j+1]
      print("key", key)
      # res += tokens[key]
      res.append(tokens[key])
      i = j+1
      j = i+1

  # return res 
  return "".join(res)
  
    
tokens = {
  '$LOCATION$': 'park',
  '$ANIMAL$': 'dog',
}
print(token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens)) 
  