height = [0,2,0,3,1,0,1,3,2,1]
#Output: 9


def trappedWater(height):
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:

        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += max(0, left_max - height[left])

        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += max(0, right_max - height[right])

    return water
print(trappedWater(height))