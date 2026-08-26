numCourses = 3
prerequisites = [[1,0]]
#Output: [0,1,2]

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre].append(course)

            visiting = set()
            visited = set()

            order = []

            def dfs(node):
                if not dfs(node):
                    return False

                if node in visiting:
                    return False
                if node in visited:
                    return True

                visiting.add(node)

                for nei in graph[course]:
                    if not dfs(nei):
                        return False

                visiting.remove(node)
                visited.add(node)

                order.append(node)

                return True

            for course in range(numCourses):
                if not dfs(course):
                    return []

            return order[::-1]