# DFS
def largest_component(graph):
  max_size = 0
  visited = set()
  for node in graph:
    size = calculate_size(node, graph, visited)
    max_size = max(max_size, size)
  return max_size

# def calculate_size(node, graph, visited):
#   stack = [node]
#   count = 0
#   while stack:
#     current = stack.pop()
#     if current not in visited:
#       visited.add(current)
#       count += 1
      
#       for neighbor in graph[current]:
#         if neighbor not in visited:
#           stack.append(neighbor)
#   return count

# recursive
def calculate_size(node, graph, visited):
  # size = 1
  if node in visited:
    return 0
  
  visited.add(node)
  size = 1
  for neighbor in graph[node]:
    size += calculate_size(neighbor, graph, visited)
  return size
  