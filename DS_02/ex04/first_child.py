import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path
    def file_reader(self):
        has_header = True
        text = self.check_file(has_header)
        print(1)
        return text

    def check_file(self, has_header):
        with open(self.path, "r") as f:
            lines = [line.rstrip() for line in f]
        if (len(lines) < 1):
            raise ValueError("Size of the file is too small")
        if lines[0] == "0,1" or lines[0] == "1,0":
            has_header = False
        if has_header and len(lines[0].split(',')) != 2:
            raise ValueError("Header is incorrect")
        mod_lines = []
        if has_header:
            mod_lines = lines[1:]
        else:
             mod_lines = lines
        for line in mod_lines:
            if line != "0,1" and line != "1,0":
                raise ValueError("Data in the file is incorrect")
        res = []
        for line in mod_lines:
            strs = line.split(',')
            numbers = []
            for number in strs:
                numbers.append(int(number))
            res.append(list(numbers))
        return res

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = 0
            tails = 0
            for pair in self.data:
                heads += pair[0]
                tails += pair[1]
            return heads, tails

        def fractions(self, heads, tails):
            first = heads * 100 / (heads + tails)
            second = tails * 100 / (heads + tails)
            return first, second

    class Analytics(Calculations):
        def predict_random(self, num):
            res = []
            for i in range(num):
                first = randint(0, 1)
                second = 0 if first else 1
                res.append([first, second])
            return res

        def predict_last(self, res):
            return res[-1]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("No input file")
    outter = Research(sys.argv[1])
    print(outter.file_reader())
    inner = outter.Calculations(outter.file_reader())
    calc = inner.counts()
    print(calc[0], calc[1])
    frac = inner.fractions(calc[0], calc[1])
    print(frac[0], frac[1])
    inherited = outter.Analytics(outter.file_reader())
    rand_nums = inherited.predict_random(3)
    print(rand_nums)
    print(inherited.predict_last(rand_nums))
