##Write a function to find the longest common prefix 
#string amongst an array of strings.
#If there is no common prefix, return "".

strs = ["class", "clown", "clock"]
#Output: "cl"

def longest_prefixx(strs):

    prefix = ""

    for i in range(len(strs[0])):
        for s in strs:
            if s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix
print(longest_prefixx(strs))


