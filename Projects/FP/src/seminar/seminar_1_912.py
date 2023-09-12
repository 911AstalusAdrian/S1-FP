'''
1. Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
	Question – What happens if we enter a non-integer number, or alphanumeric characters?
'''


def is_10(number_1, number_2):
    if number_1 == 10 or number_2 == 10 or number_1 + number_2 == 10:
        return True
    else:
        return False

n1 = 9
n2 = 1
# print(is_10(n1, n2))



# Example for var type
# None is like null, nullptr, but better behaved
var = None


# C
# int c, b;
# ...
# c = b // The value of var b is copied into variable c

# Python
# c = b
# 1. The type of c is changed to the type of b
# 2. Tha value of b is 'copied' to variable c


# s = input("Do you want an integer? ")
# if "yes" == s:
#     var = 1
# else:
#     var = '1'

# 'class' is basically a fancy way of saying type
# <class 'int'> means it's an integer
# print(type(var))

'''
3. Given a non-empty string like "Code" return a string like "CCoCodCode"
stringSplosion('Code') → 'CCoCodCode'
stringSplosion('abc') → 'aababc'
stringSplosion('ab') → 'aab'
'''
def stringSplosion(string):
    """
    Format the string explosion
    :type string: str
    """
    result = ''

    # range - Left is inclusive, but right bound is exclusive
    # Like in C - the 4th letter has index 3

    for length in range(1, len(string)+1):
        result += string[0:length]
        # A string slice starting from the beginning and up to length chars
    return result

print(stringSplosion('StringSplosion'))

'''
What we've learned:
    Python:
        Do variables have type in Python?
            YES => Python is a typed language
        When is a variable type assigned?
            DYNAMIC - when running program (interpreter, runtime env)
            STATIC - when writing program (compiler)
            
            Python is a dynamically typed language
                

    Python types we know of:
        int - integer type, str - string type

'''