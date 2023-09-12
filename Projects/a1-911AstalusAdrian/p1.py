def is_prime(var):
    for index in range(2, var):
        if var % index == 0:
            return 0
            break
    return 1


def larger_prime(var):
    i = var+1
    while is_prime(i) == 0:
        i += 1
    return i


n = input("Give a natural number n: ")
int_n = int(n)
print(larger_prime(int_n))
