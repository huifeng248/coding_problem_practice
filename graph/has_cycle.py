# DFS is not working
# def has_cycle(graph):
#   visited = set()
#   visiting = set()
#   for node in graph:
#     if detect_cycle(node, graph, visited, visiting):
#       print(node)
#       return True
#   return False 

# def detect_cycle(node, graph, visited, visiting):
#   stack = [node]
#   while stack:
#     current = stack.pop()
    
#     if current in visited:
#       return False
    
#     if current in visiting:
#       return True
    
#     visiting.add(current)  
#     for neighbor in graph[current]:
#       stack.append(neighbor)
    
#     if len(graph[current]) == 0:
#       visiting.remove(current)
#       visited.add(current)
    
#   return False
      
      
      
    



# recursive
def has_cycle(graph):
  visited = set()
  visiting = set()
  for node in graph:
    if detect_cycle(node, graph, visited, visiting):
      return True
  return False 
    

def detect_cycle(node, graph, visited, visiting):
  if node in visited:
    return False
  if node in visiting:
    return True
  
  visiting.add(node)
  for neighbor in graph[node]:
    if detect_cycle(neighbor, graph, visited, visiting):
      return True
  visiting.remove(node)
  visited.add(node)
  
  return False 

print(has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
})) # -> False


# has cycle
# Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle.

# test_00:
has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
}) # -> True
# test_01:
has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
}) # -> False
# test_02:
has_cycle({
  "a": ["b", "c"],
  "b": [],
  "c": [],
  "e": ["f"],
  "f": ["e"],
}) # -> True
# test_03:
has_cycle({
  "q": ["r", "s"],
  "r": ["t", "u"],
  "s": [],
  "t": [],
  "u": [],
  "v": ["w"],
  "w": [],
  "x": ["w"],
}) # -> False
# test_04:
has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
  "g": [],
}) # -> True
# test_05:
has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["d"],
  "d": ["b"],
}) # -> True