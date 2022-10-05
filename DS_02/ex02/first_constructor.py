import os
import sys


class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self) -> str:
        if self.path_checker():
            with open(self.file_path, "r") as in_file:
                content = in_file.read()
                lines = content.split('\n')
                if len(lines) < 2:
                    raise ValueError("Error: The file has a different structure: not enough lines")
                if lines[0] == '0,1' or lines[0] == '1,0' or len(lines[0].split(',')) != 2:
                    raise ValueError("Error: The file has a different structure in header")
                for line in lines[1:]:
                    if line != '0,1' and line != '1,0':
                        raise ValueError("Error: Incorrect file structure after header")
                return content

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


def error(path, message):
    print("{0}: {1} ".format(path, message))
    sys.exit(1)


def main(file_path):
    try:
        research = Research(file_path)
        print(research.file_reader())
    except (IOError, OSError, ValueError) as e:
        print(e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        error("Error", "Incorrect number of arguments entered")
    main(sys.argv[1])
