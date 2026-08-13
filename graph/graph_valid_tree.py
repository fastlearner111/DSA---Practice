class Solution:
    def validTree(self, n, edges):

        # PART 1 — Quick check: tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # PART 2 — Initialize Union-Find
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            # PART 3 — Cycle detection
            if rootA == rootB:
                return False

            # PART 4 — Union by rank
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            elif rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            else:
                parent[rootB] = rootA
                rank[rootA] += 1

            return True

        # PART 5 — Process edges
        for a, b in edges:
            if not union(a, b):
                return False

        # PART 6 — No cycles + correct number of edges → valid tree
        return True
