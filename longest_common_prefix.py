#Write a function to find the longest common prefix 
#string amongst an array of strings.
#If there is no common prefix, return an empty string "".

strs = ["flower", "flow", "flight"]
#Output: "fl"

strs = ["cap", "cat", "car"]
#Output: ""

#Steps: first create a variable, then pick one element from the list and comoate it to other, 
# if same character match add that to the string then move to the next character 
# if match then add that to the string, and then if the character doesne match
#  after that then return the string , else if nothing match then return empty string

def longest_prefix(strs):
    prefix = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i >= len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix
print(longest_prefix(strs))

    
