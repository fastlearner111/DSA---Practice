nums = [3,4,5]
target = 16

#Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

def combination_sum(nums, target):
    res = []

    def backtracking(start_index, current_path, current_sum):
        if current_sum == target:
            res.append(list(current_path))
            return

        if current_sum > target:
            return

        for i in range(start_index, len(nums)):
            current_path.append(nums[i])
            backtracking(i, current_path, current_sum + nums[i])
            current_path.pop()

    backtracking(0,[], 0)
    return res