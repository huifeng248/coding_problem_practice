class Solution:
    def countPrimes(self, n: int) -> int:
      if n <=1:
        return 0
      res = 0
      is_prime = [True] * n
      for i in range(2, n, 1):
        if is_prime[i] == True:
          for j in range(2*i, n, i):
            is_prime[j] = False
      
      # print(is_prime)
      for i in range(2, n, 1):
        if is_prime[i] == True:
          res += 1
      return res

# Time Complexity: The overall time complexity isO(sqrt{n}*log *log n + n). The +n+ n+n is from calculating the answer after the main algorithm. The sqrt{n} comes from the outer loop. Each time we hit a prime, we "cross out" the multiples of that prime because we know they aren't prime.
# space complexity: O(n)


# # brute force
# import math
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 1:
#             return 0
#         res = 0 
#         for i in range(2, n, 1):
#             if self.is_prime(i):
#                 res += 1
#         return res

    
#     def is_prime(self, num):
#         if num <= 1:
#             return False
#         if num == 2:
#             return True
#         for i in range(2, num, 1):
#             if num % i == 0:
#                 return False
        
#         return True

#time complexity of the given code is O(n * sqrt(n)), and the space complexity is O(1). The is_prime method uses another for loop to iterate over the values of i from 2 to num-1, and checks if num is divisible by i. 
#space complexity O(1)
        



