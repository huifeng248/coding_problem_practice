def prereqs_possible(num_courses, prereqs):
  graph = build_adjcent_list(num_courses, prereqs)
  visited = set()
  visiting = set()
  for node in graph:
    if has_cycle(node, graph, visited, visiting):
      return False
  return True

def has_cycle(node, graph, visited, visiting):
  if node in visited:
    return False
  if node in visiting:
    return True
  
  visiting.add(node)
  for neighbor in graph[node]:
    if has_cycle(neighbor, graph, visited, visiting):
      return True
  
  visiting.remove(node)
  visited.add(node)
  return False
  
  

def build_adjcent_list(num_courses, prereqs):
  graph = {}
  for i in range(num_courses):
    graph[i] = []
  
  for prereq in prereqs:
    a, b = prereq
    graph[a].append(b)
  return graph


numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs) # -> True


# prereqs possible
# Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.

# test_00:
numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs) # -> True
# test_01:
numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
  (3, 0),
]
prereqs_possible(numCourses, prereqs) # -> False
# test_02:
numCourses = 5
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
]
prereqs_possible(numCourses, prereqs) # -> True
# test_03:
numCourses = 6
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
  (5, 3),
  (3, 5),
]
prereqs_possible(numCourses, prereqs) # -> False
# test_04:
numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> True
# test_05:
numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (7, 4),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> False
# test_06:
numCourses = 42
prereqs = [(6, 36)]
prereqs_possible(numCourses, prereqs) # -> True

# white-grey-black algorithm
# def has_cycle(graph):
#     visited = set()
#     for start_node in graph:
#   	    if cycle_detect(graph, start_node, set(), visited):
#   		    return True
#     return False

# def cycle_detect(graph, node, visiting, visited):
#   if node in visited:
#   	return False

#   if node in visiting:
#   	return True

#   visiting.add(node)

#   for neighbor in graph[node]:
#     if cycle_detect(graph, neighbor, visiting, visited):
#     	return True

#   visiting.remove(node)
#   visited.add(node)
#   return False
# n = number of nodes
# Time: O(n^2)
# Space: O(n)