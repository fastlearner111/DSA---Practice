#Given an array, return the first duplicate number you find. If no duplicate exists return -1.
s =  [1, 2, 3, 1]
#Output: 1

#Input: [1, 2, 3, 4]
#Output: -1


def check_duplicate(s):
    seen = set()
    for number in s:
        if number in seen:
            return number
        else:
            seen.add(number)
    return -1
print(check_duplicate(s))