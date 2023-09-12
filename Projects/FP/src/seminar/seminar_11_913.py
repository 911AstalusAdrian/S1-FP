"""
Computational complexity
"""

'''
1
----------------
found ← false 
for i ← 1, n do
    if 𝑥𝑖 =𝑎 then 
        found ← true
    endif 
endfor

How to think about comp. complexity ?
n - size of the program's input (length of a list, size of a dict, rows * columns in a matrix etc.)
T(n) - number of operations made by the program 
    - keep it (very) simple
    - each operation (or constant block of operations) is assumed to take 1 unit of time

T(n) = n, T(n) is a linear algorithm (belongs to O(n))
BC == AC == WC 

2
----------------
found = False
for i in range(1,n):
    if x[i] == a:
    return i
return -1
    
BC(A) = 1, O(1) algorithm, runs in constant time
WC(A) = n, O(n) algorithm, runs in linear time

AC(A) = can only be calculated by making some assumptions
    1. assume value is in the list
    2. assume same probability of it being in any place 
AC(A) = n / 2, still O(n) algorithm, runs in linear time

3
----------------
T(n) = n^2 ( n^2 + 1) / 2 => T(n) is an O(n^4) algorithm

4
-----------------
def f2(l): 
    sum = 0
    for el in l:
        j = len(l)
        while j>1:
            sum+=el*j
            j=j//3
    return sum

size of algorithm's input -> len(l) (length of the iterable)
T(n) = n * log_3(n)

5
-----------------
def sumaR(l): 
    if l==[]:
        return 0
    if len(l)==1:
        return l[0]
    m = len(l)//2
    return sumaR(l[:m])+sumaR(l[m:])

(a) Time complexity
===================
T(0) = 1
T(1) = 1
T(n) = 2 * T(n/2) + 1 = 2 * [ 2 * T(n/4) + 1 ] + 1 = 2^2 * T(n/4) + 2^1 + 1
                                                   = 2^k * T(n/2^k) + 2^(k-1) + ... + 1
                                                   = 2^k + 2^(k-1) + ... + 1 (where 2^k is n)
                                                   = n => O(n), linear algorithm
(a) Extra-space complexity
===================                                                   
T(0) = 1
T(1) = 1
T(n) = 2 * T(n/2) + n (from the l[:m] ...) 
     = at each step we allocate memory for 'n' items (length of list)
     = we split the list into halves as many times as possible (log_2(n))
     -> extra space required n * log_2(n)

6. Binary search
================
T(1) = 1
T(n) = T(n/2) + 1 = T(n/4) + 1 + 1 = 
                  = T(n/2^k) + k = 1 + log_2(n)
'''
from texttable import Texttable
import random
import time

'''
bubble sort
cocktail sort
insert sort
merge sort
'''


def better_bubble_sort(data):
    flag = False
    j = 1
    while not flag:
        flag = True
        for i in range(len(data) - j):
            if data[i] > data[i + 1]:
                # TODO Start the outer for loop from the place of first change
                data[i], data[i + 1] = data[i + 1], data[i]
                flag = False
        j += 1


def bubblesort(data):
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data


def insertion_sort(array):
    for i in range(1, len(array)):
        element = array[i]
        j = i - 1
        while j >= 0 and element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element


def merge_sort(a, l_index, r_index):
    if l_index >= r_index:
        return

    m = (l_index + r_index) // 2
    merge_sort(a, l_index, m)
    merge_sort(a, m + 1, r_index)
    merge(a, l_index, r_index, m)


def merge(a, l_index, r_index, m):
    l_copy = a[l_index:m + 1]
    r_copy = a[m + 1:r_index + 1]

    l_copy_index = 0
    r_copy_index = 0
    sorted_index = l_index

    while l_copy_index < len(l_copy) and r_copy_index < len(r_copy):
        if l_copy[l_copy_index] <= r_copy[r_copy_index]:
            a[sorted_index] = l_copy[l_copy_index]
            l_copy_index = l_copy_index + 1
        else:
            a[sorted_index] = r_copy[r_copy_index]
            r_copy_index = r_copy_index + 1
        sorted_index = sorted_index + 1

    while l_copy_index < len(l_copy):
        a[sorted_index] = l_copy[l_copy_index]
        l_copy_index = l_copy_index + 1
        sorted_index = sorted_index + 1

    while r_copy_index < len(r_copy):
        a[sorted_index] = r_copy[r_copy_index]
        r_copy_index = r_copy_index + 1
        sorted_index = sorted_index + 1


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        start = start + 1


def best_case(n):
    """
    Best case list of n elements
    """
    return list(range(n))


def worst_case(n):
    """
    Best case list of n elements
    """
    data = best_case(n)
    data.reverse()
    return data


def avg_case(n):
    data = best_case(n)
    random.shuffle(data)
    return data


t = Texttable()
t.header(['size', 'bubbles', 'cocktail', 'insert', 'merge', 'timsort'])
for size in range(1000, 5001, 1000):
    data = avg_case(size)

    cdata = data[:]
    t1 = time.perf_counter()
    better_bubble_sort(cdata)
    t2 = time.perf_counter()
    bubble_time = t2 - t1

    cdata = data[:]
    t2 = time.perf_counter()
    insertion_sort(cdata)
    t3 = time.perf_counter()
    insert_time = t3 - t2

    cdata = data[:]
    t3 = time.perf_counter()
    merge_sort(cdata, 0, len(cdata) - 1)
    t4 = time.perf_counter()
    merge_time = t4 - t3

    cdata = data[:]
    t4 = time.perf_counter()
    cocktailSort(cdata)
    t5 = time.perf_counter()
    cocktail_time = t5 - t4

    cdata = data[:]
    t5 = time.perf_counter()
    cdata.sort()
    t6 = time.perf_counter()
    timsort_time = t6 - t5

    t.add_row([str(size), bubble_time, cocktail_time, insert_time, merge_time, timsort_time])

print(t.draw())
