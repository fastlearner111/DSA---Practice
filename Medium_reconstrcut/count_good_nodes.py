#Given a binary tree root, a node X in the tree is named good 
#if in the path from root to X there are no nodes with a value 
#greater than X.
#
#Return the number of good nodes in the binary tree.
#
#Input:  root = [3,1,4,3,null,1,5]
#Output: 4
#Explanation: Nodes in blue are good.
#- Root Node (3) is always a good node.
#- Node 4 → path is 3 → 4, no value greater than 4. Good.
#- Node 3 (left.left) → path is 3 → 1 → 3, no value greater than 3. Good.
#- Node 5 → path is 3 → 4 → 5, no value greater than 5. Good.
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

def goodNode(root):
    def dfs(node, maxValue):
        if not node:
            return 0
        
        good = 1 if node.val >= maxValue else 0
        maxValue = max(maxValue, node.val)

        left = dfs(node.left, maxValue)
        right = dfs(node. right, maxValue)

        return good + left + right
    return dfs(root, float('-inf'))

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left = TreeNode(3)
root.right.left = TreeNode(1) 
root.right.right = TreeNode(5)

print(goodNode(root))
        
    


