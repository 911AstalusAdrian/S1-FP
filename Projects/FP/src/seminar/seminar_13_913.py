"""
Divide & conquer
"""

"""
1. Calculate the product of even numbers found on even positions in a list
"""


# marc
def even_pos_even_numbers_prod_iter(list_of_numbers):
    total = 1
    stack = []
    stack.append(list_of_numbers)
    while stack:
        last_elem = stack.pop()
        size = len(last_elem)
        if size > 1:
            if size == len(list_of_numbers):
                even = 2
            else:
                even = 1
            stack.append(last_elem[size // 2::even])
            stack.append(last_elem[:size // 2:even])
        else:
            if last_elem and last_elem[0] % 2 == 0:
                total *= last_elem[0]
        # sleep(2)

    return total


def test():
    tests = [
        ([1, 2, 3, 4, 5], 1),
        ([2, 3, 3, 4, 4], 8),
        ([2], 2),
        ([1], 1),
        ([13, 22, 2, 100, 20, 19, 19, 200, 20], 800),
        ([2, 4, 6, 8], 12)
    ]
    for t in tests:
        assert even_pos_even_numbers_prod_iter(t[0]) == t[1]


test()

"""
2. Calculate the GCD of the numbers in a list (chip & conquer, divide in halves, recursive vs non-recursive)
"""


# Recursive, chip & conquer implementation
def gcd_recursive(list_, result=None):
    """
    Computes the gcd of items of a list recursively
    :param list_: List[int] - the list of numbers
    :param result: int - the previous result
    :return: int - the gcd of all items
    """

    def _gcd(a, b):
        return a if b == 0 else _gcd(b, a % b)

    if result is None:
        result = list_.pop(0)
    return gcd_recursive(list_, _gcd(list_.pop(0), result)) if len(list_) > 0 else result


def test_gcd_recursive():
    assert gcd_recursive([10, 20, 30, 40, 50]) == 10
    assert gcd_recursive([5, 10, 20, 30]) == 5
    assert gcd_recursive([1, 2, 3]) == 1
    assert gcd_recursive([3, 6, 333]) == 3


# ---------------------

# TODO You can use math.gcd(...)
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def arr_gcd(array):
    """
    Found the gcd of the numbers in the array
    :param array: the list of numbers that we'll calculate the gcd for
    :return: the gcd of the current array
    """
    # TODO Does not work for arrays of length 1
    lg = len(array)
    if lg == 2:
        return gcd(array[0], array[1])

    a = arr_gcd(array[0:lg // 2 + 1])
    b = arr_gcd(array[lg // 2:lg + 1])
    return gcd(a, b)


def test_arr_gcd():
    array = [150, 30, 15, 3, 12]
    assert arr_gcd(array) == 3
    array = [5, 6, 120, 5]
    assert arr_gcd(array) == 1
    array = [3000, 300, 120, 150]
    assert arr_gcd(array) == 30
    array = [3000, 2000]
    assert arr_gcd(array) == 1000


test_arr_gcd()

"""
3. Given a positive number n, calculate its r-th root with a given precision p
"""

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


# TODO Add pretty-printing
def n_queen(board, size, step=None):
    """
    Generates the n-queen board
    :param board: List[List[int]] - the board that should be modified
    :param size: int - the size of the board
    :param step: int - the current step
    """

    def another_queen_exists(x, y):
        for i in range(0, size):
            if board[x][i] == 1 or board[i][y] == 1:
                return True
        for i in range(0, size):
            for j in range(0, size):
                if i + j == x + y or i - j == x - y:
                    if board[i][j] == 1:
                        return True
        return False

    if step is None:
        step = size
    if step == 0:
        return True
    for i in range(0, size):
        for j in range(0, size):
            if not another_queen_exists(i, j) and board[i][j] == 0:
                board[i][j] = 1
                if n_queen(board, size, step - 1):
                    return True
                board[i][j] = 0
    return False


"""
5. Generate all the N x N Latin squares for a given number N. 
A Latin square is an n × n array filled with n different symbols, each occurring exactly once in each row and exactly 
once in each column
"""

"""
6. Maximum subarray sum. (subarray = one or more elements on consecutive positions in a list) 
"""


def max_sum(elements, left, middle, final):
    '''
    Computes the maximum sum between the the elements to the left of the middle, the elements to the right of the middle
    and the whole list of elements
    :param elements: the list of elements(list)
    :param left: the current left bound of the list (int)
    :param middle: the current middle point of the list (int)
    :param final: the current end of the list (int)
    :return: the maximum sum between the the elements to the left of the middle, the elements to the right of the middle
    and the whole list of elements
    '''
    S = 0
    left_sum = -100000  # better: -float("inf"), or elements[middle]

    for i in range(middle, left - 1, -1):
        S += elements[i]

        if S > left_sum:
            left_sum = S

    S = 0
    right_sum = -100000

    for i in range(middle + 1, final + 1):
        S += elements[i]

        if S > right_sum:
            right_sum = S

    return max(left_sum + right_sum, left_sum, right_sum)


def div_conq_max_subarray_sum(elements, left, final):
    '''
    Computes the maximum sum of elements between each subarray of the list
    :param elements: the list of elements (list)
    :param left: the current left bound of the list (int)
    :param final: the current right bound of the list (int)
    :return: the maximum sum of elements between each subarray of the list
    '''
    if left == final:
        return elements[left]

    middle = (left + final) // 2

    max1 = div_conq_max_subarray_sum(elements, left, middle)
    max2 = div_conq_max_subarray_sum(elements, middle + 1, final)
    max3 = max_sum(elements, left, middle, final)

    return max(max1, max2, max3)


def test():
    elements = [24, -5, -32, 68, 29, -1, 0, 39]

    final = len(elements)

    sum = div_conq_max_subarray_sum(elements, 0, final - 1)

    assert sum == 135


# test()

# ---------------------
# Maximum subarray sum problem
data = [-2, -5, 6, -2, -3, 1, 5, -6]
# max subarray value is 7, and the subarray is [6, -2, -3, 1, 5]

"""
Variant 1
    - 2 for loops (one for the start, one for the end of the subarray)
    (we update the partial sum when we go through the list using the second for loop)
    Time complexity => T(n) is O(n^2)

Variant 2 (divide & conquer)
    (implementation above)
    T(n) = 1, length 1
    T(n) = 2 * T(n/2) + n (similar to merge sort)

Variant 3 (dynamic programming)
    week 14
"""










