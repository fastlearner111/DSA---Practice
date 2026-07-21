#200. Number of Islands

#Given an m x n 2D binary grid grid which represents 
# a map of '1's (land) and '0's (water), return the 
# number of islands.
#
#An island is surrounded by water and is formed by 
# connecting adjacent lands horizontally or vertically.
#  You may assume all four edges of the grid are all 
# surrounded by water.

#Example 1:
#Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
#]
#Output: 1
#Example 2:
#
#Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
#]
#Output: 3

#Constraints:
#m == grid.length
#n == grid[i].length
#1 <= m, n <= 300
#grid[i][j] is '0' or '1'.


class Solution:
    def numIsland(self, grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            if grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count+= 1
                    dfs(r,c)
        return count


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

print("Islands in gird1:", sol.numIsland(grid1))
print("Islands in gird2:", sol.numIsland(grid2))
print("Islands in gird3:", sol.numIsland(grid3))

                    