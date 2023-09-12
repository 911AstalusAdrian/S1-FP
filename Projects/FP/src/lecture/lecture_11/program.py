from texttable import Texttable
from time import perf_counter

"""
Lecture 01 - 10
    programming in the large
        - procedural programming
        - modular programming
        - object-oriented programming (user defined types)
        - layered architecture
            & some other things

Lecture 11 - 13
    programming in the small
        - recursion
        - computational complexity
        - some search & sort algorithms
            -> depth-first search (tree)
            -> quick-sort, bubble-sort, merge-sort, insert, cocktail, ..., selection, random, ...
        - problem solving methods
            - backtracking, divide & conquer, greedy, dynamic programming (2x lectures)

0 1 1 2 3 5 8 13 21 34 55
"""


def fib_iterative(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    val = [0, 1]
    index = 3
    aux = None
    while index <= n:
        aux = sum(val)
        index += 1
        val[index % 2] = aux
    return aux


def fib_recursive(n):
    '''
    1. Make sure you have a basic case, where the recursion stops
    '''
    if n == 1:
        return 0
    if n == 2:
        return 1
    '''
    2. Recursive step
    3. Make sure it progresses towards the basic case
    '''
    return fib_recursive(n - 2) + fib_recursive(n - 1)


'''
lazy loading (proxy design pattern)
'''

d = {1: 0, 2: 1}


def fib_recursive_opt(n):
    if n not in d:
        d[n] = fib_recursive_opt(n - 2) + fib_recursive_opt(n - 1)
    return d[n]


t = Texttable()
t.header(['N', 'Iter', 'Rec', 'Opt'])
numbers = range(20, 38, 2)

for number in numbers:
    t1 = perf_counter()
    fib_iterative(number)
    t2 = perf_counter()
    fib_recursive(number)
    t3 = perf_counter()
    fib_recursive_opt(number)
    d = {1: 0, 2: 1}
    t4 = perf_counter()
    t.add_row([number, t2 - t1, t3 - t2, t4 - t3])

print(t.draw())
