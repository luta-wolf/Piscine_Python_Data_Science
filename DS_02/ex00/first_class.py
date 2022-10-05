class Must_read:
    try:
        with open("data.csv", "r") as in_file:
            print(in_file.read())
    except IOError as e:
        print(e)


if __name__ == '__main__':
    Must_read()
