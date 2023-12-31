"""
Created on Jan 10, 2017

@author: Arthur
"""

import time
from texttable import *


def generate_test(array, DIM):
    if len(array) == DIM:
        # print (array)
        pass
    if len(array) > DIM:
        return
    array.append(0)
    for i in range(0, DIM):
        array[-1] = i
        generate_test(array[:], DIM)


def backtracking(array, DIM):
    if len(array) == DIM:
        print(array)
        pass
    if len(array) > DIM:
        return
    array.append(0)
    for i in range(0, DIM):
        array[-1] = i
        if len(set(array)) == len(array):
            backtracking(array, DIM)
            array.pop()


print(7**7)
print(8**8)




'''



'''

'''
And here we build our experiment
'''
# functions = [generate_test, backtracking]
# data_sizes = [3, 4, 5, 6, 7]
#
# t = Texttable()
# t.add_row(['Functions'] + data_sizes)
# for function in functions:
#     row = [function.__name__]
#     for size in data_sizes:
#         t1 = time.perf_counter()
#         function([], size)
#         t2 = time.perf_counter()
#         row = row + [t2 - t1]
#     t.add_row(row)
# print(t.draw())
