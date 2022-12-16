def semesters_required(num_courses, prereqs):
  if len(prereqs) == 0:
    return 1
  gragh = convert_to_graph(prereqs)
  distance = {}
  max_path = 0
  for node in gragh:
    if gragh[node] == 0:
      distance[node] == 1
    path = find_longest_path(gragh, node, distance)
    if path > max_path:
      max_path = path
  return max_path

def convert_to_graph(prereqs):
  gragh = {}
  for pre in prereqs:
    node = pre[0] 
    neighbor = pre[1]
    if node not in gragh:
      gragh[node] = [neighbor]
    else:
      gragh[node].append(neighbor)
    if neighbor not in gragh:
      gragh[neighbor] = []
  print(gragh) 
  return gragh

def find_longest_path(gragh, node, distance):
  find_max = 1
  for neighbor in gragh[node]:
    path = find_longest_path(gragh, neighbor, distance) +1
    find_max = max(find_max, path)
  
  distance[node] = find_max
  return distance[node]
# def find_longest_path(gragh, node, distance):
#   if node in distance:
#     return distance[node]
  
#   find_max = 1
#   print("node:", node, "neighbors:", gragh[node], "path:", find_max)
#   for neighbor in gragh[node]:
# #     for every neighbor, this is increment by 1
#     path = find_longest_path(gragh, neighbor, distance) +1
    
#     find_max = max(find_max, path)
  
#   distance[node] = find_max
#   return distance[node]
  
  

num_courses = 7
# prereqs = [
#   (1, 2),
#   (2, 4),
#   (3, 5),
#   (0, 5),
# ]
prereqs = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]
print(semesters_required(num_courses, prereqs)) # -> 5

# solutions
# depth first
def semesters_required(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  distance = {}
  for course in range(num_courses):
    if len(graph[course]) == 0:
      distance[course] = 1
  
  for course in range(num_courses):
    traverse_distance(graph, course, distance)
    
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  max_distance = 0
  for neighbor in graph[node]:
    neighbor_distance = traverse_distance(graph, neighbor, distance)
    if neighbor_distance > max_distance:
      max_distance = neighbor_distance
    
  distance[node] = 1 + max_distance
  return distance[node]

def build_graph(num_courses, prereqs):
  graph = {}
  
  for course in range(num_courses):
    graph[course] = []
    
  for prereq in prereqs:
    a, b = prereq
    graph[a].append(b)
  
  return graph
# p = # prereqs
# c = # courses
# Time: O(p)
# Space: O(c)

  