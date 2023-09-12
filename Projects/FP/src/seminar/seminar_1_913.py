# print("Hello there 913!")

'''
3. Given a non-empty string like "Code" return a string like "CCoCodCode"
stringSplosion('Code') → 'CCoCodCode'
stringSplosion('abc') → 'aababc'
stringSplosion('ab') → 'aab'
'''
def stringSplosion(word):
    result = []
    for index in range(1,len(word)+1):
        # slice starts at 0, ends at index
        result += word[0:index]
        # print(  word[0:index]  ) # when indexing, right value is excluded
    return result

py_list = [111, [2222,333,444], 3333, 44444, 55, 234326]
print(py_list[0:3])



# print(stringSplosion('123'))
print(stringSplosion(py_list))
#
# print([] + "123")

'''
char* stringSplosion(char* word) {
    char result[100];
    ...
    
    return result;
}


Python is a dynamically typed language = all vars have a data type
Typed languages
    - static  = Exact type information is available during compile
    - dynamic = Types are decided during runtime 

'''


# print(type('1')) # <class 'str'> - type string
# print(type(1)) # <class 'int'> - int type



# print(stringSplosion('StringSplosion'))


