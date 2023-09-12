"""
Computational complexity
    O(n)

    1. asymptotic analysis (comp. complexity)
    2. empirical analysis
"""

'''
1
--------------------
found ← false
for i ← 1, n do
    if 𝑥𝑖 =𝑎 then
        found ← true
    endif
endfor

n - size of the input (e.g. length of a list, index of a term in Fib, row * count in a matrix etc)
T(n) - number of operations
    -> to keep it simple, each operation = 1 (takes up 1 amount of time)

O(1) - constant time

expected execution time
O(1) < O(log_n) < O(n^2) < O(n^3) < ... < O(2^n) < O(n^n)
O(1) is constant time
    - 1 ns is constant time
    - 1 week is constant time

Complexity is liniar (f(n) = n), and WC == AC == BC
WC(A) n steps, O(n) is in "n"
T(n) = ? 

2
----------------
found ← false
while found = fals do
    if 𝑥𝑖 =𝑎 then 
        found ← true
    i += 1
    endif 
endwhile

n - size of the input (length of iterable x ?)
BC(n) => T(n) = 1 (constant time)
WC(n) => T(n) = n (linear run time)

AC(n) = ???
we assumed that 
    1. item is in the list
    2. equal probability of it being at each index

AC(n) = (1 + 2 + ... + n) / n => n / 2 => T(n) = n / 2 => O(n) is still 'n' 

4
------------------
def f2(l): 
    sum = 0
    for el in l:
        j = len(l)
        while j>1:
            sum+=el*j
            j=j//3
    return sum

what represents the size of the algorithm's input? 
l - Python iterable => input size depends on len(l) ==> length of the iterable

outermost loop - n steps
innermost loop - log_3(n) => n * log_3(n) steps


5
---------------------
def sumaR(l): 
    if l==[]:
        return 0
    if len(l)==1:
        return l[0]
    m = len(l)//2
    return sumaR(l[:m]) + sumaR(l[m:])

(a) Time complexity
===================
We denote lines 77 - 81 as a sinlge operation (assume it takes time 1)
Line 82 ?

T(0) = 1
T(1) = 1 
T(n) = 2 * T(n/2) + 1 = 2 * [ 2 * T(n/4) + 1 ] + 1
                      = 2^2 * T(n/2^2) + 2^1 + 2^0
                      = ...
                      = 2^k * T(n/2^k) + 2^(k-1) + 2^(k-2) + ... + 2^0
                      we reach basic case when n ~ 2^k
                      = n * T(n/n) + n (last part of sum is a geometric series with base 2, ending in k-1)
                      = 2 * n, T(n) is a linear algorithm

(a) Extra-space complexity (space == memory)
============================================
T(0) = 1 (constant memory consumption)
T(1) = 1
T(n) = 2 * T(n/2) + n (from the l[:m] ...) 
     = at each step we allocate memory for 'n' items (length of list)
     = we split the list into halves as many times as possible (log_2(n))
     -> extra space required n * log_2(n)
                      
6. Binary search
================
(a) Time complexity
-------------------
T(1) = 1
T(n) = T(n/2) + 1 = T(n/4) + 1 + 1 = ... = (everytime we recurse, we increase operation count by 1) 
                                         = 1 + 1 + ... + 1 -> log_2(n) time (the number of times we can divide n into halves) 

(a) Extra-space complexity
--------------------------
T(1) = 1
T(n) = T(n/2) + 1 (1 stands for local variables allocated)
'''

from texttable import Texttable
import random
import time


def best_case(n):
    return list(range(n))


def worst_case(n):
    return best_case().reverse()


def avg_case(n):
    l = best_case(n)
    random.shuffle(l)
    return l


'''
Sorting algorithms be here
'''


def bubble_sort_op(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def insertion_sort(l):
    for i in range(1, len(l)):

        pos = l[i]
        j = i - 1
        while j >= 0 and pos < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = pos


def merge_sort(v):
    if len(v) > 1:
        middle = len(v) // 2
        left = v[:middle]
        right = v[middle:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                v[k] = left[i]
                i += 1
            else:
                v[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            v[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            v[k] = right[j]
            j += 1
            k += 1


"""
bubble sort, insert sort are O(n^2) algorithms
merge sort is an O(n * log_2(n)) algorithm
tim sort is python's inbuilt sort -> adaptive algorithm
"""

t = Texttable()

t.header(['', 'bubble sort', 'bubble sort opt', 'insert sort', 'merge sort','tim sort'])
# TODO Eliminate list copy time from the benchmark
for length in range(1000, 8001, 1000):
    data = avg_case(length)
    t1 = time.perf_counter()
    bubble_sort_op(data[:])
    t2 = time.perf_counter()
    insertion_sort(data[:])
    t3 = time.perf_counter()
    merge_sort(data[:])
    t4 = time.perf_counter()
    data[:].sort()
    t5 = time.perf_counter()
    t.add_row([str(length), '', t2 - t1, t3 - t2, t4 - t3, t5-t4])

print(t.draw())
