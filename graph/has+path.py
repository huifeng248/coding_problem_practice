# def has_path(graph, src, dst):
#   stack = [src]
#   while stack:
#     current = stack.pop()
#     if current == dst:
#       return True
#     for node in graph[current]:
#       stack.append(node)
#   return False