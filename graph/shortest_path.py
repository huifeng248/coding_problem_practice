def shortest_path(edges, node_A, node_B):
  
  graph = convert_AJ_list(edges)
  distance = calculate_path(graph, node_A, node_B)
  
  return distance

from collections import deque
def calculate_path(graph, node_A, node_B):
  visited = set([node_A])
  queue = deque([(node_A, 0)])
  while queue:
    node_value, level = queue.popleft()
    
    if node_value == node_B:
      return level
    
    for neighbor in graph[node_value]:
      if neighbor not in visited:
        queue.append([neighbor, level+1])
        visited.add(neighbor)
  return -1
    

# def calculate_path(graph, node_A, node_B):
#   visited = set()
#   queue = deque([(node_A, 0)])
#   while queue:
#     node_value, level = queue.popleft() 
#     print("before:", "node_value:", node_value, "visited:", visited)
#     visited.add(node_value)
#     print("after:", "node_value:", node_value, "visited:", visited)
          
#     # if node_value == node_B:
#     #   return level
    
#     for neighbor in graph[node_value]:
#       if neighbor not in visited:
#         queue.append([neighbor, level+1])
#         if neighbor == node_B:
#           return level +1
  
#   return -1
  
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]


    
  

def convert_AJ_list(edges):
  graph = {}
  for set in edges:
    a = set[0]
    b = set[1]
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'w', 'z') # -> 2


# solutions
# breadth first
from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  visited = set([ node_A ])
  queue = deque([ (node_A, 0) ])
  
  while queue:
    node, distance = queue.popleft()
    
    if node == node_B:
      return distance
    
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, distance + 1))
        
  return -1
  
def build_graph(edges):
  graph = {}
  
  for edge in edges:
    a, b = edge
    
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
    
  return graph
# e = number edges
# Time: O(e)
# Space: O(e)
  
# shortest path
# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.

# test_00:
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'w', 'z') # -> 2
# test_01:
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'y', 'x') # -> 1
# test_02:
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

shortest_path(edges, 'a', 'e') # -> 3
# test_03:
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

shortest_path(edges, 'e', 'c') # -> 2
# test_04:
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

shortest_path(edges, 'b', 'g') # -> -1
# test_05:
edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

shortest_path(edges, 'w', 'e') # -> 1
# test_06:
edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

shortest_path(edges, 'n', 'e') # -> 2
# test_07:
edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

shortest_path(edges, 'm', 's') # -> 6