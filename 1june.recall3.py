#You are given two strings word1 and word2. Merge them 
#by adding letters in alternating order starting with word1.
#Append remaining characters from the longer string.

word1 = "ab"
word2 = "xyz"
#Output: "axbyz"

#  

def merge_string(word1,word2):
    result = ""

    for i in range(0, min(len(word1), len(word2))):
        result += word1[i]
        result += word2[i]
    result += word1[i+1:]
    result += word2[i+1:]

    return result
print(merge_string(word1,word2))
