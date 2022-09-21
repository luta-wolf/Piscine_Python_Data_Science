#!python3
import os
import psutil
import sys


def get_generator(file_name: str):
    try:
        with open(file_name, 'r') as file:
            for row in file:
                yield row
    except OSError as e:
        print("\033[91mError: ", e)

def main(file_name):
    generetor = get_generator(file_name)
    for i in generetor:
        pass
    proc = psutil.Process(os.getpid())
    print(f'Peak memory usage = {proc.memory_info().rss / 1024 ** 3:0.3f} GB')
    cpu_times = proc.cpu_times()
    print(f'User Mode Time + System Mode Time = {cpu_times.user + cpu_times.system:0.2f}s')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
