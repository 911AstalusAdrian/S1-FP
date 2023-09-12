import unittest
import math
from texttable import Texttable

"""
Divide & conquer
"""

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive)
"""

'''
1.a Recursive implementation
'''


# divide and conquer recursive
def find_min(array, l, r, min):
    # if the list has only one element remaining
    if l == r:
        if min > array[l]:
            min = array[l]
        return min
    # divide the list into two sublists
    mid = (l + r) // 2
    # checking if the minimum of the "left" list is smaller than the current minimum
    min = find_min(array, l, mid, min)
    # checking if the minimum of the right list is smaller than the current minimum
    min = find_min(array, mid + 1, r, min)
    return min


def test():
    array = [1, 7, 15, -8, 99, 6, -15, 3, 45]
    min = find_min(array, 0, len(array) - 1, math.inf)
    assert min == -15
    array = [1, 22, 17, -124]
    min = find_min(array, 0, len(array) - 1, math.inf)
    assert min == -124
    array = [100, 17, 0, 2]
    min = find_min(array, 0, len(array) - 1, math.inf)
    assert min == 0


'''
1. Recursive chip & conquer implementation
'''


def get_min(nums):
    """
    This function determines the minimum number in the given list, using a chip & conquer approach.

    :param nums: The list of numbers
    :return: The minimum number
    """
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    return min(nums[0], get_min(nums[1:]))


class TestGetMin(unittest.TestCase):
    def test_get_min(self):
        numbers = [91, 6, 78, -4, 12, -67]
        self.assertEqual(-67, get_min(numbers))

        numbers = [0, 0, 0, 5]
        self.assertEqual(0, get_min(numbers))

        numbers = [-5, -78, -100, -203]
        self.assertEqual(-203, get_min(numbers))

        numbers = [4, 5, 3, 2, 1]
        self.assertEqual(1, get_min(numbers))

        numbers = []
        self.assertEqual(None, get_min(numbers))


"""
2. Calculate the GCD of the numbers in a list (chip & conquer, divide in halves, recursive vs non-recursive)
"""

'''
2.b iterative implementation 
    - explicitly creates and manages the stack
    - recursive implementation uses the data from Python's call stack
'''


def GCD_iterative(list_of_nr):
    gcd = 0
    stack = [list_of_nr[:len(list_of_nr) // 2], list_of_nr[len(list_of_nr) // 2:]]
    while stack:
        for el in stack:
            if len(el) > 1:
                stack.append(el[:len(el) // 2])
                stack.append(el[len(el) // 2:])
                stack.remove(el)
                break

            else:
                gcd = math.gcd(gcd, el[0])
            stack.remove(el)

    return gcd


def test_GCD_iterative():
    list = [14, 28, 7, 35]
    assert GCD_iterative(list) == 7


'''
'''

"""
3. Given a positive number n, calculate its r-th root with a given precision p
"""


# Uses binary search - https://www.geeksforgeeks.org/calculating-n-th-real-root-using-binary-search/
def Rth_root_iterative(n, r, p, low, high):
    mid = (low + high) / 2
    if abs(mid ** r - n) < p:
        return mid

    if mid ** r > n:
        return Rth_root_iterative(n, r, p, low, mid)
    else:
        return Rth_root_iterative(n, r, p, mid, high)


def test_rth_root():
    assert Rth_root_iterative(15, 5, 0.001, 1, 5) == 1.71875


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


def print_board(board):
    table = Texttable()
    for i in range(len(board)):
        table.add_row(board[i])
    print(table.draw())


def n_queen(board, col, rd=[0] * 30, ld=[0] * 30, cl=[0] * 30):
    """
    backtracking
    """
    n = len(board)
    if col >= n:
        print_board(board)
        return True

    for i in range(n):
        if ((ld[i - col + n - 1] != 1 and
             rd[i + col] != 1)
                and cl[i] != 1):

            board[i][col] = 1
            ld[i - col + n - 1] = rd[i + col] = cl[i] = 1

            if n_queen(board, col + 1, rd, ld, cl):
                return True

            board[i][col] = 0
            ld[i - col + n - 1] = rd[i + col] = cl[i] = 0

    return False


def n_queen_test():
    board1 = [[0 for x in range(4)] for y in range(4)]  # 4 by 4
    board2 = [[0 for x in range(10)] for y in range(10)]  # 10 by 10
    board3 = [[0 for x in range(1)] for y in range(1)]  # 1 by 1
    assert n_queen(board1, 0, [0] * 30, [0] * 30, [0] * 30) == True
    assert n_queen(board2, 0, [0] * 30, [0] * 30, [0] * 30) == True
    assert n_queen(board3, 0, [0] * 30, [0] * 30, [0] * 30) == True


"""
5. Generate all the N x N Latin squares for a given number N. 
A Latin square is an n × n array filled with n different symbols, each occurring exactly once in each row and exactly 
once in each column
"""

"""
6. Maximum subarray sum. (subarray = one or more elements on consecutive positions in a list) 
"""
