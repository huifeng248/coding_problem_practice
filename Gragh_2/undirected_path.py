
# favorite
# undirected path
# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

# test_00:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True


def undirected_path(edges, node_A, node_B):
  gragh = convert_to_linked_list(edges)
  # return is_path(gragh, node_A, node_B)
  return is_path(gragh, node_A, node_B, visited= set())



def convert_to_linked_list(edges):
  gragh = {}
  for connection in edges:
    a = connection[0]
    b = connection[1]
    if a not in gragh:
      gragh[a] = []
    if b not in gragh:
      gragh[b] = []
    gragh[a].append(b)
    gragh[b].append(a)
  return gragh

# DFS
# def is_path(gragh, node_A, node_B):
#   stack = [node_A]
#   visited = set()
#   while stack:
#     current = stack.pop()
# #     this add to advoid duplicate cycle 
#     visited.add(current)
#     if current == node_B:
#       return True
#     for neighbor in gragh[current]:
# #       make sure only not in visited one is added to the stack
#       if neighbor not in visited:
#         stack.append(neighbor)
#   return False

# recursive
def is_path(gragh, node_A, node_B, visited):
# This is the base case
  if node_A == node_B:
    return True
  if node_A in visited:
    return False 
  visited.add(node_A)
  for neighbor in gragh[node_A]:
    if is_path(gragh, neighbor, node_B, visited):
      return True
  return False
  # if node_A not in visited:
  #   print(node_A, gragh)
  #   visited.add(node_A)
  #   for neighbor in gragh[node_A]:
  #     if is_path(gragh, neighbor, node_B, visited):
  #       return True
  # return False