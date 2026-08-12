from collections import deque

class Solution:
    def levelorder(self, root):

        #part1
        if not root:
            return []

        #part 2
        ans = []
        queue = deque([root])

        #part3
        while queue:
            level = []
            size = len(queue)

            for _ in range(size):

                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.apppend(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)
        return ans