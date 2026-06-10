def majority_element(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    for num, freq in count.items():
        if freq > len(nums) // 2:
            return num
    return -1

print(majority_element([2,2,1,1,1,2,2]))