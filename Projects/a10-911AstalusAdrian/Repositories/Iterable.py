class Iterable:
    def __init__(self):
        self._iterable_data = []

    def __len__(self):
        return len(self._iterable_data)

    def __getitem__(self, item):
        return self._iterable_data[item]

    def __setitem__(self, key, value):
        self._iterable_data[key] = value

    def __delitem__(self, key):
        del self._iterable_data[key]

    def __iter__(self):
        self._index = 0
        while True:
            try:
                yield self._iterable_data[self._index]
                self._index += 1
            except IndexError:
                break

    def append(self, item):
        self._iterable_data.append(item)

    def filter(self, acceptance_function):
        filtered_list = []
        for item in self._iterable_data:
            if acceptance_function(item):
                filtered_list.append(item)
        return filtered_list

    def shell_sort(self, comparison_function):
        """
        We sort a given list using Shell Sort, based on a comparison function
        :param self: The list to be sorted
        :param comparison_function: Comparison function based on which we sort the list
        :return: The sorted list
        """
        interval = len(self) // 2
        while interval > 0:
            for index in range(interval, len(self)):
                temporary_value = self[index]
                j = index
                while j >= interval and comparison_function(self[j - interval], temporary_value):
                    self[j] = self[j - interval]
                    j -= interval
                self[j] = temporary_value
            interval //= 2
        return self


def non_iterable_shell_sort(given_list, comparison_function):
    """
    We sort a given list using Shell Sort, based on a comparison function
    :param given_list: The list to be sorted
    :param comparison_function: Comparison function based on which we sort the list
    :return: The sorted list
    """
    interval = len(given_list) // 2
    while interval > 0:
        for index in range(interval, len(given_list)):
            temporary_value = given_list[index]
            j = index
            while j >= interval and comparison_function(given_list[j - interval], temporary_value):
                given_list[j] = given_list[j - interval]
                j -= interval
            given_list[j] = temporary_value
        interval //= 2
    return given_list
