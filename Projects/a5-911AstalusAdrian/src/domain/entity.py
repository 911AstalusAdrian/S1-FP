"""
    Entity class should be coded here
"""
'''
Manage a list of complex numbers in a+bi form and provide the user the following features:

    Add a number. The number is read from the console.
    Display the list of numbers.
    Filter the list so that it contains only the numbers between indices start and end, where these values are read from the console.
    Undo the last operation that modified program data. This step can be repeated.

'''


class ComplexNumber:
    """
    This is the complex data type
    Used for representing a complex number
    """

    def __init__(self, real_part=0, imaginary_part=0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    @property
    def real_part(self):
        return self._real_part

    @property
    def imaginary_part(self):
        return self._imaginary_part

    @real_part.setter
    def real_part(self, value):
        self._real_part = value

    @imaginary_part.setter
    def imaginary_part(self, value):
        self._imaginary_part = value

    def __str__(self):
        """
        Transforming our complex number into a string
        """
        if self._real_part == 0 and self._imaginary_part == 0:
            return str(self._real_part)
        elif self._real_part == 0:
            return str(self._imaginary_part) + 'i'
        else:
            if self._imaginary_part > 0:
                return str(self._real_part) + '+' + str(self._imaginary_part) + 'i'
            elif self._imaginary_part == 0:
                return str(self._real_part)
            else:
                return str(self._real_part) + str(self._imaginary_part) + 'i'


def complex_test():
    """
    Test function to see if different types of complex numbers are turned into strings correctly
    """
    number = ComplexNumber(-10, 0)
    assert number.real_part == -10
    assert number.imaginary_part == 0
    assert str(number) == '-10'

    number = ComplexNumber(0, 12)
    assert number.real_part == 0
    assert number.imaginary_part == 12
    assert str(number) == '12i'

    number = ComplexNumber(0, 0)
    assert number.real_part == 0
    assert number.imaginary_part == 0
    assert str(number) == '0'

    number = ComplexNumber(20, -7)
    assert number.real_part == 20
    assert number.imaginary_part == -7
    assert str(number) == '20-7i'


complex_test()
