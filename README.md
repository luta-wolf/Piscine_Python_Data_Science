# Piscine Python Data Science

- [Чеклисты](https://github.com/Chegashi/Piscine_Python_Data_Science.42)
- Установка [Home brew](https://docs.brew.sh/Installation) на школьные маки.

## Day 00
### Инструменты командной строки UNIX

Описание: В первый день мы поможем вам приобрести навыки использования инструментов командной строки UNIX для решения базовых задач по обработке и анализу данных. Вы узнаете, как использовать curl, sort, uniq, jq, sed и cat для сбора и предварительной обработки данных.

- Команда AWK в Linux с примерами [часть 1](https://routerus.com/awk-command/?ysclid=l84uzjls5s521557873), [часть 2](https://habr.com/ru/company/ruvds/blog/327754/?ysclid=l84txpfiyk737745328) и [часть 3](https://zalinux.ru/?p=554)
- API hh.ru [часть 1](https://habr.com/ru/company/hh/blog/303168/), [часть 2](https://github.com/hhru/api/blob/master/README.md#%D0%A0%D0%B5%D1%81%D1%83%D1%80%D1%81%D1%8B) и  [часть 3](https://github.com/hhru/api/blob/master/docs/general.md)
- Linux инструмент [JQ](https://russianblogs.com/article/9830458316/)

#### Начало работы
Чтобы работала JQ подключаем в ENV home brew, которую мы установли в папку goinfre
```
eval "$(~/goinfre/homebrew/bin/brew shellenv)"
```

Запускаем hh.sh с параметром `data scientist` для нашего задания и любой профессией для парсинга остального
```
sh hh.sh "data scientist"
```
Сырые данне складываем в JSON файл и затем преобразовываем его в CSV файл, сортируем, заменяем строки и разделяем/объединяем по файлам.


## Day 01
### Введение в Python: синтаксис и семантика

Резюме: Сегодня мы поможем вам приобрести базовые знания о синтаксисе и семантикеиз Питона.

- Сортировака [словаря](https://python-school.ru/blog/sort-dict/) в Python

## Day 02
### Введение в Python: навыки ООП

Резюме: сегодня мы поможем вам получить базовые знания об ООП-подходе в Python.
- работа с [json](https://www.awesomeandrew.ru/2019/03/31/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8-%D0%B2-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B5-json-%D0%B2-python/)
- работа с [Requests](https://python-scripts.com/requests)

## Day 03
### Введение в Python: управление пакетами и виртуальная среда

Резюме: Сегодня мы поможем вам получить базовые знания о том, как управлять библиотеками в Python и работать с виртуальными средами (virtual environment [`venv`](https://github.com/luta-wolf/Piscine_Python_Data_Science/tree/main/DS_03)).

1) Установка [venv](https://pythonchik.ru/okruzhenie-i-pakety/virtualnoe-okruzhenie-python-venv)
-  `python3.10 -m venv venv` - установка
-  `. venv/bin/activate` - запускаем так
-  `source venv/bin/activate` - или так
-  `pip install --upgrade pip` - oбновляем pip
-  `deactivate` - и выход из окружения


2) Установка библиотек:
- `pip install termgraph`       [Termgraph](https://github.com/mkaz/termgraph)
- `pip install beautifulsoup4`  Beautiful soup [часть 1](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html) + [часть 2](http://bs4ru.geekwriter.ru/bs4ru.html) и [часть 3](https://habr.com/ru/post/544828/)
- `pip install lxml`            [lxml](https://pypi.org/project/lxml/) + [еще](https://webdevblog.ru/vvedenie-v-biblioteku-python-lxml/)
- `pip install pytest`          [PyTest](https://habr.com/ru/post/448782/)
- `pip install requests`        [requests](https://pypi.org/project/requests/) + [еще](https://realpython.com/python-requests/)

3) Полезное:
- [Termgraph](https://xakep.ru/2018/09/14/www-termgraph/) — консольная утилита для рисования графиков
- Модуль [BeautifulSoup4](https://docs-python.ru/packages/paket-beautifulsoup4-python/) в Python, разбор HTML
- Профилирование и отладка Python, [инструменты](https://habr.com/ru/company/vk/blog/202832/)
- PyTest [часть 1](https://habr.com/ru/post/269759/) и [часть 2](https://habr.com/ru/post/448782/)


## Day 04
### Введение в Python: эффективные методы написания кода

Резюме: Сегодня мы поможем вам написать код, который работает быстрее.

- Руководство по использованию [list comprehension](https://pythonru.com/osnovy/python-list-comprehension)
- Модуль [timeit](https://pythonim.ru/moduli/timeit-python) в Python
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Функциональное программирование](http://pythonicway.com/python-functinal-programming) в Python: lambda, zip, filter, map reduce
- Основы [функционального программирования](https://habr.com/ru/post/555378/) на Python
- Класс [Counter](https://docs-python.ru/standart-library/modul-collections-python/klass-counter-modulja-collections/) модуля collections в Python.
- [Resource](https://docs.python.org/3/library/resource.html) usage information
- [Генераторы](https://pythonist.ru/generatory-v-python/) в Python и их отличие от списков и функций


## Day 05
### Pandas: работа с фреймами данных
Резюме: сегодня мы поможем вам приобрести навыки с Pandas.

- Подборка статей о работе с библиотеками для [анализа данных](https://dfedorov.spb.ru/pandas/) на языке Python
- Обзор [типов данных](https://dfedorov.spb.ru/pandas/%D0%9E%D0%B1%D0%B7%D0%BE%D1%80%20%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20pandas.html) Pandas
- еще о [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/general_functions.html)


## Day 06
### Pandas: SQL and Pandas
Резюме: сегодня мы поможем вам приобрести навыки работы с SQL
- Методы объекта Connection [SQLite3](https://docs-python.ru/standart-library/modul-sqlite3-python/obekt-connection-modulja-sqlite3/).
- [strftime](https://oracleplsql.ru/strftime-sqlite.html) функция SQLite


## Day 07
### Pandas, SQL и визуализация данных
Резюме: Сегодня мы поможем вам с визуализацией данных в Matplotlib, Seaborn и Plotly.

- [Цвета](https://datascientyst.com/full-list-named-colors-pandas-python-matplotlib/) в Pandas
- - An Overview of Pandas [GroupBy](https://ds100.org/fa18/assets/lectures/lec03/03-groupby-and-pivot-basics.html)
- pandas.[DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plothttps://kanoki.org/2019/09/16/dataframe-visualization-with-pandas-plot/).plot

## Day 08
### Введение в машинное обучение
Резюме: Сегодня мы поможем вам с основными задачами, связанными с машинным обучением в Python.

## Day 09
### Машинное обучение: продвинутый уровень
Резюме: сегодня мы поможем вам справиться с сложными задачами, связанными с машинным обучением в Python.

## Rush 00
### Аналитика MovieLens
Резюме: Этот раш поможет вам укрепить навыки, полученные в предыдущие дни.
- Класс [OrderedDict](https://docs-python.ru/standart-library/modul-collections-python/klass-ordereddict-modulja-collections/) модуля collections в Python.
-


## Rush 01
### Продовольствие и питание
Резюме: Этот раш поможет вам укрепить навыки, полученные в предыдущие дни.
Датасет epi_r.csv скачать [здесь](https://drive.google.com/file/d/1hzmxNBrY7-9mv5EpqAvhVUiJahfrcYUN/view)


