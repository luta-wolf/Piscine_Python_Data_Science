import os
# import psutil
import sys
import re

class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file = path_to_the_file

    def dist_by_release(self, filename):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts.
        You need to extract years from the titles. Sort it by counts descendingly.
        """

        release_years = {}


        return release_years

    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
         Sort it by counts descendingly.
        """
        pass
        # return genres

    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        pass
        # return movies



def count_years(filename):
    list_years = []
    dict_years ={}
    with open(filename, 'r') as file:
        for row in file:
            step1 = re.findall(r"[(]\d{4}[)]", row)
            step2 = str(step1)[3:7]
            list_years.append(step2)
    unic_years = sorted(list(set(list_years)))
    del(unic_years)[0]
    for i in unic_years:
        dict_years[i] = list_years.count(i)
    sorted_tuples = sorted(dict_years.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {key: value for key, value in sorted_tuples}
    print(sorted_dict)





def main():
    file = "ml-latest-small/movies.csv"
    movie = count_years(file)


if __name__ == "__main__":
    main()
