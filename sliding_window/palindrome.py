s = "Was it a car or a cat I saw?"
#Output: true

def check_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    left = 0
    right = len(s) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
        return True