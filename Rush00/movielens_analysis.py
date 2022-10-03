from module.tags import Tags
from module.links import Links
from module.movies import Movies
from module.ratings import Ratings

class TestMovies:
    @classmethod
    def setup_class(cls):
        cls.movies = Movies('data/movies.csv')

    def test_dist_by_release(self):
        self.movies.dist_by_release()

    def test_dist_by_genres(self):
        self.movies.dist_by_release()

    def test_most_genres(self, n=10):
        self.movies.most_genres(n)

class TestRatings:
    @classmethod
    def setup_class(cls):
        cls.ratings = Ratings('data/ratings.csv')
        cls.movies = Movies('data/movies.csv')
        cls.ratings_movies = Ratings.Movies(cls.ratings, cls.movies)
        cls.ratings_users = Ratings.Users(cls.ratings, cls.movies)

    def test_movies_dist_by_years(self):
        self.ratings_movies.dist_by_year()

    def test_movies_dist_by_rating(self):
        self.ratings_movies.dist_by_rating()

    def test_top_by_num_of_ratings(self, n=10):
        self.ratings_movies.top_by_num_of_ratings(n)

    def test_top_by_ratings(self, n=10):
        self.ratings_movies.top_by_ratings(n)

    def test_top_controversial(self, n=10):
        self.ratings_movies.top_controversial(n)

    def test_dist_by_ratings_number(self):
        self.ratings_users.dist_by_ratings_number()

    def test_dist_by_ratings_values(self):
        self.ratings_users.dist_by_ratings_values()

    def test_top_by_variance(self, n=10):
        self.ratings_users.top_by_variance(n)

class Tests:
    def setup_class(self):
        self.tags = Tags('data/tags.csv')
        self.links = Links('data/links.csv')

    def test_tags_most_words(self):
        result = self.tags.most_words(10)
        return (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_tags_longest(self):
        result = self.tags.longest(10)
        return (isinstance(result, list) and
                (set(map(type, result)) == {str}))

    def test_tags_most_words_and_longest(self):
        result = self.tags.most_words_and_longest(232)
        return (isinstance(result, list) and
                set(map(type, result)) == {str})

    def test_tags_most_popular(self):
        result = self.tags.most_popular(10)
        return (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_get_imdb(self):
        result = self.links.get_imdb(['1', '2', '3', '4', '5'], ['director', 'name', 'genre', 'actor'])
        return (isinstance(result, list) and
                set(map(type, result)) == {list} and
                sorted(result, reverse=True, key=lambda x: x[0]) == list(result))

    def test_top_directors(self):
        self.links.get_imdb(['1', '2', '3', '4', '5'], ['director', 'name', 'genre', 'actor'])
        result = self.links.top_directors(3)
        return (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result, reverse=True, key=lambda x: x[1]) == list(result))

# def tags_n_linksTest():
#     testTags_n_Links = Tests()
#     testTags_n_Links.setup_class()
#
#     print(testTags_n_Links.test_tags_most_words())
#     print(testTags_n_Links.test_tags_longest())
#     print(testTags_n_Links.test_tags_most_words_and_longest())
#     print(testTags_n_Links.test_tags_most_popular())
#     print(testTags_n_Links.test_get_imdb())
#
#     testTags_n_Links.test_top_directors()
#
# def ratingsTest():
#     testRatings = TestRatings()
#     testRatings.setup_class()
#
#     testRatings.test_movies_dist_by_years()
#     testRatings.test_movies_dist_by_rating()
#     testRatings.test_top_by_num_of_ratings(5)
#     testRatings.test_top_by_ratings(5)
#     testRatings.test_top_controversial(5)
#     testRatings.test_dist_by_ratings_number()
#     testRatings.test_dist_by_ratings_values()
#     testRatings.test_top_by_variance(5)


# def moviesTest():
#     testMovies = TestMovies()
#     testMovies.setup_class()
#
#     testMovies.test_dist_by_release()
#     testMovies.test_dist_by_genres()
#     testMovies.test_most_genres(5)


# if __name__ == '__main__':
    # moviesTest()
    # ratingsTest()
    # tags_n_linksTest()
