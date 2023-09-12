"""
Computational complexity

1.
-------------
found ← false
for i ← 1, n do
    if 𝑥! =𝑎 then
        found ← true
    endif
endfor

Keep in mind:
What determines the size of the input data?
    n - size of the input
Operations inside the for loop
    independent from n, so we assign it an execution time of 1 (runs in constant time)

T(n) - number of operations carried out (depends on n, usually)
T(n) = n * 1 (for loop runs n times, nested block runs in constant time)
T(n) belongs to O(n)

2.
-------------
found ← false
while found = false and i < len(x) do # n = len(x)
    if 𝑥𝑖 =𝑎 then # x is a finite iterable
        found ← true
    i += 1
    endif
endwhile

BC/WC/AC:

BC: T(n) = 1 (we find the element on the first position => list length is of no consequence)
WC: T(n) = n (like example 1.)

AC: T(n) = ??? (we have to assume where the searched for element is)
    We have to make some assumptions:
        1. searched for element is in the list
        2. same probability of it being found at any index
    T(n) = (1 + 2 + ... + n) / n ~ n/2 => O(n) (n/2 + 1/2 - 50% chance of the element being in the first half)

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

n - len(l)
T(n) = n * log_3(n)

5
---------------------
def sumaR(l):
    if l==[]:
        return 0
    if len(l)==1:
        return l[0]
    m = len(l)//2
    return sumaR(l[:m]) + sumaR(l[m:]) # data[1:] - all elements except the first one

(a) Time complexity
-------------------
T(n) = 1, n <= 1
T(n) = 2 * T(n/2) + 1, n > 1

T(n) = 2 * T(n/2) + 1 = 2 * [ 2 * T(n/4) + 1] + 1 = 2^2 * T(n/4) + 2 + 1
                                                  = 2^2 * [ 2 * T(n/8) + 1 ] + 2 + 1
                                                  = 2^3 * T(n/8) + 2^2 + 2^1 + 2^0

                                                  we have k, so that 2^k = n ( k = log_2(n) )
                                                  = 2^k * T(n/2^k) + 2^(k-1) + ... + 2^0
                                                  = n * 1 + n - 1 = 2 * n  => T(n) is a O(n) algorithm

(b) Extra-space complexity
--------------------------
T(n) = 1, n <= 1
T(n) = 2 * T(n/2) + 2 * n/2, n > 1

T(n) = 2 * T(n/2) + n = 2 * [ 2 * T(n/4) + n/2] + n = 2^2 * T(n/4) + n + n
                                                    = 2^3 * T(n/8) + n + n + n
                                                    we have k, so that 2^k = n ( k = log_2(n) )
                                                    = n * 1 + k * n
                                                    = n + n * log_2(n), T(n) is an O( n * log_2(n) )

Binary search
-------------
T(n) = 1, basic case
T(n) = T(n/2) + 1 = T(n/4) + 1 + 1 = T(n/8) + 1 + 1 + 1
                                    2^ k = n
                                   = T(n/2^k) + k * 1
                                   = 1 + log_2(n), bin. search is an O( log_2(n) ) algorithm
"""
import random
import time

from texttable import Texttable


def best_case(n):
    return list(range(n))


def worst_case(n):
    return best_case().reverse()


def avg_case(n):
    l = best_case(n)
    random.shuffle(l)
    return l


'''
bubble sort
cocktail sort 
insert sort
binary insertion sort
merge sort
quicksort
'''


def cocktail_sort(a_list):
    length = len(a_list)
    swapped = True
    start = 0
    end = length - 1

    while swapped is True:
        swapped = False

        for index in range(start, end):
            if a_list[index] > a_list[index + 1]:
                a_list[index], a_list[index + 1] = a_list[index + 1], a_list[index]
                swapped = True

        if swapped is False:
            break

        swapped = False

        end = end - 1

        for index in range(end - 1, start - 1, -1):
            if a_list[index] > a_list[index + 1]:
                a_list[index], a_list[index + 1] = a_list[index + 1], a_list[index]
                swapped = True

        start = start + 1


def quicksort(a, x, y):
    i = x
    j = y
    pivot = a[(x + y) // 2]
    while i <= j:
        while i < y and a[i] < pivot:
            i += 1
        while j > x and a[j] > pivot:
            j -= 1

        if i <= j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i += 1
            j -= 1

    if x < j:
        quicksort(a, x, j)
    if i < y:
        quicksort(a, i, y)


def quick_sort(a):
    quicksort(a, 0, len(a) - 1)


def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key


def bubble_sort(a_list):
    sw = 1
    while sw == 1:
        sw = 0
        for i in range(0, len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                sw = 1
                aux = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = aux


def merge_sort(given_list):
    if len(given_list) > 1:
        mid = len(given_list) // 2
        left = given_list[:mid]
        right = given_list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                given_list[k] = left[i]
                i += 1
            else:
                given_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            given_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            given_list[k] = right[j]
            j += 1
            k += 1


# sort
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = binary_search(arr, temp, 0, i) + 1
        for k in range(i, pos, -1):
            arr[k] = arr[k - 1]
        arr[pos] = temp


def binary_search(arr, key, start, end):
    # key
    if end - start <= 1:
        if key < arr[start]:
            return start - 1
        else:
            return start
    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid)
    else:
        return mid


t = Texttable()
t.header(['size', 'bubbles', 'cocktail', 'insert', 'binary insert', 'merge', 'quicksort', 'timsort'])
for size in range(1000, 5001, 1000):
    data = best_case(size)

    '''
    Bubble sort
    '''
    cdata = data[:]
    t1 = time.perf_counter()
    bubble_sort(cdata)
    t2 = time.perf_counter()
    bubble_time = t2 - t1

    '''
    Insert sort
    '''
    cdata = data[:]
    t2 = time.perf_counter()
    insert_sort(cdata)
    t3 = time.perf_counter()
    insert_time = t3 - t2

    '''
    Merge sort
    '''
    cdata = data[:]
    t3 = time.perf_counter()
    merge_sort(cdata)
    t4 = time.perf_counter()
    merge_time = t4 - t3

    '''
    Cocktail sort
    '''
    cdata = data[:]
    t4 = time.perf_counter()
    cocktail_sort(cdata)
    t5 = time.perf_counter()
    cocktail_time = t5 - t4

    '''
    Timsort
    '''
    cdata = data[:]
    t5 = time.perf_counter()
    cdata.sort()
    t6 = time.perf_counter()
    timsort_time = t6 - t5

    '''
    Binary insertion sort
    '''
    cdata = data[:]
    t6 = time.perf_counter()
    binary_insertion_sort(cdata)
    t7 = time.perf_counter()
    binary_insert_time = t7 - t6

    '''
    Quicksort
    '''
    cdata = data[:]
    t7 = time.perf_counter()
    quick_sort(cdata)
    t8 = time.perf_counter()
    quick_sort_time = t8 - t7

    t.add_row([str(size), bubble_time, cocktail_time, insert_time, binary_insert_time, merge_time, quick_sort_time,
               timsort_time])

print(t.draw())
