from Problem.iterative_backtracking import iterative
from Problem.recursive_backtracking import recursive

array = [1, 2, 3, 4, 5]
n = 9
subsets_1 = []
recursive(array, n, [], 0, subsets_1)
if len(subsets_1) == 0:
    print("There are no subsets")

print("\n--------------\n")


subsets = iterative(array, len(array), n)
if len(subsets) == 0:
    print("There are no subsets")
else:
    for subset in subsets:
        print(subset)