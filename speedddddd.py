#Given two strings word1 and word2, merge them alternately.
#Start with word1. If one string is longer, append the rest.

#word1 = "abc"
#word2 = "pqr"
#Output: "apbqcr"
#
word1 = "ab"
word2 = "pqrs"
#Output: "apbqrs"

def merge_sort(word1,word2):
    result = ""

    for i in range(0, min(len(word1), len(word2))):
        result += word1[i]
        result += word2[i]
    result += word1[i+1:]
    result += word2[i+1:]
    return result
print(merge_sort(word1,word2))

