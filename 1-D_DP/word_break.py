s = "applepenapple"
wordDict = ["apple","pen","ape"]

#Output: true

class Solution:
    def word_break(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)
        dp = True + False * n

        for i in range(1, n + 1):
            dp[i] = any(
                dp[j] and s[j:1] in word_set
                for j in range(i)
            )

        return dp[n]