#Count nodes where path from root has no node greater than this node.
#
#Input:  root = [3,1,4,3,null,1,5]
#Output: 4


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def count_node(root):
    def dfs(node, maxValue):
        if not node:
            return 0
        
        good = 1 if node.val >= maxValue else 0
        maxValue = max(maxValue,node.val)

        left = dfs(node.left, maxValue)
        right = dfs(node.right, maxValue)

        return good + left + right
    return dfs(root, float('-inf'))

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1) 
root.right.right = TreeNode(5)

print(count_node(root))
        
    

