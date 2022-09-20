#! /bin/sh


python3 -m cProfile -s time financial.py 'MSFT' 'Total Revenue' > profiling-sleep.txt
python3 -m cProfile -s time financial.py 'MSFT' 'Total Revenue' > profiling-tottime.txt
python3 -m cProfile -s time financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-http.txt
python3 -m cProfile -s calls financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-ncalls.txt
# Скрипты записывают результаты в файл
python3 financial_enhanced.py 'MSFT' 'Total Revenue'

# Скрипт со
python3 -m cProfile -s calls -o pstats-cumulative.temp financial_enhanced.py
python3 -m pstats pstats-cumulative.temp
% sort cumulative
% stats 5
