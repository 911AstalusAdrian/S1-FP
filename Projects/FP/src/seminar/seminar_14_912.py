from texttable import Texttable

"""
===================================================================
Shaking hands problem (dynamic programming using Catalan Numbers)

There are 2n people around a rounded table. In how many ways they
can shake their hands (in pairs of 2) without intersecting each
other
sources: http://campion.edu.ro/arhiva/www/arhiva_2009/papers/paper20.pdf
"""
from texttable import Texttable


def print_pretty(a):
    t = Texttable()
    t.header(["X"] + list(range(len(a))))
    t.add_row(["V"] + a)
    print(t.draw())


def shaking_hands(n):
    a = [0 for i in range(n + 1)]
    a[0] = 1

    for i in range(1, n + 1):
        for j in range(0, i):
            a[i] += a[j] * a[i - j - 1]
    print_pretty(a)
    return a[n]


shaking_hands(4)
# shaking_hands(int(input("number of pairs: ")))

"""
-= Edit distance =-

Given two strings str1 and str2, the operations below that can performed on str1. Find minimum number of operations to
convert ‘str1’ into ‘str2’.

Operations:
    1. Insert character
    2. Remove character
    3. Replace character
All of the above operations are of equal cost.

where?
    spell checking (Levenshtein distance -> cost 2 for replace, cost 1 for insert/remove)

"""

# 'abc' -> '' (3 operations)
# 'abc' -> 'axc' (1 operation)

'''
v1 - brute force algorithm
'''


def edit_distance_bf(str1, str2):
    # base case, one string is empty
    # if min(len(str1), len(str2)) == 0:
    #     return len(str1) + len(str2)

    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    # common last letter
    if str1[-1] == str2[-1]:
        return edit_distance_bf(str1[:-1], str2[:-1])

    # last char is not common
    return 1 + min(edit_distance_bf(str1, str2[:-1]), edit_distance_bf(str1[:-1], str2),
                   edit_distance_bf(str1[:-1], str2[:-1]))


'''
v2 - dynamic programming

"Those who forget the past are condemned to repeat it"
    - dynamic programming
    
-> DP is (in many cases) an optimization for doing away with recursion 
'''


def pretty_print(T, str1, str2):
    t = Texttable()

    t.header('  ' + str1)
    for i in range(len(str2) + 1):
        t.add_row(([str2[i - 1]] if i > 0 else [' ']) + T[i])

    print(t.draw())


# str1 -> str2
def edit_distance_dp(str1, str2):
    n = len(str1)
    m = len(str2)

    T = [[0 for i in range(n + 1)] for j in range(m + 1)]

    # Basic case (from/to an empty string)
    for i in range(n + 1):
        T[0][i] = i
    for j in range(m + 1):
        T[j][0] = j

    # fill in the rest of the table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # common last letter
            if str1[i - 1] == str2[j - 1]:
                T[j][i] = T[j - 1][i - 1]
            else:
                T[j][i] = 1 + min(T[j - 1][i], T[j][i - 1], T[j - 1][i - 1])

    pretty_print(T, str1, str2)


print(edit_distance_dp('Harry', 'blueberry'))
# print(edit_distance_dp('abc', 'aXc'))
# print(edit_distance_dp('abracadabra', 'avada kedeavra?'))

# 'harry' -> 'blueberry'
# 'ha' -> 'bluebe' => 'bl' (2 x replace) => 'bluebe' (4 x insert) => 6 operations
