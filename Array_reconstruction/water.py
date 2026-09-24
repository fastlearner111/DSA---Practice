#that holds the most water. Return the maximum amount of water.
#
height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#
#Input:  height = [1,1]
#Output: 1

def isContainer(height):
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
        water = min(height[left], height[right]) * (right - left)
        result = max(result, water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result
print(isContainer(height))
