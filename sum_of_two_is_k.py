
"""
Problem #1: This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

numbers_list_1 = [10, 15, 3, 7, 0]
numbers_list_2= [10, 15, 3, 7, 0, 0]
k = 17


def sum_of_two_is_k(numbers, sum_total):
    result = set()
    for number in numbers:
        if sum_total - number in result:
            return True
        result.add(number)
    return False


print(sum_of_two_is_k(numbers_list_1, k))
print(sum_of_two_is_k(numbers_list_1, 0))
print(sum_of_two_is_k(numbers_list_2, 0))
