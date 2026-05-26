#Given an array, return True only if any number appears
#MORE THAN TWICE. Appearing exactly twice does not count.
s =  [1, 2, 3, 1, 1]
#Output: True  (1 appears 3 times)

#Input: [1, 2, 3, 1]
#Output: False  (1 appears exactly twice, not more)

# so by lookig at the ouput expected I know that I need dict
# so count = {}
# then this ooks kinda like the frequency map thing, so we are gonna store which numbr is repetd how
# many times and then
# we are gonna create another loop to see if > 2 or not then if yes return True else False

def count_appear(s):
    count = {}

    for number in s:
        if number in count:
            count[number] +=1
        else:
            count[number] = 1

    for value in count.values():
        if value > 2:
            return True
    return False
print(count_appear(s))