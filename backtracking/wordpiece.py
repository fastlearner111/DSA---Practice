board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

#Output: true

class Solution:
    def wordpeice(self):
        ROWS = len(board)
        COLS = len(board[0])

        