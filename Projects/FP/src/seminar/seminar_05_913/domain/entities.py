class Cat:
    # common to all cats
    _count = 0

    def __init__(self, id_, name, breed, age, is_vaccinated):
        # These don't change -> read-only attributes
        self._id = id_
        self._name = name
        self._breed = breed
        # These below might change -> read/write attributes
        self._age = age
        self._is_vaccinated = is_vaccinated
        Cat._count += 1

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def vaccinated(self):
        return self._is_vaccinated

    @vaccinated.setter
    def vaccinated(self, other):
        self._is_vaccinated = other

    def __add__(self, other):
        # return cat(self.name, self.breed, self.age + other, self._is_vaccinated)
        self.age += other
        return self

    @staticmethod
    def cat_count():
        return Cat._count

    def __eq__(self, other):
        # only compare cats to other cats
        if isinstance(other, Cat) == False:
            raise TypeError('Cannot compare cats to non-cats')
        return self.id == other.id


class Stay:
    def __init__(self, cat_, arrival, departure=None):
        self._cat = cat_
        self._arrival = arrival
        self._departure = departure

    @property
    def cat(self):
        return self._cat

    @property
    def arrival(self):
        return self._arrival

    @property
    def departure(self):
        return self._departure


if __name__ == '__main__':
    c1 = Cat(100, 'Tabby', 'domestic short-hair', 8, False)
    c2 = Cat(101, 'Garfield', 'domestic short-hair', 8, False)

    print(c1.name)

    # c.age = c.age + 1 -> c.age getter and setter both called

    c1 + 1 + 1 + 1 + 1  # make the cat older by one year

    c1.age += 1
    print(c1.age)

    print(Cat.cat_count())
