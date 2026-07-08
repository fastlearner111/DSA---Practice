#Given root of binary tree, count the number of "good" nodes.
#A node is good if the path from root to that node has no node 
#with a greater value than this node.
#
#Input:  root = [3,1,4,3,null,1,5]
#Output: 4  (nodes: 3, 4, 3, 5)
#
#Input:  root = [3,3,null,4,2]
#Output: 3
#
#Input:  root = [1]
#Output: 1

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def countnodes(root):
    def dfs(node, maxvalue):
        if not node:
            return 0
        
        good = 1 if node.val >= maxvalue else 0
        maxvalue = max(maxvalue, node.val)

        left = dfs(node.left, maxvalue)
        right = dfs(node.right, maxvalue)
        return good + left + right
    return dfs(root,float('-inf'))

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

print(countnodes(root))