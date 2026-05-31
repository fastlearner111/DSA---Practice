#Given two strings word1 and word2, merge them by 
#adding letters in alternating order starting with word1.

word1 = "xyz"
word2 = "ab"
#Output: "xayzbz"

def add_string(word1, word2):

    result = ""

    for i in range(0, min(len(word1), len(word2))):
        result += word1[i]
        result += word2[i]
    result += word1[i+1:]
    result += word2[i+1:]

    return result 
print(add_string(word1,word2))