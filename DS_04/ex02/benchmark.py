#!/usr/bin/env python3
import timeit
from sys import argv

def comprehensions(emails):
    return [mail for mail in emails if mail.endswith('@gmail.com')]

def maps(emails):
    return list(map(lambda mail: mail if mail.endswith('@gmail.com') else None, emails))

def filters(emails):
    return list(filter(lambda mail: mail.endswith('@gmail.com'), emails))

def repets(emails):
    lst = []
    for mail in emails:
        if mail.endswith('@gmail.com'):
            lst.append(mail)
    return lst

def main():
    try:
        emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
        if argv[1] == 'loop':
            print(timeit.timeit(f'repets({emails})', setup='from __main__ import repets', number=int(argv[2])))
        elif argv[1] == 'list_comprehension':
            print(timeit.timeit(f'comprehensions({emails})', setup='from __main__ import comprehensions', number=int(argv[2])))
        elif argv[1] == 'map':
            print(timeit.timeit(f'maps({emails})', setup='from __main__ import maps', number=int(argv[2])))
        elif argv[1] == 'filter':
            print(timeit.timeit(f'filters({emails})', setup='from __main__ import filters', number=int(argv[2])))
        else:
            print("Not exist this rule")
    except:
        print("Error incoming date")

if __name__ == '__main__':
    if len(argv) == 3:
        main()
