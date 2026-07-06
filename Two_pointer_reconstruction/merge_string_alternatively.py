#Given two strings word1 and word2, merge them alternately.
#Start with word1. If one string is longer, append the remaining characters.
#
word1 = "abc"
word2 = "pqr"
#Output: "apbqcr"
#
#Input:  word1 = "ab", word2 = "pqrs"
#Output: "apbqrs"
#
#Input:  word1 = "abcd", word2 = "pq"
#Output: "apbqcd"


def merge_alt(word1, word2):
    result = ""
    m = min(len(word1), len(word2))

    for i in range(m):
        result += word1[i]
        result += word2[i]
    result += word1[m:]
    result += word2[m:]
    return result
print(merge_alt(word1, word2))
