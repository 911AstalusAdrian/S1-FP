def factor_product(n):
    p = 1
    if n % 2 == 0:
        p = p*2
        while n % 2 == 0:
            n //= 2
    for index in range(3, n+1):
        if n % index == 0:
            p = p*index
            while n % index == 0:
                n //= index

    return p

str_var = input("Give a natural number: ")
var = int(str_var)
print(factor_product(var))
