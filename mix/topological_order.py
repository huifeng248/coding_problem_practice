def topological_order(graph):
  parent_child = parent_count(graph)
  return ordering_graph(graph, parent_child)
  
  
def ordering_graph(graph, parent_child):
  ready = [node for node in parent_child if parent_child[node] == 0]
  order = []
  while ready:
    current = ready.pop()
    order.append(current)
    for child in graph[current]:
      parent_child[child] -= 1
      if parent_child[child] == 0 :
        ready.append(child)
  return order 
  
def parent_count(graph):
  res = {}
  for node in graph:
    res[node] = 0
  
  for node in graph:
    for child in graph[node]:
      res[child] += 1
  return res

print(topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
})) # -> ['c', 'a', 'f', 'b', 'd', 'e'])
      