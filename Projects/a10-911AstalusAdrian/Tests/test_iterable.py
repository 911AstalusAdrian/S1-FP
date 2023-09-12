import unittest
from Repositories.Iterable import Iterable, non_iterable_shell_sort


class TestIterable(unittest.TestCase):
    def setUp(self):
        self._iterable = Iterable()
        self._iterable.append("Dog")
        self._iterable.append("Cat")
        self._iterable.append("Horse")
        self._iterable.append("Cow")

    def test_length(self):
        iterable_length = len(self._iterable)
        self.assertEqual(iterable_length, 4)

    def test_get(self):
        get_item = self._iterable[2]
        self.assertEqual(get_item, "Horse")

    def test_set(self):
        self._iterable[3] = 'Unicorn'
        get_item = self._iterable[3]
        self.assertEqual(get_item, 'Unicorn')

    def test_delete(self):
        del self._iterable[3]
        self.assertEqual(len(self._iterable), 3)

    def test_iter(self):
        iteration = iter(self._iterable)
        self.assertEqual(next(iteration), 'Dog')
        self.assertEqual(next(iteration), 'Cat')
        self.assertEqual(next(iteration), 'Horse')
        self.assertEqual(next(iteration), 'Cow')

    def test_filter(self):
        filtered_list = self._iterable.filter(lambda item: item == 'Dog')
        self.assertEqual(len(filtered_list), 1)
        self.assertEqual(filtered_list[0], 'Dog')

    def test_sort(self):
        sorted_list = self._iterable.shell_sort(lambda a, b: a < b)
        self.assertEqual(len(sorted_list), 4)
        self.assertEqual(sorted_list[0], 'Horse')
        self.assertEqual(sorted_list[1], 'Dog')
        self.assertEqual(sorted_list[2], 'Cow')
        self.assertEqual(sorted_list[3], 'Cat')

    def test_non_iterable_shell_sort(self):
        random_list = ['Mike', 'Jane', 'Alexander', 'Zack']
        sorted_list = non_iterable_shell_sort(random_list, lambda a, b: a > b)
        self.assertEqual(sorted_list[0], 'Alexander')
        self.assertEqual(sorted_list[1], 'Jane')
        self.assertEqual(sorted_list[2], 'Mike')
        self.assertEqual(sorted_list[3], 'Zack')

