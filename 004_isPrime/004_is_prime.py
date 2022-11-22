def is_prime(n):
  # pass # todo
  if n == 1:
    return False
   # while x in range(1,11):
  for number in range(2, n):
    if n == 2:
      return True
    if n % number == 0:
      return False
  return True

# print(is_prime(2))

from math import sqrt, floor
def is_prime(n):
  # pass # todo
  if n == 1:
    return False
   # while x in range(1,11):
  for number in range(2, floor(sqrt(n)) +1):
    if n == 2:
      return True
    if n % number == 0:
      return False
  return True


# Course Contents
# structy-logo
# structy
# premium
# favorite
# is prime
# Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

# A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

# For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

# You can assume that the input number is a positive integer.



# favorite
# solution
from math import sqrt, floor

def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
      return False
    
  return True
# n = input number
# Time: O(square_root(n))
# Space: O(1)