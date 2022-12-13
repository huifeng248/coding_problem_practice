#  this one is tricky, look at the print for explaination

def largest_component(graph):
  max_size = 0
  visited = set()
  for node in graph:
    size = find_size(graph, node, visited)
    print("node:", node, "----", "size:",size)
    if size > max_size:
      max_size = size
  return max_size

def find_size(graph, node, visited):
  size = 0
  if node in visited:
    print("node in visited:", node, "size", size)
    return size
  
  visited.add(node)
  
  size = 1
  print("in the loop of each node:", node, "size:", size)
  for neighbor in graph[node]:
    size += find_size(graph, neighbor, visited) 
    
  return size 
  
  
  

# def largest_component(graph):
#   max_size = 0
  
#   for node in graph:
#     size = find_size(graph, node, visited = set())
#     if size > max_size:
#       max_size = size
#   return max_size

# def find_size(graph, node, visited):
#   size = 0
#   if node in visited:
#     return 0
# #   if not in the visited, need to add to visited
#   visited.add(node)
#   size = 1
#   for neighbor in graph[node]:
#     size = find_size(graph, neighbor, visited) + size
#   return size
    
print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4


# solutions
# depth first
def largest_component(graph):
  visited = set()
  
  largest = 0
  for node in graph:
    size = explore_size(graph, node, visited)
    if size > largest:
      largest = size
  
  return largest

def explore_size(graph, node, visited):
  if node in visited:
    return 0
  
  visited.add(node)
  
  size = 1
  for neighbor in graph[node]:
    size += explore_size(graph, neighbor, visited)
    
  return size
# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(n)