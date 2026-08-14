height = [1,7,2,5,4,7,3,6]
#Output: 36

def maxArea(height):
     # Step 1: Initialize pointers
    left = 0
    right = len(height) - 1
    max_water = 0

    # Step 2: Two-pointer scan
    while left < right:
        # Step 3: Calculate area
        area  = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, area)

        # Step 4: Move the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    # Step 5: Return max area
    return max_water
print(maxArea(height))