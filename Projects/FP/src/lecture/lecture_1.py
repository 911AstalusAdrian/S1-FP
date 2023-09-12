
# console input / output in Python
# Basic data types - str, int, list, dict, tuple
# control flow - for, while, if-elif-else
# some builtin functions - len, id, type

print('Hello everyone')
# value = input("Give me an integer: ")

# cast vs. conversion
# ValueError - type of the error (it's an exception)
int_value = None
# Catching the error
'''
try:
    # Scope of int_value is the current block of code
    # python block of code = indentation level
    int_value = int(value)
except ValueError:
    print("No bueno, not an integer!")
'''
# str, int - immutable
def f(val):
    val += 99


old_val = 42
f(old_val)
# print(old_val)

def f(my_list):
    list_a = [3,4,5]
    my_list = list_a
    # my_list = [] - we create a new list, scope (domeniu de vizibilitate) is local to the function
    my_list.append(55) # the same list, with a new element
    #my_list.clear()
    #print(id(my_list))
    return my_list

some_list = []
returned_list = f(some_list)
# print(returned_list)

#
# lst = [1,2,3]
# print(id(lst))
# f(lst)
#
# print(id(lst))
# print(lst)

# my_list is destryed, do the id 1 is available

# some more code

'''
1 + 2 = 3 
'1' + '2' = '12'
'1' + 2 = ????
'''
# print('The value just read is ' , int_value,45)

# List
data_1 = list()
data_2 = []

# ????
# range(2, 10) - returns numbers from 0 to 10 (exclusive)
for i in range(2, 10, 3): # for (int i = 2;i<10; i++)
    data_1.append(i)
print(data_1)

data_1.append('99')

# How do I uniquely identify something? - id() function
# The unique ID of the given parameter (object - everything in Py is an object)
# print('data_1',id(data_1),data_1)
# print('data_2',id(data_2),data_2)

# data_1 and data_3 are aliased (they reference the same list)
# data_3 = data_1
#
# data_3.append(999)
# print('data_1',id(data_1),data_1)
# print('data_3',id(data_3),data_3)

# data = list(range(1,20)) # convert to a list
# # how do I know what type data is ?
# print(type(data))
# print(data)
#
# # get the first 3 elements
# print(data[0:3]) # left inclusive, right exclusive
# # the last 3 elements
# print(data[-3:])
# # only the even numbers
# print(data[1::2]) # third param is the step
# # the last element
# print(data[-1])
# print(data[-2])

# Dictionaries (maps) - mapping between a unique key and a value
# keys - unique, values have no requirements
d = { 1 : "Mary", 2 : "Cathy", 3 :"John", 4 : [1,2,3] }
print(d)

# retrieve key for 4
print(d[4])
# retrieve the second element of the list in the dictionary
print(d[4][1])
# d - reference the dict
# d[4] - value that corresponds to key 4
# d[4][1] - second elements of the list

# Recap
# data types - int, str, list, dict
# functions - id, type, len (length of lisst, string), range
# for loop, if-elif-else

# Python is dynamically typed
# 1. rng takes the type of range(10)
# 2. rng takes the value from the right hand side
rng = range(10)