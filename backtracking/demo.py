n = 3

class Solution:
    def generate_parentheses(self):
        res = []

        def backtrack(open_count, close_count, current_path):
            if len(current_path) == 2 * n:
                res.append("".join(current_path))

            if open_count < n:
                current_path.append('(')
                backtrack(open_count + 1, close_count, current_path)
                current_path.pop()

            if close_count < open_count:
                current_path.append(')')
                backtrack(open_count, close_count + 1, current_path)
                current_path.pop()

        backtrack(0, 0, [])
        return res