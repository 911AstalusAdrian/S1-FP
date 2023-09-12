"""
The sequence a = a1, ..., an with distinct integer numbers is given.
Determine all subsets of elements having the sum divisible by a given n.
"""


def recursive(array, n, subset, index, subsets):
    if subset != [] and sum(subset) % n == 0:
        print(subset)
        subsets.append(subset)
    for i in range(index, len(array)):
        subset.append(array[i])
        recursive(array, n, subset, i+1, subsets)
        subset.pop(-1)


array = [1, 2, 3, 4, 5]
n = 6
subsets = []
recursive(array, n, [], 0, subsets)
if len(subsets) == 0:
    print("There are no subsets")
