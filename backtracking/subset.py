nums = [1,2,3]

def subset(nums):
    res = []

    def backtracking(start_index, current_path):
        res.append(list(current_path))

        for i in range(start_index, len(nums)):
            current_path.append(nums[i])
            backtracking(i + 1, current_path)
            current_path.pop()

    backtracking(0, [])
    return res
print(subset(nums))