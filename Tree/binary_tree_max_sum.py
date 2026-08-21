class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumtree(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            path = node.val + node.left + node.right
            self.max_sum = max(self.max_sum, path)

            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
    

