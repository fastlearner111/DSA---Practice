class TreeNode:
    def buildTree(self, preorder, inorder):
        index_map = {val:i for i, val in enumerate(inorder)}
        self.pre_idx = 0

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