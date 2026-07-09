window = set()
l = 0

for r in range(len(nums)):
    # if the window is too big then shrink

    if r - l > k:
        window.remove(nums[l])
        l += 1

        # check condition
    if nums[r] in window:
        return True
    
    window.add(nums[r])
return False
        