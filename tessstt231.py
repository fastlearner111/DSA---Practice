#Diameter of Binary Tree
root = [1,2,3,4,5]
#Output: 4
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
        return 1 + max(left,right)
    dfs(root)
    return res[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter(root))