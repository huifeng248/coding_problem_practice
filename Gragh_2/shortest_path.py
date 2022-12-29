from collections import deque
def shortest_path(edges, node_A, node_B):
  gragh = convert_adjcent_list(edges)
  visited = set()
  return find_shortest(gragh, visited, node_A, node_B)

def find_shortest(gragh, visited, node_A, node_B):
  queue = deque([(node_A, 0)])
  while queue:
    current, level = queue.popleft()
    if current not in visited:
      visited.add(current)
      
      for neighbor in gragh[current]:
        if neighbor not in visited:
          queue.append((neighbor, level+1))
          if neighbor == node_B:
            return level +1
  return -1
  
def convert_adjcent_list(edges):
  gragh = {}
  for edge in edges:
    a = edge[0]
    b = edge[1]
    if a not in gragh:
      gragh[a] = []
    if b not in gragh:
      gragh[b] = []
    gragh[a].append(b)
    gragh[b].append(a)
  return gragh