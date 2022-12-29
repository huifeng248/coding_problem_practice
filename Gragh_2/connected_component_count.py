# DFS
def connected_components_count(graph):
  visited = set()
  count = 0
  for node in graph:
    if find_island(node, graph, visited):
      print(node, "result", find_island(node, graph, visited))
      count += 1
  return count
    

def find_island(node, graph, visited):
  if node in visited:
    return False
  stack = [node]
  while stack:
    current = stack.pop()
    if current not in visited:
      visited.add(current)
      for neighbor in graph[current]:
        if neighbor not in visited:
          stack.append(neighbor)
  return True
    
#   recursive
def connected_components_count(graph):
  visited = set() 
  count = 0
  for node in graph:
    if find_island(node, graph, visited):
      count += 1
  return count

def find_island(node, graph, visited):
  if node in visited:
    return False
  
  visited.add(node)
  for neighbor in graph[node]:
    find_island(neighbor, graph, visited)
  return True