class Solution:
    def canFinish(self, numCourses, prerequisities):

        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisities:
            graph[b].append[a]

        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            path.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True 
            