
"""
Problem #1: This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

numbers_list = [10, 15, 3, 7]
k = 17
m = 18


def sum_of_two_is_k(numbers, sum_total):
    for number in numbers:
        difference = sum_total - number
        if difference in numbers:
            return True
        return False


print(sum_of_two_is_k(numbers_list, k))
print(sum_of_two_is_k(numbers_list, m))
