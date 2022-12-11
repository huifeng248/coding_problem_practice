# def has_path(graph, src, dst):
#   stack = [src]
#   while stack:
#     current = stack.pop()
#     if current == dst:
#       return True
#     for node in graph[current]:
#       stack.append(node)
#   return False

def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    
    if has_path(graph, neighbor, dst):
      return True
  return False


# solutions
# depth first
def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
    
  return False
# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(n)
# breadth first
# from collections import deque

def has_path(graph, src, dst):
  queue = deque([ src ])
  
  while queue:
    current = queue.popleft()
    
    if current == dst:
      return True
    
    for neighbor in graph[current]:
      queue.append(neighbor)
    
  return False
# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(n)


# has path
# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

# Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

# test_00:
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'k') # True

# test_01:
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'j') # False
# test_02:
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'i', 'h') # True
# test_03:
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'w') # True
# test_04:
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'z') # False