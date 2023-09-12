"""
    Service class includes functionalities for implementing program features
"""
from random import randint

from domain.entity import ComplexNumber


class NumberFunctions:

    def __init__(self):
        """
        We create our list of complex numbers, being empty at first
        """
        self.complex_numbers_list = []

    @property
    def complex_numbers_list(self):
        return self._complex_numbers_list

    @complex_numbers_list.setter
    def complex_numbers_list(self, new_list):
        self._complex_numbers_list = list(new_list)

    def add_complex(self, real_part, imaginary_part):
        """
        Function used to add a complex number to the list, knowing the real and the imaginary part
        We create the complex number, using the ComplexNumber class in entity
        We add this number to our list
        """
        number = ComplexNumber(real_part, imaginary_part)
        self.complex_numbers_list.append(number)

    def __len__(self):
        return len(self.complex_numbers_list)

    def initialise(self):
        """
        Function used for initialising the list with 10 random complex numbers
        We generate the real and the imaginary part with randint, then we add the numbers to the initial list
        """
        for index in range(10):
            real_part = randint(-20, 20)
            imaginary_part = randint(-20, 20)
            self.add_complex(real_part, imaginary_part)

    def filter_list(self, start, end):
        """
        We create a new list with the elements between the 'start' and 'end' index
        We replace the existent list with the new list
        'start' - The starting index
        'end' - The last index
        """
        new_list = []
        for index in range(start, end+1):
            new_list.append(self.complex_numbers_list[index])
        self.complex_numbers_list = new_list[:]


def test_add():
    """
    Test function for the addition of complex numbers
    """
    test = NumberFunctions()
    test.add_complex(10, 21)
    test.add_complex(12, 15)
    test.add_complex(1, 0)
    test.add_complex(0, 24)

    assert str(test._complex_numbers_list[0]) == '10+21i'
    assert test._complex_numbers_list[0].imaginary_part == 21
    assert test._complex_numbers_list[0].real_part == 10

    assert str(test._complex_numbers_list[1]) == '12+15i'
    assert test._complex_numbers_list[1].imaginary_part == 15
    assert test._complex_numbers_list[1].real_part == 12

    assert str(test._complex_numbers_list[2]) == '1'
    assert test._complex_numbers_list[2].imaginary_part == 0
    assert test._complex_numbers_list[2].real_part == 1

    assert str(test._complex_numbers_list[3]) == '24i'
    assert test._complex_numbers_list[3].imaginary_part == 24
    assert test._complex_numbers_list[3].real_part == 0


test_add()
