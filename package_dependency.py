# add a package to the package management object
# base on the package name, pull its dependency in order

# def add_package(package_name, dependency, graph={}):
#     if dependency not in graph:
#         graph[dependency] = []
        
#     if package_name not in graph:
#         graph[package_name] = []
#     graph[package_name].append(dependency)
#     return graph

# def get_packages(package_name, graph):
#     stack = [package_name]
#     visited = set()
#     res = []
#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             visited.add(current)
#             res.append(current)
            
            
#         for dependency in graph[current]:
#             if dependency not in visited:
#                 stack.append(dependency)
#     res.reverse()
#     return res
            
        
        
    
    

# graph = {
#     "a":["c"],
#     "f":["a", "c"],
#     "c":["e"],
#     "e":[]
# }
# print(get_package("f", graph))


# def add_package(package_name, dependency, graph={}):
#     # if dependency not in graph:
#     #     graph[dependency] = []
#     # graph[dependency].append(package_name)
#     # graph[package_name] = []
#     if dependency not in graph:
#         return False
#     if package_name not in graph:
#         graph[package_name] = []
#     graph[package_name].append(dependency)
        
#     return graph

# Mai solution
def get_packages(package_name, graph):
    if package_name not in graph:
        return []

    res = []
    dfs(package_name, graph, res, set())
    
    return res

def dfs(package_name, graph, res, visited):
    if package_name in visited:
        return
    
    visited.add(package_name)
    
    for neighbor in graph[package_name]:
        dfs(neighbor, graph, res, visited)
    

    res.append(package_name)
        
graph = {
    "a":["c"],
    "f":["a", "c"],
    "c":["e"],
    "e":[]
}
print(get_packages("f", graph))        
    
    