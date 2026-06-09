s =[1,3,5,7,9]
target = 7
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right ) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1


    
print(binary_search([1,3,5,7,9], 7))
# Expected: 3