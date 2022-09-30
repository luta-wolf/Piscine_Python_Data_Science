class SimilarRecipes:
    """
    Recommending similar recipes with additional information
    """
    def __init__(self, list_of_ingredients):
        """
        Put any here fields that you think you will need.
        """

    def find_all(self):
        """
This method returns a list of indexes of the recipes that contain the given list of ingredients. If there is no recipe that contains all the ingredients, handle it.
        """
        return indexes

    def top_similar(self, n):
        """
This method returns a text formatted as in the example above with title, rating, and URL. Before that, it finds top-n most similar recipes by the number of additional ingredients that are required in the recipes using indexes from the find_all method. The most similar is the one that does not require any other ingredients. Next is the one that requires only one, etc. If it requires 5 more ingredients, do not return those recipes.
        """
        return text_with_recipes
