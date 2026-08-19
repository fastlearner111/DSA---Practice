# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):

        # STEP 1 — Build hashmap for inorder indices
        index_map = {val: i for i, val in enumerate(inorder)}
        

        # STEP 2 — Preorder pointer
        self.pre_idx = 0

        # STEP 3 — DFS to build tree
        def dfs(left, right):

            # Base case: no subtree
            if left > right:
                return None

            # STEP 4 — Get root value from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            # Create root node
            root = TreeNode(root_val)

            # Find root index in inorder
            mid = index_map[root_val]

            # STEP 5 — Build left and right subtrees
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        # Build entire tree
        return dfs(0, len(inorder) - 1)
