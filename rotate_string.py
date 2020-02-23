"""
Determine the smallest rotated string

You are given a string of length n and an integer k. The string can be manipulated by taking one of the first k
letters  and moving it to the end of the string.

Write a program to determine the lexicographically smallest string that can be created  after an unlimited number of
moves.

For example, suppose we are given the string 'daily' and k = 1. The best we can create in this case is 'ailyd'.
"""


def swap_string(string, i, j):
    string = list(string)

    #rotate so that i is at the beginning.
    while i > 0:
        string = string[i:] + string[:i]
        i -= 1

        # move the first 2 letters to the end in reversed order
        string = string[:1] + string[2:] + string[1:2]
        string = string[1:] + string[:1]

        # rotate  back to the initial position
        while len(string) > j + 1:
            string = string[1:] + string[:1]
            j += 1

        return ''.join(string)


def rotate_string(string, k):
    string = list(string)

    if k == 1:
        best = string
        for i in range(1, len(string)):
            if string[i:] + string[:i] < best:
                best = string[i:] + string[:i]
        return best
    else:
        return ''.join(sorted(string))


print('Swap string')
print(swap_string('daily', 2, 1))
print(rotate_string(swap_string('daily', 2, 1), 2))

print(swap_string('appreciate', 2, 1))
print(rotate_string(swap_string('appreciate', 2, 1), 1))
print(rotate_string(swap_string('appreciate', 2, 1), 2))

print("Rotate string")
s = rotate_string('daily', 1)
print(s)
s = rotate_string('daily', 2)
print(s)
s = rotate_string('daily', 3)
print(s)
s = rotate_string('appreciate', 2)
print(s)
