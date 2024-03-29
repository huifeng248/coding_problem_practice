def substitute_synonyms(sentence, synonyms):
  res = _substitute_synonyms(sentence, synonyms)
  result = []
  for ele in res:
    result.append(ele[:-1])
  return result

def _substitute_synonyms(sentence, synonyms):
  if len(sentence) == 0:
    return [""]
  res = []
  result = []
  
  choices, remainder = check_synonyms(sentence, synonyms)
  for choice in choices:
    remainder_possibilities = _substitute_synonyms(remainder, synonyms)
    for remainder_possibility in remainder_possibilities:
      res.append(choice + " "+ remainder_possibility)
  return res
      
  

def check_synonyms(sentence, synonyms):
  sentence_arr = sentence.split(" ")
  if sentence_arr[0] in synonyms:
    choices = synonyms[sentence_arr[0]]
  else:
    choices = [sentence_arr[0]]
    
  remainder_arr = sentence_arr[1:]
  print("remainder_arr", remainder_arr)
  remainder = " ".join(remainder_arr)
  print("remainder", remainder)
  return (choices, remainder)
      
    
sentence = "follow the yellow brick road"
synonyms = {
  "follow": ["chase", "pursue"],
  "yellow": ["gold", "amber", "lemon"],
}
# sentence = "I think it's gonna be a long long time"
# synonyms = {
#   "think": ["believe", "reckon"],
#   "long": ["lengthy", "prolonged"],
# }
print(substitute_synonyms(sentence, synonyms))
# print(check_synonyms(sentence, synonyms))


# substituting synonyms
# Write a function, substituting_synonyms, that takes in a sentence and a dictionary as arguments. The dictionary contains words as keys whose values are arrays containing synonyms. The function should return an array containing all possible sentences that can be formed by substituting words of the sentence with their synonyms.

# You may return the possible sentences in any order, as long as you return all of them.

# test_00:
sentence = "follow the yellow brick road"
synonyms = {
  "follow": ["chase", "pursue"],
  "yellow": ["gold", "amber", "lemon"],
}

substitute_synonyms(sentence, synonyms)
# [
#   'chase the gold brick road',
#   'chase the amber brick road',
#   'chase the lemon brick road',
#   'pursue the gold brick road',
#   'pursue the amber brick road',
#   'pursue the lemon brick road'
# ]
# test_01:
sentence = "I think it's gonna be a long long time"
synonyms = {
  "think": ["believe", "reckon"],
  "long": ["lengthy", "prolonged"],
}

substitute_synonyms(sentence, synonyms)
# [
#   "I believe it's gonna be a lengthy lengthy time",
#   "I believe it's gonna be a lengthy prolonged time",
#   "I believe it's gonna be a prolonged lengthy time",
#   "I believe it's gonna be a prolonged prolonged time",
#   "I reckon it's gonna be a lengthy lengthy time",
#   "I reckon it's gonna be a lengthy prolonged time",
#   "I reckon it's gonna be a prolonged lengthy time",
#   "I reckon it's gonna be a prolonged prolonged time"
# ]
# test_02:
sentence = "palms sweaty knees weak arms heavy"
synonyms = {
  "palms": ["hands", "fists"],
  "heavy": ["weighty", "hefty", "burdensome"],
  "weak": ["fragile", "feeble", "frail", "sickly"],
}

substitute_synonyms(sentence, synonyms)
# [
#   'hands sweaty knees fragile arms weighty',
#   'hands sweaty knees fragile arms hefty',
#   'hands sweaty knees fragile arms burdensome',
#   'hands sweaty knees feeble arms weighty',
#   'hands sweaty knees feeble arms hefty',
#   'hands sweaty knees feeble arms burdensome',
#   'hands sweaty knees frail arms weighty',
#   'hands sweaty knees frail arms hefty',
#   'hands sweaty knees frail arms burdensome',
#   'hands sweaty knees sickly arms weighty',
#   'hands sweaty knees sickly arms hefty',
#   'hands sweaty knees sickly arms burdensome',
#   'fists sweaty knees fragile arms weighty',
#   'fists sweaty knees fragile arms hefty',
#   'fists sweaty knees fragile arms burdensome',
#   'fists sweaty knees feeble arms weighty',
#   'fists sweaty knees feeble arms hefty',
#   'fists sweaty knees feeble arms burdensome',
#   'fists sweaty knees frail arms weighty',
#   'fists sweaty knees frail arms hefty',
#   'fists sweaty knees frail arms burdensome',
#   'fists sweaty knees sickly arms weighty',
#   'fists sweaty knees sickly arms hefty',
#   'fists sweaty knees sickly arms burdensome'
# ]


# solutions
# recursive
def substitute_synonyms(sentence, synonyms):
  words = sentence.split(' ')
  subarrays = generate(words, synonyms)
  return [ ' '.join(subarray) for subarray in subarrays ]

def generate(words, synonyms):
  if len(words) == 0:
    return [[]]
  
  first_word = words[0]
  remaining_words = words[1:]
  
  subarrays = generate(remaining_words, synonyms)
  
  if first_word in synonyms:
    result = []
    for synonym in synonyms[first_word]:
      result += [ [synonym, *subarray] for subarray in subarrays ]
    return result
  else:
    return [ [first_word, *subarray] for subarray in subarrays ] 
# n = number of words in sentence
# m = max number of synonyms for a word
# Time: ~O(m^n)
# Space: ~O(m^n)