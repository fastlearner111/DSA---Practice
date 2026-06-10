#Given an integer array nums, return all the unique elements
#that appear exactly once.

nums = [1,2,2,3,3,4]
#Output: [1,4]


def unique_element(nums):
    seen = {}

    for numb in nums:
        if numb in seen:
            seen.get(numb, 0) + 1
        else:
            seen[numb] = 1

    for i, numb in seen.items():
        if freq >  len(numb) / 2:
            return numb
    return -1
print(unique_element(nums))
