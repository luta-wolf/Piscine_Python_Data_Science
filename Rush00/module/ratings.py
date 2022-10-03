import datetime as dt
from collections import Counter, defaultdict
from module.movies import Movies
from functools import reduce


class Statistics:
    @staticmethod
    def average(values: list):
        return sum(values) / len(values)

    @staticmethod
    def median(values: list):
        if len(values) == 0:
            raise ValueError('List is empty.')

        if len(values) == 1:
            return float(values[0])

        values = sorted(values)
        mid = int(len(values) / 2)

        if len(values) % 2:
            return float(values[mid])

        return (values[mid - 1] + values[mid]) / 2.0

    @classmethod
    def variance(cls, values: list):
        mean = cls.average(values)

        def reduce_func(prev, curr):
            diff = curr - mean
            return prev + diff * diff

        squares_sum = reduce(reduce_func, values)

        return squares_sum / len(values)


class Ratings:
	# """
	# Analyzing data from ratings.csv
	# """
    def __init__(self, path_to_the_file: str):
		# """
		# Put here any fields that you think you will need.
		# """
        self.filename = path_to_the_file


    def read_file(self):
        with open(self.filename, "r", encoding='utf-8') as f:
            line = f.readlines()
            all_lines = []

            for i in range(len(line)):
                tmp_line = line[i].replace('\n', '')
                all_lines.append(tmp_line.split(','))

        return all_lines

    class Movies:
        def __init__(self, ratings_cls, movies_cls: Movies):
            if not isinstance(ratings_cls, Ratings) or not isinstance(movies_cls, Movies):
                raise ValueError('invalid class object')
            self.ratings = ratings_cls
            self.movies_cls = movies_cls

        def dist_by_year(self):
			# """
			# The method returns a dict where the keys are years and the values are counts.
			# Sort it by years ascendingly. You need to extract years from timestamps.
			# """
            result = Counter()
            tmp = self.ratings.read_file()
            for i in range(1, len(tmp)):
                year = dt.datetime.fromtimestamp(int(tmp[i][3])).year
                result[year] += 1

            ratings_by_year = dict(sorted(result.items()))

            return ratings_by_year

        def dist_by_rating(self):
			# """
			# The method returns a dict where the keys are ratings and the values are counts.
			# Sort it by ratings ascendingly.
			# """
            result = Counter()
            tmp = self.ratings.read_file()

            for i in range(1, len(tmp)):
                rat = tmp[i][2]
                result[rat] += 1

            ratings_distribution = dict(sorted(result.items()))

            return ratings_distribution

        def top_by_num_of_ratings(self, top_size: int):
			# """
			# The method returns top-n movies by the number of ratings.
			# It is a dict where the keys are movie titles and the values are numbers.
			# Sort it by numbers descendingly.
			# """
            result = Counter()

            tmp = self.ratings.read_file()

            for i in range(1, len(tmp)):
                result[self.movies_cls.get_title(tmp[i][1])] += 1

            top_movies = dict(result.most_common(top_size))

            return top_movies

        def top_by_ratings(self, n, metric=Statistics.average):
			# """
			# The method returns top-n movies by the average or median of the ratings.
			# It is a dict where the keys are movie titles and the values are metric values.
			# Sort it by metric descendingly.
			# The values should be rounded to 2 decimals.
			# """
            all_movies = defaultdict(list)

            tmp = self.ratings.read_file()
            del tmp[0]

            for data in tmp:
                all_movies[self.movies_cls.get_title(data[1])].append(float(data[2]))

            for movie in all_movies:
                all_movies[movie] = round(metric(all_movies[movie]), 2)

            top_movies = dict(sorted(all_movies.items(), key=lambda item: item[1], reverse=True)[:n])

            return top_movies

        def top_controversial(self, n):
			# """
			# The method returns top-n movies by the variance of the ratings.
			# It is a dict where the keys are movie titles and the values are the variances.
			# Sort it by variance descendingly.
			# The values should be rounded to 2 decimals.
			# """
            all_movies = defaultdict(list)

            tmp = self.ratings.read_file()
            del tmp[0]

            for data in tmp:
                all_movies[self.movies_cls.get_title(data[1])].append(float(data[2]))

            for movie in all_movies:
                all_movies[movie] = round(Statistics.variance(all_movies[movie]), 2)

            top_movies = dict(sorted(all_movies.items(), key=lambda item: item[1], reverse=True)[:n])

            return top_movies

    class Users(Movies):
		# """
		# In this class, three methods should work.
		# The 1st returns the distribution of users by the number of ratings made by them.
		# The 2nd returns the distribution of users by average or median ratings made by them.
		# The 3rd returns top-n users with the biggest variance of their ratings.
		# Inherit from the class Movies. Several methods are similar to the methods from it."""
        def dist_by_ratings_number(self):
            ratings_distribution = Counter()

            tmp = self.ratings.read_file()
            del tmp[0]

            for data in tmp:
                ratings_distribution[data[0]] += 1

            ratings_distribution = dict(sorted(ratings_distribution.items(), key=lambda item: item[1]))

            return ratings_distribution

        def dist_by_ratings_values(self, metric=Statistics.average):
            all_ratings = defaultdict(list)

            tmp = self.ratings.read_file()
            del tmp[0]

            for data in tmp:
                all_ratings[data[0]].append(float(data[2]))

            for user in all_ratings:
                all_ratings[user] = round(metric(all_ratings[user]), 2)

            all_ratings = dict(sorted(all_ratings.items(), key=lambda item: item[1]))

            return all_ratings

        def top_by_variance(self, n: int):
            all_ratings = defaultdict(list)

            tmp = self.ratings.read_file()
            del tmp[0]

            for data in tmp:
                all_ratings[data[1]].append(float(data[2]))

            for user in all_ratings:
                all_ratings[user] = round(Statistics.variance(all_ratings[user]), 2)

            all_ratings = dict(sorted(all_ratings.items(), key=lambda item: item[1], reverse=True)[:n])

            return all_ratings
