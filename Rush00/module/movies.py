import re
from collections import Counter


class Movies:
    """
    Analyzing data from movies.csv
    """

    def __init__(self, path_to_the_file='../data/movies.csv'):
        """
        Put here any fields that you think you will need.
        """
        self.filename = path_to_the_file
        self.data = self.read_file()
        self.titles = {}
        for data in self.read_file():
            self.titles[data[0]] = data[1]


    def read_file(self):
        with open(self.filename, 'r') as file:
            tmp = file.readlines()
        return tmp

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts.
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        list_years = []
        for row in self.data:
            step1 = re.findall(r"[(]\d{4}[)]", row[1])
            step2 = str(step1)[3:7]
            list_years.append(step2)

        # unic_years = sorted(list(set(list_years)))
        # del(unic_years)[0]
        # for i in unic_years:
        #     dict_years[i] = list_years.count(i)
        # sorted_tuples = sorted(dict_years.items(), key=lambda item: item[1], reverse=True)
        # release_years = {key: value for key, value in sorted_tuples}
        # print(release_years)

        release_years = dict(Counter(list_years).most_common())

        return release_years

    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
         Sort it by counts descendingly.
        """
        all_lines = self.data
        del all_lines[0]

        tmp = [el[2].split('|') for el in all_lines]

        result = Counter()

        for elem in tmp:
            for el in elem:
                if el:
                    result[el] += 1

        return dict(result.most_common())

    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        all_lines = self.read_file()
        del all_lines[0]

        result = dict()

        for elem in all_lines:
            result[elem[1]] = len(elem[2].split('|'))

        return dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:n])

    def get_title(self, movie_id):
        return self.titles.get(movie_id)

    def read_file(self):
        with open(self.filename, "r", encoding='utf-8') as f:
            line = f.readlines()
            all_lines = []
            for i in range(len(line)):
                tmp_line = line[i].replace('\n', '')
                if tmp_line.find('"') != -1:
                    splitted = re.split(r',\"|\",', tmp_line)
                else:
                    splitted = tmp_line.split(',')
                all_lines.append(splitted)
        return all_lines
