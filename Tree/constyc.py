class TreeNode:
    def buildTree(self, inorder, preorder):
        index_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)