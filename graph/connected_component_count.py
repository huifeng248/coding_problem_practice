
def connected_components_count(graph):
  visited = set()
  count = 0
  for node in graph:
    if traval_node(graph, node, visited) == True:
      count += 1
  return count 

def traval_node(graph, current_node, visited):
  if current_node in visited:
    return False
  else:
    visited.add(current_node)
    for neighbor in graph[current_node]:
      traval_node(graph, neighbor, visited)
    return True
    
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~This illustative is not working yet~~~~~~~~~~~~~~~~~~~
# def connected_components_count(graph):
#   count = 0
#   visited = set()
  
#   for node in graph:
#     if node in visited:
#         continue
#     stack = [node]  # [0]
#     print("stack~~~~~~~", stack)
   
#     while stack: 
#       current = stack.pop()  #0   #5
#       visited.add(current)  #{0}  # {0, 5}
      
#       print("current", current, "visited set", visited)
      
#       if len(graph[node]) == 0:
#         #   print("grapg[node]", graph[node])
#           count += 1
#       else:
#         for neighbor in graph[node]: #[8,1,5] # [0, 8]
#             if neighbor in visited:
#                 continue
#             print("neibor:", neighbor)
#             stack.append(neighbor)  #stack=[8,1,5, 0]
#     count += 1
#   return count  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~This illustative is not working yet~~~~~~~~~~~~~~~~~~~
      
    
    
          
  
  
#   return count 
# print(connected_components_count({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# })) # -> 2

graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}
print(graph.keys())
