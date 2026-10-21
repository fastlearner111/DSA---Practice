digits = "34"
#Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
#Input: digits = ""
#Output: []

class Solution:
    def lettercombination(self,digits):
        if not digits:
            return []

        res = []

        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7":"pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(i,current_path):
            if i == len(digits):
                res.append("".join(current_path))
                return

            current_chars = digit_to_char[digits[i]]

            for char in current_chars:
                current_path.append(char)
                backtrack(i + 1, current_path)
                current_path.pop()

        backtrack(0, [])
        return res 