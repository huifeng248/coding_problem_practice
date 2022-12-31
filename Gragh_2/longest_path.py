# DFS
# def longest_path(graph):
#   max_path = 0
#   for node in graph:
#     path = find_max_length(node, graph)
#     max_path = max(max_path, path)
#   return max_path

# # 每一层都走到最底下， 所以不需要add visited。 time complexity eges * node
# def find_max_length(node, graph):
#   stack = [(node, 0)]
#   res = 0
#   while stack:
    
#     current, level = stack.pop()
#     if len(graph[current]) == 0:
#       res = max(level, res)
   
#     for neighbor in graph[current]:
#       stack.append((neighbor, level+1))
#   return res

# recursive
def longest_path(graph):

  distance = {}
  for node in graph:
    if len(graph[node])== 0:
      distance[node] = 0
    
  for node in graph:
    find_longest(graph, node, distance)
  
  return max(distance.values())
      
def find_longest(graph, node, distance):
  max_step = 0
  if node in distance:
    return distance[node]
  
  step = 0
  for neighbor in graph[node]:
#     this is the meat, we need to calculate the step for the neighbor, 
# which is one step away
    step = find_longest(graph, neighbor, distance) + 1
#   need to get the largest step from the neighbor and store it.
    max_step = max(step, max_step)
    
  distance[node] = max_step
  return distance[node]