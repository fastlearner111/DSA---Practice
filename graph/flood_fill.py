# Flood fill

#You are given an image represented by an m x n grid of
#integers image, where image[i][j] represents the pixel 
#value of the image. You are also given three integers sr
#, sc, and color. Your task is to perform a flood fill on
#the image starting from the pixel image[sr][sc].
#
#To perform a flood fill:
#Begin with the starting pixel and change its color to color.
#Perform the same process for each pixel that is directly
#adjacent (pixels that share a side with the original pixel, 
#either horizontally or vertically) and shares the same color as 
#the starting pixel.Keep repeating this process by checking 
#neighboring pixels of the updated pixels and modifying their
#color if it matches the original color of the starting pixel.
#The process stops when there are no more adjacent pixels of 
#the original color to update.Return the modified image after 
#performing the flood fill.
#
# 
#
#Example 1:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]


class Solution:

    def floodFill(self, image, sr, sc, newColor):

        # PART 1 — Setup
        rows, cols = len(image), len(image[0])
        originalColor = image[sr][sc]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # If the color is already the same, no need to do anything
        if originalColor == newColor:
            return image

        # DFS helper
        def dfs(r, c):
            # boundary + wrong color checks
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                image[r][c] != originalColor
            ):
                return

            # recolor the cell
            image[r][c] = newColor

            # explore neighbors
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # PART 2 — Start DFS from the starting pixel
        dfs(sr, sc)

        # PART 3 — Return the updated image
        return image
