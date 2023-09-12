"""
Class rational
"""


class rational:
    """
    This is the rational data type
    Data type = domain + operations
        domain - means the set of attributes and possible values
        operations - means methods
    """

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = value

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError('rational cannot have 0 denominator')
        self.__denominator = value


q = rational()
q.new_attribute = 10

print(rational.__dict__)  # -> the data type (say integer)
print(q.__dict__)  # -> a value (say 5)

'''
{'__module__': '__main__',
 '__doc__': '\n    This is the rational data type\n    Data type = domain + operations\n        domain - means the set of attributes and possible values\n        operations - means methods\n    ',
 '__init__': <function rational.__init__ at 0x10931e550>,
 'numerator': <property object at 0x109333090>,
 'denominator': <property object at 0x109325d60>,
 '__dict__': <attribute '__dict__' of 'rational' objects>, '__weakref__': <attribute '__weakref__' of 'rational' objects>
}


{'_rational__numerator': 0, '_rational__denominator': 1, 'new_attribute': 10}
'''

'''
attribute -> variable
method    -> function
property  -> variable that you access/modify using a function
'''

'''
V1 
    + looks nice
    - breaks encapsulation (you can set invalid values here)
'''
# q1.numerator += 1


'''
V2
    - not so nice
    + works ok
'''
# q1.set_numerator(q1.get_numerator() + 1)


'''
V3 - Python properties 
    + nice to look at
    + works correctly
'''
# ????

# q1.numerator += 1


# print(q1.get_numerator())

# q1.get_numerator() <==> rational.get_numerator(q1)


# q1.denominator = 0
# Just because you can, doesn't mean ...
# q1.__denominator = 0


# print(q1)

#
# q2 = rational()
#
# print(q1)
# print(q1.numerator)
# print(q1.denominator)
