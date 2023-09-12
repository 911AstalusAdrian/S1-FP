def divisor_sum(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    return s


def is_perfect(n):
    div_sum = divisor_sum(n)
    if div_sum == n:
        return 1
    else:
        return 0


def smaller_perfect(n):
    p = -1
    for i in range(n-1, 0, -1):
        if is_perfect(i):
            p = i
            break
    return p



str_var = input("Give number: ")
var = int(str_var)
perf = smaller_perfect(var)
if perf == -1:
    print("There is no smaller perfect number")
else:
    print(perf)
