# blue force
# def fib(n):
#   if n == 0:
#     return 0
#   if n == 1:
#     return 1
#   return fib(n-1) +fib(n-2)

# memo solution 1

def fib(n, memo={}):
  if n in memo:
    return memo[n]
  if n == 0:
    return 0
  if n == 1:
    return 1
  memo[n] = fib(n-1, memo) + fib(n-2, memo)
  print("memo", memo)
  return memo[n]
  
  


  
# memo solution 2
# def fib(n, memo = {}):
#   if n == 0:
#     memo[0] = 0
#     return 0
#   if n == 1:
#     memo[1] = 1
#     return 1
#   if n-1 in memo:
#     memo[n] = memo[n-1] + memo[n-2]
#   else:
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)
#   return memo[n]


print(fib(5))

# brute-force (timeout)
# def fib(n):
#   if n == 0 or n == 1:
#     return n
#   return fib(n - 1) + fib(n - 2)

# Time: O(2^n)
# Space: O(n)
# memoized (pass)
# def fib(n):
#   memo = {}
#   return _fib(n, memo)

# def _fib(n, memo):
#   if n == 0 or n == 1:
#     return n
  
#   if n in memo:
#     return memo[n]

#   memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
#   return memo[n]
# Time: O(n)
# Space: O(n)


# fib
# Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

# The 0-th number of the sequence is 0.

# The 1-st number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous two numbers.

# Solve this recursively.

# test_00:
fib(0); # -> 0
# test_01:
fib(1); # -> 1
# test_02:
fib(2); # -> 1
# test_03:
fib(3); # -> 2
# test_04:
fib(4); # -> 3
# test_05:
fib(5); # -> 5
# test_06:
fib(35); # -> 9227465
# test_07:
fib(46); # -> 1836311903