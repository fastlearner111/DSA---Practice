#Given the root of a binary tree, return the length of the diameter.
#Diameter is the longest path between any two nodes — measured in edges.
#The path does not have to pass through the root.
#
root = [1,2,3,4,5]
#Output: 3
#
#Input:  root = [1,2]
#Output: 1

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def diameter(root):
    res = [0]

    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        res[0] = max(res[0], left + right)
        return 1 + max(left, right)
    
    dfs(root)
    return res[0]

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)

print(diameter(node))


    