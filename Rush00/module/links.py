#!/usr/bin/env python

from collections import Counter, OrderedDict
from bs4 import BeautifulSoup
import requests


class Links:
    """
    Analyzing data from links.csv
    """

    def __init__(self, path_to_the_file='../data/links.csv'):
        """
        Put here any fields that you think you will need.
        """
        self.file = path_to_the_file

        self.movie_imdb_ID = {}
        try:
            with open(self.file, 'r') as fl:
                for i, line in enumerate(fl):
                    if i == 0:
                        continue
                    mov = line.split(',')[0]
                    self.movie_imdb_ID[mov] = line.split(',')[1]
            range_nm = list(map(str, range(1, 6)))
            self.data = self.get_imdb(range_nm,
                                      ['Director', 'Also known as', 'Budget', 'Gross worldwide', 'Runtime'])
        except OSError as os_err:
            print(os_err)

    def get_links_by_movie_id(self, idx):
        with open(self.file, 'r') as fl:
            for i, line in enumerate(fl):
                if i == 0:
                    continue
                if int(line.split[','][0] == idx):
                    return line

    def get_imdb(self, list_of_movies, list_of_fields):
        """
        The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the
        argument (movieId). For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime]. The values
        should be parsed from the IMDB webpages of the movies. Sort it by movieId descendingly.
        """
        imdb_info = []
        for mov in list_of_movies:
            imdb = [mov]
            url = "https://www.imdb.com/title/tt{}".format(self.movie_imdb_ID[mov])
            response = requests.get(url, headers={'User-Agent': 'PYTHON'})
            soup = BeautifulSoup(response.text, 'lxml')
            tags = soup.find_all('li', role='presentation', class_='ipc-metadata-list__item')
            for field in list_of_fields:
                for tag in tags:
                    if tag.text.find(field) != -1:
                        imdb.append(tag.text.replace(field, ''))
                        break

            if len(imdb) == 6:
                imdb_info.append(imdb)

        imdb_info = sorted(imdb_info, key=lambda x: int(x[0]), reverse=True)
        return imdb_info

    def top_directors(self, n):
        """
        The method returns a dict with top-n directors where the keys are directors and 
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        directors = [mov[1] for mov in self.data]
        directors = dict(Counter(directors))
        sorted_pairs = sorted(directors.items(), key=lambda item: item[1], reverse=True)
        directors = OrderedDict()
        for k, v in sorted_pairs:
            if k not in directors:
                directors[k] = v
                if len(directors) == n:
                    break
        return dict(directors)

    def most_expensive(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        budgets = {}
        for mov in self.data:
            budgets[mov[2]] = self.summa_to_int(mov[3])
        sorted_pairs = sorted(budgets.items(), key=lambda item: item[1], reverse=True)
        budgets = OrderedDict()
        for k, v in sorted_pairs:
            if k not in budgets:
                budgets[k] = v
                if len(budgets) == n:
                    break

        return dict(budgets)

    def summa_to_int(self, string):
        return int(string[1::].split(' ')[0].replace(',', ''))

    def most_profitable(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
     Sort it by the difference descendingly.
        """
        profits = {}
        for mov in self.data:
            profits[mov[2]] = self.summa_to_int(mov[4]) - self.summa_to_int(mov[3])
        sorted_pairs = sorted(profits.items(), key=lambda item: item[1], reverse=True)
        profits = OrderedDict()
        for k, v in sorted_pairs:
            if k not in profits:
                profits[k] = v
                if len(profits) == n:
                    break

        return dict(profits)

    def longest(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version – choose any.
     Sort it by runtime descendingly.
        """
        runtimes = {}
        for mov in self.data:
            runtimes[mov[2]] = self.time_to_int(mov[5])
        sorted_pairs = sorted(runtimes.items(), key=lambda item: item[1], reverse=True)
        runtimes = OrderedDict()
        for k, v in sorted_pairs:
            if k not in runtimes:
                runtimes[k] = v
                if len(runtimes) == n:
                    break

        return dict(runtimes)

    def time_to_int(self, string):
        result = 0
        if 'hour' in string:
            result += int(string.split('hour')[0]) * 60
        if 'minutes' in string:
            result += int(string.split(' ')[-2])
        return result

    def top_cost_per_minute(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it.
     The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        costs = {}
        for mov in self.data:
            costs[mov[2]] = round(self.summa_to_int(mov[3]) / self.time_to_int(mov[5]), 2)
        sorted_pairs = sorted(costs.items(), key=lambda item: item[1], reverse=True)
        costs = OrderedDict()
        for k, v in sorted_pairs:
            if k not in costs:
                costs[k] = v
                if len(costs) == n:
                    break

        return dict(costs)

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     lll = Links() #('../data/links.csv')
#     res = lll.most_profitable(35)
#     for p, m in res.items():
#         print(p, m)
