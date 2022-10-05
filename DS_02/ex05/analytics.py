import os
from random import randint


class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self, has_header=True):
        if self.path_checker():
            with open(self.file_path, "r") as in_file:
                content = in_file.read()
                lines = content.split('\n')
                if len(lines) < 1:
                    raise ValueError("Error: The file is empty")
                if lines[0] == '0,1' or lines[0] == '1,0':
                    has_header = False

                if has_header and len(lines) < 2:
                    raise ValueError("Error: The file with header has no enough lines")
                if has_header and len(lines[0].split(',')) != 2:
                    raise ValueError("Error: The file has a different structure in header")
                if has_header:
                    content_lines = lines[1:]
                else:
                    content_lines = lines
                for line in content_lines:
                    if line != '0,1' and line != '1,0':
                        raise ValueError("Error: Incorrect file structure in content")
                content_list = [[int(value) for value in line.split(',')] for line in content_lines]

                return content_list

    def path_checker(self):
        if not os.path.exists(self.file_path):
            raise OSError("Error: File not found")
        if not os.path.isfile(self.file_path):
            raise OSError("Error: The specified path is not a file")
        if not self.file_path.endswith('.csv'):
            raise OSError("Error: Incorrect file extension")
        if not os.access(self.file_path, os.R_OK):
            raise OSError("Error: Can't read file")
        return True

    class Calculations:

        def __init__(self, data):
            self.data = data
            self.count = self.counts()

        def counts(self):
            heads = 0
            tails = 0
            for elem in self.data:
                heads += elem[0]
                tails += elem[1]
            result = [heads, tails]
            return result

        def fractions(self):
            sum_all = self.count[0] + self.count[1]
            result = [(self.count[0] / sum_all) * 100, (self.count[1] / sum_all) * 100]
            return result

    class Analytics(Calculations):
        def predict_random(self, predict_number):
            dictionary = {0: [0, 1], 1: [1, 0]}
            return [dictionary[randint(0, 1)] for num in range(predict_number)]

        def predict_last(self) -> list:
            return self.data[-1]

        def save_file(self, data, out_file, extension):
            with open(f'{out_file}.{extension}', 'w') as file:
                file.write(data)
