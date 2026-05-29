nums = [5, 3, 8, 3, 9]
def check_duplicate(nums):

    seen = set()

    for number in nums:
        if number in seen:
            return True
        seen.add(number)
    
    return False
print(check_duplicate(nums))