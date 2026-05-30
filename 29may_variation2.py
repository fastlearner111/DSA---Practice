
strs = []
strs = [s.lower() for s in strs]

def check_length(strs):
    if not strs:
              return ""
    strs = [s.lower() for s in strs]
    prefix = ''

    for i in range(len(strs[0])):
        
        for s in strs:
            if  i >= len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
        
    return prefix
print(check_length(strs))