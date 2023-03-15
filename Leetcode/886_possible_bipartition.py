class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        graph = {}
        for pair in dislikes:
            a,b = pair[0], pair[1]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        color_dict = {}
        visited = set()

        for node in graph:
            if node not in visited: 
                if not self.helper(node, visited, color_dict, graph):
                    return False 
        return True

    def helper(self, node, visited, color_dict, graph):
        stack = [(node, 1)]
        while stack:
            current, color = stack.pop()
            if current not in color_dict:
                color_dict[current] = color
                visited.add(current)
            else:
                if color_dict[current] != color:

                    return False
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append((neighbor, -color))
        return True

# time complexity: O(N+E) E is the number of dislikes, and n is the number of nodes.
# The first for loop that constructs the adjacency list takes O(len(dislikes)) time, as it needs to iterate over all pairs of dislikes. It requires O(len(dislikes)) space to store the adjacency list.

# The helper function uses a depth-first search approach to traverse the graph. In the worst case, it can visit every node and every edge in the graph, which takes O(n+m) time, where n is the number of nodes and m is the number of edges. Each node can be pushed to the stack at most once, so the space complexity of the function is O(n).


# space complexity: O(N+E) N is the number of nodes。 
# graph is a dictionary that stores the adjacency list, which requires O(len(dislikes)) space to store, as it contains one key-value pair for each edge in the graph








