def majority_element(nums):
    count = {}
    
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    for num, freq in count.value():
        if freq > len(nums) // 2:
            return freq
    
print(majority_element([3,2,3]))