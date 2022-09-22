#!/usr/bin/env python3
import timeit
from collections import Counter
from random import randint

def my_counter(lst):
    d = {}
    for el in lst:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return d

def last_ten(lst):
    return sorted(my_counter(lst).items(), key=(lambda x: -x[1]))[:10]

def main():
    lis = [randint(0, 100) for x in range(1000000)]
    print('my function: ', timeit.timeit(f'my_counter({lis})', setup='from __main__ import my_counter', number=1))
    print('Counter: ', timeit.timeit(f'Counter({lis})', setup='from __main__ import Counter', number=1))
    print('my top: ', timeit.timeit(f'last_ten({lis})', setup='from __main__ import last_ten', number=1))
    print('Counter\'s top: ', timeit.timeit(f'Counter({lis}).most_common(10)', setup='from __main__ import Counter', number=1))

if __name__ == '__main__':
        main()

