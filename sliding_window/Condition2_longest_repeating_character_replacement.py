#Longest Repeating Character Replacement  
#You are given a string s and an integer k.
#You can choose any character in the string 
#and change it to any other uppercase English character.
#Return the length of the longest substring 
#containing the same letter you can get after performing at most k operations.
s = "AABABBA"
k = 1
#Output: 4
#Explanation: Replace the 'B' in "AABA" to get "AAAA".


def charReplacement(s,k):
    freq = {}
    left = 0
    maxFreq = 0
    ans = 0

    for right in range(len(s)):
        ch = s[right]
        freq[ch] = freq.get(ch,0) + 1
        maxFreq = max(maxFreq, freq[ch])

        while (right - left + 1) - maxFreq > k:
            left_ch = s[left]
            freq[left_ch] -= 1
            left += 1
            
        ans = max(ans, right - left + 1)
    return ans
print(charReplacement(s,k))