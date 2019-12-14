
"""
Problem #1: This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

numbers_list_1 = [10, 15, 3, 7, 0]
numbers_list_2 = [10, 15, 3, 7, 0, 0]
numbers_list_3 = [10, -15, -10, 7, 0, -5]
k = 17


def sum_of_two_is_k(numbers, sum_total):
    result = set()                        # storage for holding the difference between the given k # and current number
    for number in numbers:                # loop through the list and...
        if sum_total - number in result:  # evaluate that the difference is in the result set. If yes,
            return True                   # return True
        result.add(number)                # otherwise, add the difference to the result set, and continue looping
    return False                          # return False if all numbers were evaluated and did not meet the if criteria.


print(sum_of_two_is_k(numbers_list_1, k))
print(sum_of_two_is_k(numbers_list_1, 0))
print(sum_of_two_is_k(numbers_list_2, 0))
print(sum_of_two_is_k(numbers_list_2, 11))
print(sum_of_two_is_k(numbers_list_3, -15))
print(sum_of_two_is_k(numbers_list_3, -30))
