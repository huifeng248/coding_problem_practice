# anagrams
# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

# test_00:
# anagrams('restful', 'fluster') # -> True
# test_01:
# anagrams('cats', 'tocs') # -> False
# test_02:
# anagrams('monkeyswrite', 'newyorktimes') # -> True
# test_03:
# anagrams('paper', 'reapa') # -> False
# test_04:
# anagrams('elbow', 'below') # -> True
# test_05:
# anagrams('tax', 'taxi') # -> False
# test_06:
# anagrams('taxi', 'tax') # -> False
# test_07:
# anagrams('night', 'thing') # -> True
# test_08:
# anagrams('abbc', 'aabc') # -> False
# test_09:
# anagrams('po', 'popp') # -> false
# test_10:
# anagrams('pp', 'oo') # -> false



def anagrams(s1, s2):
  arr1 = [i for i in s1]
  arr2 = [i for i in s2]
  
  arr1.sort()
  arr2.sort()
  
  return arr1 ==arr2

print(anagrams('restful', 'fluster'))


def anagrams(s1, s2):
  obj_1 = obj_convert(s1)
  obj_2 = obj_convert(s2)
  
  return obj_2 == obj_1
  
  
  
def obj_convert(s1):
  obj1 = {}
  for i in s1:
    if i not in obj1:
      obj1[i] = 1
    else:
      obj1[i] += 1
  return obj1

# if there is no key, key error is raise. which is diff from js
print(obj_convert("fluster"))

print(anagrams('restful', 'fluster'))


from collections import Counter

def anagrams(a1, a2):
  return Counter(a1) == Counter(a2)

# //Counter can convert a string into a dict
# dict can be compared directly


# solution
# using dictionaries
def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)

def char_count(s):
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1
  
  return count
# n = length of string 1
# m = length of string 2
# Time: O(n + m)
# Space: O(n + m)
# using Counters
from collections import Counter

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)
# n = length of string 1
# m = length of string 2
# Time: O(n + m)
# Space: O(n + m)