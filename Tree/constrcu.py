class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        
        # 1. Build our cheat sheet once
        index_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        # 2. Define our DFS helper INSIDE the method
        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = index_map[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root
        return dfs(0, len(inorder) - 1)