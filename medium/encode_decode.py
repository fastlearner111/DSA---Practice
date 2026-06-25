#Design an algorithm to encode a list of strings to a single string,
#and decode that single string back to the original list.
#
#encode(["neet","code","love","you"]) → "4#neet4#code4#love3#you"
#decode("4#neet4#code4#love3#you") → ["neet","code","love","you"]
#
#encode(["we","say",":","yes"]) → "2#we3#say1#:3#yes"
#decode("2#we3#say1#:3#yes") → ["we","say",":","yes"]
strs =["neet","code","love","you"]
def encode(strs):
    result = ""
    for s in strs:
        result +=  str(len(s)) + '#' + s
    return result
print(encode(strs))

def decode(s):
    result = []
    i = 0
    while i < len(s):
        j = s.index("#", i)
        length = int(s[i:j])
        result.append(s[j+1 : j+1+length])
        i = j + 1 + length
    return result
encoded = encode(strs)
print(decode(encoded))