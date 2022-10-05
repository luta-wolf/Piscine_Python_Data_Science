import os
import sys


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
        def counts(data):
            heads = 0
            tails = 0
            for elem in data:
                heads += elem[0]
                tails += elem[1]
            result = [heads, tails]
            return result

        def fractions(counts):
            sum_all = counts[0] + counts[1]
            result = [(counts[0] / sum_all) * 100, (counts[1] / sum_all) * 100]
            return result


def error(path, message):
    print("{0}: {1} ".format(path, message))
    sys.exit(1)


def main(file_path):
    try:
        research = Research(file_path)
        list_data = research.file_reader()
        print(list_data)
        counts = research.Calculations.counts(list_data)
        fractions = research.Calculations.fractions(counts)
        print(counts[0], counts[1])
        print(fractions[0], fractions[1])
    except (IOError, OSError, ValueError) as e:
        print(e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        error("Error", "Incorrect number of arguments entered")
    main(sys.argv[1])
