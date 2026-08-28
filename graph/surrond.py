#⭐ 1. Problem Explanation (Interview Style)

#You’re given a board of 'X' and 'O'.

#Goal:

#✔ Flip all 'O' regions that are completely 
# surrounded by 'X'.
#Example:
#Code
#X X X X
#X O O X
#X X O X
#X O X X
#Only the middle region is fully surrounded.
#
#Output:
#
#Code
#X X X X
#X X X X
#X X X X
#X O X X
#The 'O' at the bottom is not flipped because 
# it touches the border.

class Solution:

    def solve(self, board):

      # PART 1 — Setup
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # DFS to mark safe 'O's
        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "S"  # mark as safe

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # PART 2 — Mark all border-connected 'O's as safe
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # PART 3 — Flip all non-safe 'O's to 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # PART 4 — Turn safe cells back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
