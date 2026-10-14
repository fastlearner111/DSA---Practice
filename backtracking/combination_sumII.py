candidates = [1,2,3,4,5]
target = 7

#Output: [
#  [1,2,4],
#  [2,5],
#  [3,4]
#]

def combination_sum(candidates, target):
    candidates.sort()
    res = []

    def backtrack(start_index, current_path, current_sum):
        if current_sum == target:
            res.append(list(current_path))
            return

        if current_sum > target:
            return

        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            current_path.append(candidates[i])
            backtrack(i + 1, current_path, current_sum + candidates[i])
            current_path.pop()

    backtrack(0, [], 0)
    return res
