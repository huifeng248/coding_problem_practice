# def undirected_path(edges, node_A, node_B):
#   graph = {}
  
#   for node in edges:
#     node_1 = node[0]
#     node_2 = node[1]
#     if node_1 not in graph:
#       graph[node_1] = [node_2]
#     else: 
#       graph[node_1].append(node_2)
    
#     if node_2 not in graph:
#       graph[node_2] = [node_1]
#     else: 
#       graph[node_2].append(node_1)
#   print(graph)
  
#   res = find_path(graph, node_A, node_B)
  
#   return res
# def find_path(graph, start, target):
#   stack = [start]
#   visited = set()
  
#   while stack:
#     current = stack.pop()
#     if current == target:
#       return True
    
#     for node in graph[current]:
#       if node in visited:
#         pass
#       else:
#         stack.append(node)
#         visited.add(node)
#   return False 

def undirected_path(edges, node_A, node_B):
  graph = {}
  for node in edges:
    node_1 = node[0]
    node_2 = node[1]
    if node_1 not in graph:
      graph[node_1] = [node_2]
    else: 
      graph[node_1].append(node_2)
    
    if node_2 not in graph:
      graph[node_2] = [node_1]
    else: 
      graph[node_2].append(node_1)
  print("!!!", graph)
  
  return find_path(graph, node_A, node_B, visited=set())

def find_path(graph, start, target, visited):
  if start == target:
    return True
  
  if start in visited:
    return 0
  visited.add(start)
  
  for neighbor in graph[start]:
    if find_path(graph, neighbor, target, visited) == True:
      return True
  return False

    
  
  
  

gragh = {
 'i': ['j', 'k'], 
 'j': ['i'], 
 'k': ['i', 'm', 'l'], 
 'm': ['k'], 
  'l': ['k'], 
 'o': ['n'], 
 'n': ['o']} 

# print("helper:", find_path(gragh, "j", "m"))
# undirected_path(edges, 'j', 'm') # -> True



# favorite
# solutions
# depth first
def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, set())

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
    
def has_path(graph, src, dst, visited):
  if src == dst:
    return True
  
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
    
  return False
# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(e)