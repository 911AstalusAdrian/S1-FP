from errors import RuleError


class Rules:
    """
    Possible rules:
        edge: the number of squares per line/column (10, 20, 25, 50)
        can_touch: if the ships can or can't touch at placement
        number of <ship>: more than 1, up to 5
        difficulty:
            0 - Beginner
            1 - Easy
            2 - Normal
            3 - Hard
    """

    def __init__(self, file_name='persistence/rules.config'):
        self._file_name = file_name
        self._rules = self._load()

    def _load(self):
        f = open(self._file_name, 'rt')
        lines = f.readlines()
        f.close()
        dictionary = {}
        for line in lines:
            line = line.split('=')
            dictionary[line[0].strip()] = line[1].strip('\n').strip()
        return dictionary

    def _write(self):
        with open(self._file_name, 'wt') as f:
            for (key, value) in self._rules.items():
                line = str(key) + ' = ' + ('False' if value is False else
                                           "True" if value is True else str(value)) + '\n'
                f.write(line)

    @property
    def edge(self):
        return 10               # int(self._rules['edge'])

    @property
    def can_touch(self):
        return True if self._rules['can_touch'].lower() == 'true' else False

    @property
    def number_of(self):
        number_of = {
            'destroyer':    1,  # int(self._rules['destroyers']),
            'submarine':    1,  # int(self._rules['submarines']),
            'cruiser':      1,  # int(self._rules['cruisers']),
            'battleship':   1,  # int(self._rules['battleships']),
            'carrier':      1   # nt(self._rules['carriers'])
        }
        return number_of

    @property
    def difficulty(self):
        return int(self._rules['difficulty'])

    @property
    def display_probability(self):
        return True if self._rules['display_probability'].lower() == 'true' else False

    @property
    def test(self):
        return True if self._rules['test'].lower() == 'true' else False

    @staticmethod
    def __check_validity(key, value):
        if key == 'can_touch':
            if value not in [True, False]:
                return 'Invalid ship touch rule!'
        if key == 'display_probability':
            if value not in [True, False]:
                return 'Invalid display probability rule!'
        if key == 'test':
            if value not in [True, False]:
                return 'Invalid test rule!'
        if key == 'edge':
            if value is True or False or value not in [10, 15, 20]:
                return 'Invalid edge size!'
        if key == 'destroyers':
            if value not in [1, 2, 3, 4, 5]:
                return 'Invalid number of destroyers!'
        if key == 'submarines':
            if value is True or False or value not in [1, 2, 3, 4, 5]:
                return 'Invalid number of submarines!'
        if key == 'cruisers':
            if value is True or False or value not in [1, 2, 3, 4, 5]:
                return 'Invalid number of cruisers!'
        if key == 'battleships':
            if value is True or False or value not in [1, 2, 3, 4, 5]:
                return 'Invalid number of battleships!'
        if key == 'carriers':
            if value is True or False or value not in [1, 2, 3, 4, 5]:
                return 'Invalid number of carriers!'
        if key == 'difficulty':
            if value is True or False or value not in [1, 2, 3, 4]:
                return 'Invalid difficulty level!'
        return ''

    def set_rules(self, **kwargs):
        """
        allowed keys:
            edge
            can_touch
            destroyers
            submarines
            cruisers
            battleships
            carriers
            difficulty
            display_probability
            test
        """
        error = ''
        for (key, value) in kwargs.items():
            if key not in self._rules:
                raise RuleError('Invalid key!')
            validity = self.__check_validity(key, value)
            if validity == '':
                self._rules[key] = value
            else:
                error += validity + '\n'
        if error != '':
            raise RuleError(error)
        self._write()
