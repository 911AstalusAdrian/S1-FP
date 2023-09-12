def iterative(array, len, value):
    partial_set = []
    for i in range(1<<len):
        sub = []
        for j in range(len):
            if(i & (1<<j) > 0):
                sub.append(array[j])

        if sum(sub) % value == 0 and sub != []:
            partial_set.append(sub)

    return partial_set


array = [1, 2, 3, 4, 5]
n = 6
subsets = iterative(array, len(array), n)
if len(subsets) == 0:
    print("There are no subsets")
else:
    print(subsets)
