""" Problem 2.2
Given a list of words, find all pairs of unique indices such that the concatenation  of the two words is a palindrome.
For example, given the list ["code", "edoc", "da", "d"], return [(0,1), (1,0), (2,3)]
"""

def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    d = {}
    for i, word in enumerate(words):
        d[word] = i

    result = []

    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if (is_palindrome(suffix) and reversed_prefix in d):
                if i != d[reversed_prefix]:
                    result.append((i, d[reversed_prefix]))
            if (is_palindrome(prefix) and reversed_suffix in d):
                if i != d[reversed_suffix]:
                    result.append((d[reversed_suffix], i))
    return result

x = ["code", "edoc", "da", "d"]
print(palindrome_pairs(x))
print(palindrome_pairs(["tnelis", "silent", "enlist", "tsilne"]))