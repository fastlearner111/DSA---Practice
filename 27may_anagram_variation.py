#Given a string, check if it can be rearranged to form a palindrome.

s = "racecar"
#Output: True  (already a palindrome)

#Input: "aab"
#Output: True  (can rearrange to "aba")

#Input: "abc"
#Output: False  (no palindrome possible)

# so that means we are tryna see if there is one odd and remainig even or not
# if yes then palindrome, else, not, we need to find the frequency of each length
# then we need to give a condition where it checks for odd or even, and then
# another condition if there is only one odd then truw else false

def check_palindrome(s):
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    odd_count = 0

    for value in count.values():
        if value % 2 != 0:
            odd_count += 1
    return odd_count <= 1
print(check_palindrome(s))
