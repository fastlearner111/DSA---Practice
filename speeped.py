#Given an integer array nums, return all the unique elements
#that appear exactly once.

nums = [1,2,2,3,3,4]
#Output: [1,4]


def unique_element(nums):
    seen = {}

    for numb in nums:
        if numb in seen:
            seen[numb] = seen.get(numb, 0) + 1
        else:
            seen[numb] = 1

    for numb, freq in seen.items():
        if freq == 1:
            result.append(numb)
    return result
print(unique_element(nums))
