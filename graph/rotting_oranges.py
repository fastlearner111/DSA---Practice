#You are given a 2-D matrix grid.
#Each cell can have one of three 
#possible values:
#
#0 representing an empty cell
#1 representing a fresh fruit
#2 representing a rotten fruit
#
#Every minute, if a fresh fruit is horizontally
#or vertically adjacent to a rotten
#fruit, then the fresh fruit also becomes 
#rotten.
#
#Return the minimum number of minutes
#that must elapse until there are zero 
#fresh fruits remaining. If this state is
#impossible within the grid, return -1.
#
#Example 1:
#grid = [[1,1,0],[0,1,1],[0,1,2]]
#Output: 4
#
#Example 2:
#grid = [[1,0,1],[0,2,0],[1,0,1]]
#Output: -1

from collections import deque

class Solution:

    def orangeRotting(self,grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr,dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            if queue:
                minutes += 1

        if fresh > 0:
            return -1

        return minutes