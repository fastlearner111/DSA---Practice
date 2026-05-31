#You are given two strings word1 and word2. Merge the 
#strings by adding letters in alternating order, starting 
#with word1. If a string is longer than the other, append 
#the additional letters onto the end of the merged string.

#Input:  word1 = "abc", word2 = "pqr"
#Output: "apbqcr"

word1 = "ab"
word2 = "pqrs"
#Output: "apbqrs"

#Input:  word1 = "abcd", word2 = "pq"
#Output: "apbqcd"

def merge_string(word1, word2):

    result = ""

    for i in range(0, min(len(word1), len(word2))):
        result += word1[i]
        result += word2[i]
    result += word1[i+1:]
    result += word2[i+1:]

    return result
print(merge_string(word1,word2))

