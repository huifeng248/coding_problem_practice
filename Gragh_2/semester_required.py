# DSF

def semesters_required(num_courses, prereqs):
  if len(prereqs) == 0: return 1
  gragh = convert_to_graph(prereqs)
  return find_longest_path(gragh)

def convert_to_graph(prereqs):
  gragh = {}
  for prereq in prereqs:
    a = prereq[0]
    b = prereq[1]
    if a not in gragh:
      gragh[a] = []
    if b not in gragh:
      gragh[b] = []
    gragh[a].append(b)
  print("gragh", gragh)
  return gragh

def find_longest_path(gragh):
  distance = {}
  for node in gragh:
    if len(gragh[node]) == 0:
      distance[node] = 1
  for node in gragh:
    semesters_required = get_distance(distance, node, gragh)
  print("distance", distance)
  max_semester = max(distance.values())
  return max_semester

def get_distance(distance, node, gragh):
  
  if node in distance:
    return distance[node]
  stack = [(node, 1)]

  while stack:
    res = 1
    current, level = stack.pop()
    print("current", current, "level", level)
    
#     if len(gragh[current]) == 0:
#       # res = max(level,1)
#       distance[node] = max(level,1)
    
    for neighbor in gragh[current]:
      if neighbor not in distance:
        stack.append((neighbor, level+1))
        print("neighbor",neighbor,  "level+1", level+1, "stack", stack)
      else:
        path = level + distance[neighbor]
        res = max(res, path)
    # res = max(res, level) 
    distance[node] = res
  return distance[node]
  
        
  

# # recursive
# def semesters_required(num_courses, prereqs):
#   if len(prereqs) == 0: return 1
#   gragh = convert_to_graph(prereqs)
#   return find_longest_path(gragh)

  
# def convert_to_graph(prereqs):
#   gragh = {}
#   for prereq in prereqs:
#     a = prereq[0]
#     b = prereq[1]
#     if a not in gragh:
#       gragh[a] = []
#     if b not in gragh:
#       gragh[b] = []
#     gragh[a].append(b)
#   return gragh

# def find_longest_path(gragh):
#   distance = {}

#   for node in gragh:
#     if len(gragh[node]) == 0:
#       distance[node] = 1
#   for node in gragh:
#     semesters_required = get_distance(distance, node, gragh)
#   max_semester = max(distance.values())
#   return max_semester
    
# def get_distance(distance, node, gragh):
#   if node in distance:
#     return distance[node]
  
#   if len(gragh[node]) == 0:
#     return 1
  
#   max_path = 1
#   for neighbor in gragh[node]:
#     path = get_distance(distance, neighbor, gragh) + 1
#     if path > max_path:
#       max_path = path
#   distance[node] = max_path
#   return distance[node]
  

# def semesters_required(num_courses, prereqs):
#   if len(prereqs) == 0:
#     return 1
#   gragh = convert_to_graph(prereqs)
#   distance = {}
#   max_path = 0
#   for node in gragh:
#     if gragh[node] == 0:
#       distance[node] == 1
#     path = find_longest_path(gragh, node, distance)
#     if path > max_path:
#       max_path = path
#   return max_path

# def convert_to_graph(prereqs):
#   gragh = {}
#   for pre in prereqs:
#     node = pre[0] 
#     neighbor = pre[1]
#     if node not in gragh:
#       gragh[node] = [neighbor]
#     else:
#       gragh[node].append(neighbor)
#     if neighbor not in gragh:
#       gragh[neighbor] = []
#   print(gragh) 
#   return gragh

# def find_longest_path(gragh, node, distance):
#   find_max = 1
#   for neighbor in gragh[node]:
#     path = find_longest_path(gragh, neighbor, distance) +1
#     find_max = max(find_max, path)
  
#   distance[node] = find_max
#   return distance[node]

# def find_longest_path(gragh, node, distance):
#   # if node in distance:
#   #   print("if comes here", "node;", node)
#   #   return distance[node]
# #   i dont need the above codes.  find_max = 1 is my base case.
# # if i dont have neighbor, i dont need to enter the for loop.i should just return 1.

#   find_max = 1
#   print("node:", node, "neighbors:", gragh[node], "path:", find_max)
  
#   for neighbor in gragh[node]:
# #     for every neighbor, this is increment by 1
#     path = find_longest_path(gragh, neighbor, distance) +1
#     if path > find_max:
#       find_max = path
  
#   distance[node] = find_max
#   return distance[node]

# def get_distance(distance, node, gragh):
# #   base case 1
#   if node in distance:
#     return distance[node]
# #   base case 2
#   if len(gragh[node]) == 0:
#     return 1
  
#   max_path = 1
#   for neighbor in gragh[node]:
#     path = get_distance(distance, neighbor, gragh) + 1
#     max_path = max(max_path, path)
#   distance[node] = max_path
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
  