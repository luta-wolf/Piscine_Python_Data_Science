class Research:
    @staticmethod
    def file_reader() -> str:
        with open("data.csv", "r") as in_file:
            return in_file.read()


if __name__ == '__main__':
    try:
        print(Research.file_reader())
    except IOError as e:
        print(e)
