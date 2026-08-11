#Max Area of Island
#
#You are given a matrix grid where grid[i] is
#either a 0 (representing water) or 1 (representing land).
#An island is defined as a group of 1's connected horizontally
#or vertically. You may assume all four edges of the grid
#are surrounded by water.
#The area of an island is defined as the number of cells 
#within the island.
#Return the maximum area of an island in grid. 
#If no island exists, return 0.
#
#Example 1:
#Input: grid = [
#  [0,1,1,0,1],
#  [1,0,1,0,1],
#  [0,1,1,0,1],
#  [0,1,0,0,1]
#]
#
#Output: 6
#Explanation: 1's cannot be connected diagonally, 
#so the maximum area of the island is 6.

class Solution:
    def maxArea(self,grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0.-1)]

        def dfs(r,c):
            if(
                r < 0 or c < 0 or
                r >= rows or c >=cols or
                grid[r][c] == 0 or
                (r,c) in visited
            ):
                return 0

            visited.add((r,c))
            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        max_area = 0

        for r in range(rows):
            for c in range(cols):


#   Look in all four directions. For every direction you
#  check, send out a search party, ask them how much land 
# they find, add it to our running total, and then hand that
#  grand total back.
                if grid[r][c] == 1 and (r,c) not in visited:
                    island_area = dfs(r,c)
                    max_area = max(max_area, island_area)

        return max_area