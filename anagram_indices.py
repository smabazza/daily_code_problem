"""
Problem 2.1
Given a word w and a string s, find all indices in s which are the starting locations of anagrams of w.
For example, given w is 'ab' and s is 'abxaba', return [0, 3, 4]

"""

from collections import defaultdict


def delete_if_zero(dictionary, char):
    """ Checks that the char count is 0 and deletes the char

    Args:
        dictionary: The dictionary containing the counts of the occurnences of char
        char: The character to check

    Returns: N/A
    """
    if dictionary[char] == 0:
        del dictionary[char]


def anagram_indices(word, s):
    result = []

    frequency = defaultdict(int)    # dictionary to hold the count the occurence of each char in word
    # e.g word = 'ab', should be {'a': 1, 'b': 1}

    for char in word:               # loop through the given word
        frequency[char] += 1        # increment the count of the new char

    for char in s[:len(word)]:    # get a char from the substring starting at index 0 up to the length of the given word
        frequency[char] -= 1      # decrement the count of the old char
        delete_if_zero(frequency, char)   # if the char count is 0, delete the char from the dictionary

    if not frequency:               # check that the frequency dictionary is not empty
        result.append(0)            # add to result list

    for i in range(len(word), len(s)):                 # loop thru the rest of the string
        start_char, end_char = s[i - len(word)], s[i]  # get the current starting char and ending char
        frequency[start_char] += 1                     # add the char to the frequency dictionary with the count
        delete_if_zero(frequency, start_char)          # and check if char count is zero

        frequency[end_char] -= 1                       # decrement the count of the ending char
        delete_if_zero(frequency, end_char)            # and check that char count is zero

        if not frequency:                              # check that the frequency dictionary is not empty
            beginning_index = i - len(word) + 1        # update the beginning index
            result.append(beginning_index)             # and add the value to result list

    return result


x = anagram_indices('ab', 'abxaba')
print(x)
y = anagram_indices('ab', 'xabyaba')
print(y)
z = anagram_indices('ab', ' ab x bab ')
print(z)
a = anagram_indices('bab', ' ab x bab a')
print(a)
b = anagram_indices('silent', 'xlsient$listenzstenilnelites')
print(b)