#!/usr/bin/env python3
import timeit
from sys import argv
from functools import reduce

def reduces(ch):
    a = [i for i in range(1, int(ch)+1)]
    return reduce(lambda x, y: x + y**2, a)

def repets(ch):
    s = 0
    a = [i for i in range(1, int(ch) + 1)]
    for i in a:
        s += i**2
    return s

def main():
    try:
        if argv[1] == 'loop':
            print(timeit.timeit('repets('+argv[3]+')', setup='from __main__ import repets', number=int(argv[2])))
        elif argv[1] == 'reduce':
            print(timeit.timeit('reduces('+argv[3]+')', setup='from __main__ import reduces', number=int(argv[2])))
        else:
            print("Not exist this rule")
    except:
        print("Error incoming date")
    # emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

if __name__ == '__main__':
    if len(argv) == 4:
        main()
