#Write a function to find the longest common prefix 
#string amongst an array of strings.
#If there is no common prefix, return "".

strs = ["sprint", "spring", "sprite"]
#Output: "spr"

# first we create a empty string
# we make  duct
# then we are gonna use a nested loop that starts from 0
# then we are gonna have another loop inside the main
# then we will have if condtion to see if the characters are same or not
# in not return prefix
# else we add
# then return
# then print

def longest_prefix(strs):
    prefix = ""

    for i in range(len(strs[0])):
        for s in strs:
            if s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix
print(longest_prefix(strs))