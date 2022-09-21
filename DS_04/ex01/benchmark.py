#!/usr/bin/env python3
import timeit

def comprehensions(emails):
    return [mail for mail in emails if mail.endswith('@gmail.com')]

def maps(emails):
    return list(map(lambda mail: mail if mail.endswith('@gmail.com') else None, emails))

def repets(emails):
    lst = []
    for mail in emails:
        if mail.endswith('@gmail.com'):
            lst.append(mail)
    return lst

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    repets_time = timeit.timeit(f'repets({emails})', setup='from __main__ import repets', number=900000)
    maps_time = timeit.timeit(f'maps({emails})', setup='from __main__ import maps', number=900000)
    comprehensions_time = timeit.timeit(f'comprehensions({emails})', setup='from __main__ import comprehensions', number=900000)
    # print(repets(emails))
    # print(comprehensions(emails))
    time = sorted([repets_time, comprehensions_time, maps_time])
    if repets_time < comprehensions_time and repets_time < maps_time:
        print('it is better to use a loop\n', str(time[0]) + ' vs ' + str(time[1]) + ' vs ' + str(time[2]), sep='')
    elif comprehensions_time < repets_time and comprehensions_time < maps_time:
        print('it is better to use a list comprehension\n', str(time[0]) + ' vs ' + str(time[1]) + ' vs ' + str(time[2]), sep='')
    else:
        print('it is better to use a map\n', str(time[0]) + ' vs ' + str(time[1]) + ' vs ' + str(time[2]), sep='')

if __name__ == '__main__':
    main()
