#Given a reference of a node in a connected undirected graph,
#return a deep copy (clone) of the graph.
#
#Each node in the graph contains a value (int) and a list of 
#its neighbors (List[Node]).
#
#class Node:
#    def __init__(self, val = 0, neighbors = None):
#        self.val = val
#        self.neighbors = neighbors if neighbors is not None else []
#
#Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
#Output: [[2,4],[1,3],[2,4],[1,3]]
#
#Explanation:6
#Node 1 has neighbors: 2, 4
#Node 2 has neighbors: 1, 3
#Node 3 has neighbors: 2, 4
#Node 4 has neighbors: 1, 3
#
#Input:  adjList = [[]]
#Output: [[]]
#(One node with no neighbors)
#
#Input:  adjList = []
#Output: []
#(Empty graph)
#
#Constraints:
#- Number of nodes: [0, 100]
#- 1 <= Node.val <= 100
#- Node.val is unique for each node
#- No repeated edges, no self-loops

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self,node):
        if not node:
            return None
        
        visited = {}

        def dfs(curr):
            if curr in visited:   # if curr is in visted then we need to return a clone
                return visited[curr]
            
            clone = Node(curr.val)  # i think this means we create a new clone 
            visited[curr] = clone # we put the value fo visted[curr] inside the clone

            for nei in curr.neighbors:# not sure about this one
                clone.neighbors.append(dfs(nei))# not sure about this one
            
            return clone
        return dfs(node)
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

sol = Solution()
cloned = sol.cloneGraph(n1)

# Print cloned graph values and neighbors
print("Cloned Node:", cloned.val)
print("Neighbors:", [nei.val for nei in cloned.neighbors])

print("Cloned Node 2:", cloned.neighbors[0].val)
print("Neighbors:", [nei.val for nei in cloned.neighbors[0].neighbors])