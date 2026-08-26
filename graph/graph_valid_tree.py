n = 5
edges = [[0,1],[1,2],[3,4]]

#Output: 2

class Solution:
    def valid_tree(self, n, edges):

        if len(edges) != n-1:
            return False

        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph(a).append(b)
            graph(b).append(a)

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)
        return len(visited) == n