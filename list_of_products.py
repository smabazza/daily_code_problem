"""
Problem #2: This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""


def make_products_list(numbers):

    # prefix_products is a list containing the products of numbers before the index. Initially empty
    prefix_products = []
    for number in numbers:
        if prefix_products:  #If list is not empty, multiply the number by the previous product in the list and append the product
            prefix_products.append(prefix_products[-1] * number)
        else:             # if list is empty, it means this is the first number so append the current number to the list
            prefix_products.append(number)

    # Suffix products. Same logic as in prefix products except that the input list is reversed
    suffix_products = []
    for number in reversed(numbers):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * number)
        else:
            suffix_products.append(number)
    suffix_products = list(reversed(suffix_products))

    # Generate result from the product of prefixes and suffixes
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(numbers) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])

    return result


input_1 = [3, 2, 1]
result_1 = make_products_list(input_1)
print(result_1)
input_2 = [1, 2, 3, 4, 5]
result_2 = make_products_list(input_2)
print(result_2)
input_3 = [2, 4, 6, 8, 10]
print(make_products_list(input_3))

