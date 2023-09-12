# print("Welcome group 911")

"""
What have we learned?
    - Python modules (files ending .py) can be run as they are (no main function, no classes)
    - Hello world helps me make sure the IDE is well configured
    - Indication that Python is a 'simple' language
"""



'''
1. How to write a Python function (def + name + paraneters)
2. Python uses code indentation to identify blocks
    - C/C++/Java ->  { } 
    - Pascal -> begin end
    - Python -> indentation
2. Pass ?
3. range - inbuilt function that generates values (left bound inclusive, right one is exclusive)
4. value[0:index] - slice between index 0 and the value of 'index' (left bound inclusive, right one is exclusive)
'''

'''
3. Given a non-empty string like "Code" return a string like "CCoCodCode"
stringSplosion('Code') → 'CCoCodCode'
stringSplosion('abc') → 'aababc'
stringSplosion('ab') → 'aab'
'''
def stringSplosion(value):
    # hint: strings in Python are immutable
    print(type(value))
    result = ''

    for index in range(len(value), 0, -1):
        # This creates a new str value at each step
        result = value[0:index] + result
    return result

# int c;

c = None
c = 100
c = '100'

'''
Hmmm ... dynamic typing?
    typed language - every variable has a type
    statically typed  - variable types are known at definition  
    dynamically typed - variable types are known at runtime
'''
# print(stringSplosion('12345'))
# print(stringSplosion(12345))


def add(a, b):
    return a + b

print(add('123','456')) # 123456 - concatenation
print(add(123,456))  # 579 - addition
# TypeError means the code has a problem with var types
# print(add(123,'456')) # ??

# Define a Python list:
lst = [] # empty list
lst = list() # same thing
print(add([1,2,3],[4,5,6]))

print([] + ['asd'])

# 1. Empty list is defined
# 2. append is called -> returns None
my_list = []
my_list.append('abc')
print(my_list)

'''
print - reference to a built-in function
x takes the type and value of print => x is an alias of the inbuilt function
() - function call operator
'''
x = print
x('abd')
print(type(x))



