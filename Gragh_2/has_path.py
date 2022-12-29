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

# has_path(graph, 'f', 'k') # True

# DFS ilterative 
def has_path(graph, src, dst):
  visited = set()
  stack = [src]
  while stack:
    current = stack.pop()
    if current in visited:
      continue 
      
    if current == dst:
      return True
    visited.add(current)
    
    for neighbor in graph[current]:
      if neighbor not in visited:
        stack.append(neighbor)
  return False

# DFS recursive
# def has_path(graph, src, dst):
#   if src == dst:
#     return True
  
#   for neighbor in graph[src]:
#     if has_path(graph, neighbor, dst) == True:
#       return True
#   return False 
    
  
  
  
  
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True