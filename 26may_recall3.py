#Sliding Window Variable.
s = "abcabcbb"
#Find longest substring without repeating characters.

# since we are dealing with finding non repeating element
# we are gonna use a set,
# so we are gonna use seen , seen = set()
# then we need a left variable, left = 0, its a pointer
# then we are gonna need is a max_lenght variable that stores the count
# then we are gonna jump into the sliding window looop. 
# we are gooona use a while loop to see id the elemenbt is in seen
# if yes left +=1 , otherwise update max and move and add new element 

def longest_variable(s):
    left = 0
    seen = set()
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        max_length = max(max_length, right - left + 1)
        seen.add(s[right])
    return max_length
print(longest_variable(s))
        