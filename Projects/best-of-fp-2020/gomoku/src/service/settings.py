class Settings:
    def __init__(self):
        self._dict = {}

    def parse(self, text_file):
        """
        Parses the information from a text file
        :param text_file: the name of the text file
        """
        f = open(text_file)
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split('=')
            self._dict[line[0].strip()] = line[1].strip()

    def get(self, key):
        """
        Returns the value at the given key, if the key exists
        :param key: the given key
        :return: the value at that key or None if the key does not exist
        """
        if key not in self._dict:
            return None

        return self._dict[key]

    def __getitem__(self, item):
        return self.get(item)
