
class LastBoardConfig:

    def __init__(self, file_name='D:/GitHubRepo/Assignments/a11-RazvanLazar9/persistence/last_board.config'):
        self._file_name = file_name
        self._last_board_config = self._load()

    def _load(self):
        f = open(self._file_name, 'rt')
        lines = f.readlines()
        f.close()
        dictionary = {}
        for line in lines:
            line = line.split('=')
            key = line[0].strip()
            params = line[1].strip()
            params = params.split(' ', 1)
            dictionary[key] = {'position': params[0].strip(), 'orientation': params[1].strip()}
        return dictionary

    def _write(self):
        with open(self._file_name, 'wt') as f:
            for (key, value) in self._last_board_config.items():
                line = str(key) + ' = ' + value['position'] + ' ' + value['orientation'] + '\n'
                f.write(line)

    def get_position(self, ship_type: str):
        return self._last_board_config[ship_type]['position']

    def get_orientation(self, ship_type: str):
        return self._last_board_config[ship_type]['orientation']

    def set_config(self, config):
        for key, value in config.items():
            self._last_board_config[key] = value
        self._write()
