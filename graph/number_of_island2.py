class Solution:

    def numIslands(self, grid):

        # PART 1 — Setup
        rows, cols = len(grid), len(grid[0])
        visited = set()

        # DFS helper
        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == "0" or
                (r, c) in visited
            ):
                return

            visited.add((r, c))

            # explore neighbors
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # PART 2 — Scan grid
        islands = 0

        for r in range(rows):
            for c in range(cols):

                # PART 3 — Found new island
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        # PART 4 — Return result
        return islands


# Test grids
grid1 = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"]
]

grid2 = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]
]

grid3 = [
    ["0", "0", "0"],
    ["0", "0", "0"],
    ["0", "0", "0"]
]

sol = Solution()

print("Islands in grid1:", sol.numIslands(grid1))
print("Islands in grid2:", sol.numIslands(grid2))
print("Islands in grid3:", sol.numIslands(grid3))
