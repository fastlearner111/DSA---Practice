#Given the root of a binary tree, return its maximum depth.
#Maximum depth is the number of nodes along the longest path 
#from the root node down to the farthest leaf node.
#
#root = [3,9,20,null,null,15,7]
#Output: 3
#
#Input:  root = [1,null,2]
#Output: 2
#
#Input:  root = []
#Output: 0
#
#Constraints:
#- Number of nodes: [0, 10^4]
#- -100 <= Node.val <= 100

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    if not node:
        return 0
    
    left = dfs(node.left)
    right = dfs(node.right)

    return 1 + max(left, right)

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

print(dfs(node))