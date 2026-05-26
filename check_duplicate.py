# so first we need a set
# we are gonna say if the number in seen then return  true
# else false
s = [1, 2, 3, 1]
#Output: True
def check_duplicate(s):
    seen = set()
    for number in s:
        if number in seen:
            return True
        else:
            seen.add(number)
    return False
print(check_duplicate(s))