def subsets(nums):
    res = []
    
    def backtrack(start_index, current_path):
        # Step A: Capture the state
        # Every single path we take is a valid subset! 
        # We append a copy of current_path to our results list.
        res.append(list(current_path))
        
        # Step B: The Loop (Choices)
        # We loop through elements starting from 'start_index'
        for i in range(start_index, len(nums)):
            # CHOOSE: Add the current number to our working path
            current_path.append(nums[i])
            
            # EXPLORE: Recurse deeper. We pass 'i + 1' so we never 
            # reuse the same number or look backward.
            backtrack(i + 1, current_path)
            
            # UNCHOOSE (BACKTRACK): Pop the last item off so we 
            # can clear the path and try the next number in the loop.
            current_path.pop()

    backtrack(0, [])
    return res