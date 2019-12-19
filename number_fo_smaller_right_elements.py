"""
Problem 3: Given an array of integers, return a new array where each element in the new array is the number of smaller
           elements to the right of that element in the original input array.

           For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since

           * There is 1 smaller element to the right of 3
           * There is 1 smaller element to the right of 4
           * There are 2 smaller element to the right of 9
           * There is 1 smaller element to the right of 6
           * There are no smaller element to the right of 1
"""


def smaller_element_counts(numbers):
    result = list()
    for i, number in enumerate(numbers):
        count = sum(value < number for value in numbers[i + 1:])
        result.append(count)
    return result


print(smaller_element_counts([3, 4, 9, 6, 1]))

print(smaller_element_counts([0, 0, 4, 9, 6, 1]))

print(smaller_element_counts([0, -1, 4, 9, 6, 1]))

print(smaller_element_counts([-1, -2, -4, 9, 6, 1]))
