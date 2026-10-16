class Solution:
    def permute(self, nums):
        res = []
        
        def backtrack(current_path):
            # 2. SUCCESS GUARD: If our backpack is as long as the original array, 
            # it's a complete permutation!
            if len(current_path) == len(nums):
                res.append(list(current_path)) # Make a copy and save it
                return
            
            # 3. THE LOOP: Always scan from 0 because any number can be picked first/next
            for i in range(len(nums)):
                # 3. THE GUARD: If this number is already in our backpack, skip it
                if nums[i] in current_path:
                    continue
                    
                # 4. THE TRIO: Choose -> Explore -> Unchoose
                current_path.append(nums[i])      # Choose
                backtrack(current_path)           # Explore deeper
                current_path.pop()                # Unchoose (Backtrack)

        backtrack([])
        return res