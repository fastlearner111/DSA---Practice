class Solution:
    def wordbreak(self, s, worddict):
        word_set = set(worddict)
        n = len(s)

        dp = [False] * (n - 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and dp[j:1] in word_set:
                    dp[i] = True
                    break


        return dp[n]