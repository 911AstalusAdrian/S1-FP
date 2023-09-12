
class PlaceStatistics:

    def __init__(self, abs_path='D:/GitHubRepo/Assignments/a11-RazvanLazar9/statistics'):
        self.__abs_path = abs_path

    def write_to_file(self, file, result):
        file_name = self.__abs_path + '/' + file + '.txt'

        with open(file_name, 'at') as f:
            f.write(result + '\n')

    def clear_file(self, file):
        file_name = self.__abs_path + '/' + file + '.txt'
        with open(file_name, 'wt') as f:
            f.write('')
