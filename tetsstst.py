def contains_duplicate(nums):
    seen = set()
    
    for num in nums:
        seen.add(num)
        if num in seen:
            return True
    return False

print(contains_duplicate([1,2,3,1]))