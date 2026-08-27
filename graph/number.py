n = 5
edges = [[0,1],[1,2],[3,4]]

#Output: 2

class Solution:
    def countComponent(self, n, edges):
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        component = 0

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                component += 1
                dfs(node)

        return component