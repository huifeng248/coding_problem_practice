def add_package(package_name, dependency, graph={}):
    # if dependency not in graph:
    #     graph[dependency] = []
    # graph[dependency].append(package_name)
    # graph[package_name] = []
    if dependency not in graph:
        return False
    if package_name not in graph:
        graph[package_name] = []
    graph[package_name].append(dependency)
        
    return graph

def get_packages(package_name, graph):
    if package_name not in graph:
        return []

    res = []
    dfp(package_name, graph, res, set())
    
    return res

def dfp(package_name, graph, res, visited):
    for neighbor in graph[package_name]:
        dfs(neighbor, graph, res, visited)
    
    res.append(package_name)
        
        
    