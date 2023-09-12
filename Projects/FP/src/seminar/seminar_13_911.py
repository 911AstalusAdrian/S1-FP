"""
Divide & conquer
"""

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive)
"""

# Bledea Mihaela-Alexandra - Smallest number in list (iterative)
import sys


# Not an explicit implementation of divide & conquer
# (it's not obvious how the problem is divided into sub-problems)
# (the example below this one illustrates that better)
def find_smallest_number(list):
    """
    We initialize the minimum with a maximum size
    With this function we go through the list of numbers and compare each humber from the list with the one
    initialized with a maximum size, if they are smaller, then the param minimum gets that value
    :param list:the list of numbers through which we go for searching the smalles one
    :return: it returns the smallest number from the list
    """
    minimum = sys.maxsize
    for i in range(0, len(list)):
        if list[i] < minimum:
            minimum = list[i]

    return minimum


def test_find_smallest_number():
    list = [-8, 5, 1, 100, -40]
    minimum = find_smallest_number(list)
    assert minimum == -40


list = [217829, 1, -4, 6, 7, 10]
print(find_smallest_number(list))
test_find_smallest_number()


# ---------------------------------------------------------

# Borcani Robert - iterative chip & conquer
def smallest_number_chip_conquer_iterative(numbers):
    """
    Finds the smallest number from the given list
    :param numbers: A list of numbers
    :return: The smallest number
    """
    current_list = numbers[1:]
    number = numbers[0]

    # This loop illustrates dividing the problem into sub-problmes better
    while current_list:
        number = min(number, current_list[0])
        current_list = current_list[1:]

    return number


# lst = [4, 4, 4, 6, 2]
# print(smallest_number_chip_conquer_iterative((lst)))

# ---------------------------------------------------------

# Andrioaie Daria - Smallest number in a list (recursive chip & conquer)
def smallest_number(given_list):
    """
    The function compares the last element in the list with the smallest number in the list, excepting the last element
    :param given_list: the list of numbers
    :return: the smallest number in the list
    """
    if len(given_list) == 1:
        return given_list[0]

    last_element = given_list[-1]
    smallest_number_in_list_excepting_last_element = smallest_number(given_list[:-1])

    if last_element < smallest_number_in_list_excepting_last_element:
        return last_element

    return smallest_number_in_list_excepting_last_element


def test_smallest_number():
    my_list = [5, 4, 1, 7, 9]
    assert smallest_number(my_list) == 1

    my_list = [-3]
    assert smallest_number(my_list) == -3


# ---------------------------------------------------------
# Boicu Monica - recursive smallest number
def smallest_number(l):
    n = len(l)
    if n == 1:
        return l[0]
    mid_index = n // 2
    return min(smallest_number(l[mid_index:]), smallest_number(l[:mid_index]))


def test_min():
    print(smallest_number([-10, 6, -3, 9, 4]))
    print(smallest_number([-10, 6, -3, -40]))


# test_min()

"""
2. Calculate the product of even numbers found on even positions in a list
"""


# Andrioaie Daria -  product of the even numbers found on even positions in a list: recursive chip and conquer.
def product_of_even_numbers(given_list):
    """
    The function calculates the product of the even numbers found on even positions in a list using recursive chip and
    conquer.

    The main idea is that we check is the length of the initial array is and even number, meaning that the last element
    is on an odd position, case which is not in our interest, so we move recursively back with one position, reaching an
    element on an even position.
    From this point on, we only check if the last element is even and add it to the product of even numbers of the list
    sliced with two elements, such that the last element is always on an even position

    :param given_list: the list
    :return: the calculated product
    """

    # base case
    if len(given_list) == 1:
        if given_list[0] % 2 == 0:
            return given_list[0]
        return 1

    if len(given_list) % 2 == 0:
        return product_of_even_numbers(given_list[:-1])

    last_element = given_list[-1]
    product_of_even_numbers_excepting_last_element = product_of_even_numbers(given_list[:-2])

    # if the length of the list is and odd number, it means that the last element is on an even position
    if last_element % 2 == 0:
        return last_element * product_of_even_numbers_excepting_last_element

    return product_of_even_numbers_excepting_last_element


def test_product_of_even_numbers():
    my_list = [2, 1, 4, 5, 6]
    assert product_of_even_numbers(my_list) == 48

    my_list = [1, 3, 5, 7]
    assert product_of_even_numbers(my_list) == 1


# ---------------------------------------------------------
# Aldea Denise - recursive product (chip and conquer)
def product_recursive(list, index):
    if index < len(list):
        if index % 2 == 0:
            if list[index] % 2 == 0:
                return list[index] * product_recursive(list, index + 2)
            return product_recursive(list, index + 2)
        else:
            return product_recursive(list, index + 1)
    return 1


def test_product():
    print(product_recursive([2, 45, 44, 12, 5], 0))
    print(product_recursive([5552, 45, 744, 12, 35], 0))


test_product()


# ---------------------------------------------------------
# Arsene Gina-Teodora - Iterative product
def iterative_product(array):
    """
    Computes the product of the even numbers, placed on the even positions of an array, by iterating through the array
    from 0 to the end of the array with a step of 2, and checking whether or not the number found on that position is even
    """
    product = 1
    # TODO Good implementation, but not representative of divide & conquer
    for i in range(0, len(array), 2):
        if array[i] % 2 == 0:
            product = product * array[i]
    return product


def test_iterative_product():
    array = [4, 8, 1, 5, -1, 6, -5, 6]
    pr = iterative_product(array)
    assert pr == 4


"""
Backtracking
"""

"""
Recursive implementation for permutations
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


# print(bkt_rec([], 7))

"""
4. Change the code for generating the permutation above to work for the n-Queen problem
"""

"""
5. Generate all the N x N Latin squares for a given number N. 
A Latin square is an n × n array filled with n different symbols, each occurring exactly once in each row and exactly 
once in each column
"""


# Borcani Robert - Latin squares
def WriteMatrix(matrix):
    for row in matrix:
        line = ''
        for column in row:
            line += column + ' '
        print(line)
    print('\n')


def latin_squares(matrix, line, column):
    """
    Computes all latin squares using backtracking
    :param matrix: Th matrix of squares
    :param line: The current line
    :param column: The current column
    :return: -
    """
    if line == len(matrix):
        WriteMatrix(matrix)
        return

    if line == 0 or column == 0:
        if line == 0:
            # TODO Replace chr(ord('A') + column) with numbers and only format for output when printing
            matrix[line][column] = chr(ord('A') + column)
        elif column == 0:
            matrix[line][column] = chr(ord('A') + line)

        if column + 1 < len(matrix):
            latin_squares(matrix, line, column + 1)
        else:
            latin_squares(matrix, line + 1, 0)
    else:
        letters_until_now = []
        for i in range(line):
            letters_until_now.append(matrix[i][column])
        for j in range(column):
            letters_until_now.append(matrix[line][j])

        for current_letter in range(len(matrix)):
            character = chr(ord('A') + current_letter)
            if character in letters_until_now:
                continue
            matrix[line][column] = character

            if column + 1 < len(matrix):
                latin_squares(matrix, line, column + 1)
            else:
                latin_squares(matrix, line + 1, 0)


matrix = []
for i in range(4):
    matrix.append(['*', '*', '*', '*'])

latin_squares(matrix, 0, 0)

"""
6. Maximum subarray sum. (subarray = one or more elements on consecutive positions in a list) 
"""


#
# Divide & Conquer implementation
#
# Besu Dan max subarray sum
def max_crossing_middle_sum(list_, left_index, middle, h):
    # elements on left of middle
    sm = 0
    left_sum = -100000

    for i in range(middle, left_index - 1, -1):
        sm = sm + list_[i]
        if sm > left_sum:
            left_sum = sm

    # elements on right of mid
    sm = 0
    right_sum = -10000
    for i in range(middle + 1, h + 1):
        sm = sm + list_[i]
        if sm > right_sum:
            right_sum = sm

    # return sum of elements on left and right of middle
    return max(left_sum + right_sum, left_sum, right_sum)


def max_subarray_sum(list_, left_index, high_index):
    # only one element
    if left_index == high_index:
        return list_[left_index]

    # find middle point
    m = (left_index + high_index) // 2

    # return maximum of following three possible cases
    return max(max_subarray_sum(list_, left_index, m),  # maximum subarray sum in left half
               max_subarray_sum(list_, m + 1, high_index),  # maximum subarray sum in right half
               max_crossing_middle_sum(list_, left_index, m,
                                       high_index))  # maximum subarray sum such that the subarray crosses the midpoint


def test_max_subarray_sum():
    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    length = len(arr)
    max_sum = max_subarray_sum(arr, 0, length - 1)
    assert max_sum == 7

    arr = [2, 3, 4, 5, 7]
    length = len(arr)
    max_sum = max_subarray_sum(arr, 0, length - 1)
    assert max_sum == 21


# ----
# Maximum subarray sum
# subarray = a bunch of numbers with consecutive array indices
data = [-2, -5, 6, -2, -3, 1, 5, -6]


# In this example, the max subarray sum value is 7 (subarrray is [6, -2, -3, 1, 5])

# Variants to solve this problem
# variant 1 -> 3 for loops => time complexity is O(n^3)
# 1 sets the start of the subarray
# 1 sets the end of the subarray
# 1 counts the sum of the current subarray

# variant 2 -> 2 for loops => time complexity is O(n^2)
# Eliminate one for loop by making the loop that sets the array end also count partial sums

# variant 3 -> divide and conquer
# T(n) = 1, n == 1
# T(n) = 2 * T(n/2) + n (same as merge sort) => time complexity O(n*log(n))

# variant 4 -> dynamic programming
# time complexity is O(n) (we have a single for loop over the list)

# ----

#
# Dynamic Programming implementation
#
# Borcani Robert - Maximum subarray sum
# TODO This implementation is a bit more convoluted than in can be
def max_subarray_sum(numbers):
    """
    The maximum subarray sum
    :param numbers: A list of numbers
    :return: The maximum subarray sum
    """
    partial_sums = []
    for i in range(len(numbers)):
        partial_sums.append(numbers[i])
        if i > 0:
            partial_sums[i] += partial_sums[i - 1]

    minimum = 0
    max_sum = 0
    for i in range(len(numbers)):
        max_sum = max(max_sum, partial_sums[i] - minimum)
        minimum = min(minimum, partial_sums[i])

    return max_sum

# lst = [4, -1, 4, -6, 20]
# print(max_subarray_sum((lst)))
