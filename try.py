def majority_element(nums):
    count = {}
    
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    for num, freq in count.items():
        if freq > len(nums) // 2:
            return num
    
print(majority_element([3,2,3]))