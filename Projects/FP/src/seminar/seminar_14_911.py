from texttable import Texttable

"""
BARABAS ELINA
source: https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/

Egyptian Fraction Representantion

Every positive fraction can be represented as sum of unique unit fractions. A fraction is unit fraction if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction. Such a representation is called Egyptian Fraction as it was used by ancient Egyptians.

Following are few examples:

Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156
"""

import math


def egyptian_fraction(numerator, denominator):
    """

    :param numerator: the numerator of that function that will be displayed in the Egyptian Fraction Representation
    :param denominator: the denominator of that function that will be displayed in the Egyptian Fraction Representation
    :return: the Egyptian Fraction Representation of the fraction numerator/denominator
    """

    print("The Egyptian Fraction " +
          "Representation of {0}/{1} is".
          format(numerator, denominator), end="\n")

    Egyptian_Fraction = []

    while numerator >= 1:
        denominator_first_unit_fraction = math.ceil(denominator / numerator)

        Egyptian_Fraction.append(denominator_first_unit_fraction)

        numerator = denominator_first_unit_fraction * numerator - denominator
        denominator = denominator * denominator_first_unit_fraction

    for index in range(len(Egyptian_Fraction)):
        if index != len(Egyptian_Fraction) - 1:
            print(" 1/{0} +".
                  format(Egyptian_Fraction[index]), end=" ")
        else:
            print(" 1/{0}".
                  format(Egyptian_Fraction[index]), end=" ")


egyptian_fraction(99, 100)

"""
How do we compute the Egyptian Fraction Representation of 4/5?

It's simple

Egyptian_Fraction = []

We start by computing the ceil value* of the inverse of our fraction (5/4) ---> math.ceil(5/4)=2

So 2 will be the denominator of the the first unit fraction

REMEMBER! Every unit fraction has numerator=1 
(so the fraction is reduced to a form where denominator is greater than numerator 
    and numerator does not divide denominator.) 

Egyptian_Fraction = [1/2]

4/5=1/2+s ----> s=4/5-1/2 ----> s=(2*4)/(2*5)-(5*1)/(5*2) ----> s=3/10

Now we start again until the numerator becomes 1

math.ceil(10/3)=4

3/10=1/4+s ----> s=3/10-1/4 ----> s=(4*3)/(4*10)-(10*1)/(10*4) ----> s=2/40 ----> s=1/20

Egyptian_Fraction = [1/2, 1/4]

We notice that s=1/20 has the numerator 1, so we will stop and s will be the last unit fraction

Egyptian_Fraction = [1/2, 1/4, 1/20]

SO, The Egyptian Fraction Representation of 4/5 is 1/2 + 1/4 + 1/20 

ceil value*= the smallest integer greater than or equal to the given number.
"""

"""
-= Weighted interval scheduling =-

You have to schedule N jobs on a computer. Each job is represented by following elements:
    1. Start Time (s_i)
    2. Finish Time (f_i)
    3. Value (v_i, >= 0)
Find the subset of jobs with maximum value, so that no two jobs in overlap

e.g.
# All jobs we want to schedule (start, end, value)
jobs = [(0, 3, 3), (1, 4, 2), (0, 5, 4), (3, 6, 1), (4, 7, 2), (3, 9, 5), (5, 10, 2), (8, 10, 1)]

!! if all jobs have the same value => greedy implementation is optimal
"""

# All jobs we want to schedule (start, end, value)
jobs = [(0, 3, 3), (1, 4, 2), (0, 5, 4), (3, 6, 1), (4, 7, 2), (3, 9, 5), (5, 10, 2), (8, 10, 1)]

'''
v1 - Brute force algorithm
'''


def jobs_bf_start(data):
    # Sort jobs by their ending time
    data = sorted(data, key=lambda x: x[1])
    return jobs_bf(data, len(data) - 1)


def jobs_bf(data, index):
    # base case !?
    if index < 0:
        return 0

    # find the latest job not overlapping the current one
    next_job = index - 1
    while next_job > -1 and data[next_job][1] > data[index][0]:
        next_job -= 1

    # if -1, make it 0
    # next_job = max(next_job, 0)

    # maximum between including the current job, or excluding it from the solution
    return max(data[index][2] + jobs_bf(data, next_job), jobs_bf(data, index - 1))


'''
v2 - Dynamic programming implementation
!! Dynamic programming is (in many cases) an optimization of recursion
'''


def pretty_print(T):
    t = Texttable()
    t.header(['start', 'end', 'val', 'prev', 'total'])
    for i in range(len(T)):
        t.add_row(T[i])
    print(t.draw())


def jobs_dp(data):
    # Sort jobs by their ending time
    data = sorted(data, key=lambda x: x[1])

    # initialize the matrix
    T = [list(data[i]) + [0, 0] for i in range(len(data))]
    T.insert(0, [0, 0, 0, 0, 0])

    # for each job, calculate latest job that does not intersect it
    for index in range(1, len(T)):
        job_ends = T[index][1]

        # TODO Binary search (jobs are sorted according to their end time)
        last_job = index - 1
        while last_job > -1 and T[last_job][1] > T[index][0]:
            last_job -= 1
        T[index][3] = last_job

    # calculate the totals
    for index in range(len(T)):
        last_compatible_job = T[index][3]
        T[index][4] = max(T[index][2] + T[last_compatible_job][4], T[index - 1][4])

    pretty_print(T)


# jobs_dp(jobs)
# print(jobs_bf_start(jobs))


"""
Borcani Robert-Raul

Problem statement:
    Suppose we have n people and n tasks. Each person will solve exactly one task. If task i is solved by person j,
    the efficiency of solving the task is a[i][j]. Our goal is to maximize the total efficiency by attributing tasks
    optimally. The total efficiency is obtained by adding up all the efficiencies from all of our solved tasks.

    Constraints: 1 <= n <= 18
                 1 <= a[i][j] <= 100

    Input: n - number of people and tasks
           a - n lines with n values each. jth value from ith line denotes a[i][j]

    Output: the maximum efficiency

    {1, 2, 3, 4}
    {1, 3}
    0101

    Example:
        input

        3
        1 1 2
        1 2 1
        2 1 1

        output
        6

        (first task - third person)    = 2
        (second task - second person)  = 2
        (third task - first person)    = 2

        TOTAL EFFICIENCY               = 6
"""
from math import inf
from random import randint

from texttable import Texttable


def read_data():
    """
    Reads the input.
    :return: -
    """
    n = int(input())
    a = []

    for i in range(n):
        a.append([])
        line = input()
        items = line.split(' ')
        for item in items:
            a[-1].append(int(item))

    return n, a


def solve_naive_solution(n, a, index, person, current_efficiency):
    """
    Backtracking approach to solve the problem
    :param n: Number of people and tasks
    :param a: list of lists representing a matrix with n lines with n columns each.
                a[i][j] = efficiency if eprson j solves task i
    :param index: The current person
    :param person: A list with meaning person[i] = who solves task i
    :param current_efficiency: The efficiency until now
    :return: The best efficiency we can achieve.
    """
    # Complexity: O(n!)
    if len(person) == n:
        return current_efficiency

    available_people = []
    for i in range(n):
        if i not in person:  # If person i does not solve any tasks
            available_people.append(i)

    # We try to assign task index to each person
    maximum = -inf
    for current_person in available_people:
        person.append(current_person)
        maximum = max(maximum, solve_naive_solution(n, a, index + 1, person,
                                                    current_efficiency + a[index][current_person]))
        person.pop()

    return maximum


def solve_dp(n, a):
    """
    Dynamic programming approach to solve the problem
    :param n: Number of people and tasks
    :param a: list of lists representing a matrix with n lines with n columns each.
                a[i][j] = efficiency if eprson j solves task i
    :return: The best efficiency we can achieve.
    """
    dp = []
    for i in range(n + 1):
        dp.append([])
        for j in range(1 << n):
            dp[-1].append(-inf)

    # dp[i][mask] = the best efficiency we can achieve by performing the first i tasks using the people marked
    #               in our bitmask (if first bit of bitmask is set => the first person already solved a task)
    #                              (if second bit of bitmask is set => the second person already solved a task)
    #                   etc.

    # Base case:
    dp[0][0] = 0  # The maximum efficiency for solving 0 tasks using no persons if 0
    for i in range(n):
        for mask in range(1 << n):
            # At this point, we chose the first i tasks and a bitmask mask
            # As mask contains all the persons we used so far for solving i tasks, there are some conditions
            # that need to be met in order for the current state to make sense:
            # mask needs to have exactly i bits set
            cnt = 0
            for bit in range(n):
                if (1 << bit) & mask:
                    cnt += 1
            if cnt != i or dp[i][mask] == -inf:
                continue

            # Now, we need to choose which person will solve task i + 1
            # That person must be free (it shouldn't already have any tasks assigned)
            for person in range(n):
                if (1 << person) & mask:
                    continue
                # At this point, we have first i tasks solved by people marked in mask and we found a free person
                # that could, potentially, be suited for solving the next task, which is task i + 1
                next_efficiency = dp[i][mask] + a[i][person]
                if dp[i + 1][mask | (1 << person)] < next_efficiency:
                    dp[i + 1][mask | (1 << person)] = next_efficiency

    print_dp(n, dp)
    # Now, our result should be in dp[n][(1 << n)- 1] - the maximum efficiency to solve first n tasks using all
    # of our people. (1 << n) - 1 is 111...1 (n times) in base 2 <=> taking all people
    return dp[n][(1 << n) - 1]


def print_dp(n, dp):
    tbl = Texttable(150)
    header = ['X']
    for i in range(1 << n):
        header.append(str(i) + ' = ' + b2(i) + '(2)')
    tbl.header(header)

    for i in range(n + 1):
        line = [str(i)]
        for j in range(1 << n):
            line.append(dp[i][j])
        tbl.add_row(line)

    print(tbl.draw())


def b2(n):
    if n < 2:
        return str(n)
    return b2(n // 2) + str(n % 2)


n, a = read_data()
print(solve_naive_solution(n, a, 0, [], 0))
print(str(solve_dp(n, a)))

# for t in range(100):
#    n = randint(1, 8)
#    a = []
#    for i in range(n):
#        a.append([])
#        for j in range(n):
#            a[-1].append(randint(1, 100))
#
#    assert solve_naive_solution(n, a, 0, [], 0) == solve_dp(n, a)
#
#    print(f'Test {t} run successfully!')
