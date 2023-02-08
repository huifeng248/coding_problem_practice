def safe_cracking(hints):
  graph = covert_graph(hints)
  parent_child = {}
  for node in graph:
    parent_child[node] = 0
  
  for node in graph:
    for child in graph[node]:
      parent_child[child] += 1
  print("graph", graph)
  print("parent_child", parent_child)
  ready = [node for node in parent_child if parent_child[node] == 0]
  print("ready", ready)
  # res = ""
  res = []
  while ready:
    current = ready.pop()
    res.append(current)
    # res+= str(current)
    for child in graph[current]:
      parent_child[child] -= 1
      if parent_child[child] == 0:
        ready.append(child)
  return "".join([str(num) for num in res])

def covert_graph(hints):
  graph = {}
  for pair in hints:
    a = pair[0]
    b = pair[1]
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    # graph[b].append(a)
  return graph
    
    
print(safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
])) # -> '718')

solution
graph topological order
def safe_cracking(hints):
  graph = build_graph(hints)
  return topological_order(graph)

def build_graph(edges):
  graph = {}
  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = [] 
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
  return graph

def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
    
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1
  
  ready = [ node for node in graph if num_parents[node] == 0 ]
  order = ''
  while ready:
    node = ready.pop()
    order += str(node)
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)
    
  return order
# e = number of hints
# Time: O(e)
# Space: O(e)



# safe cracking
# Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine the correct combination. Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

# The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit can occur zero or one time in the answer.

# Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination that will unlock the safe. The function should return a string representing the combination.

# test_00:
safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
]) # -> '718'
# test_01:
safe_cracking([
  (3, 1),
  (4, 7),
  (5, 9),
  (4, 3),
  (7, 3),
  (3, 5),
  (9, 1),
]) # -> '473591'