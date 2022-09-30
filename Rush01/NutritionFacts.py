class NutritionFacts:
    """
    Offering nutritional facts on given ingredients.
    """
    def __init__(self, list_of_ingredients):
        """
        Put any fields here that you think you will need.
        """

    def retrieve(self):
        """
This method gets all the nutrient facts about the given ingredients from the file with pre-collected information. It returns any structure that you find useful.
        """
        return facts

    def filter(self, must_nutrients, n):
        """
This method selects from the nutrient facts only nutrients from the list of must_nutrients (for example, from PDF-files below) and the top-n nutrients with the highest values of daily value norms for the given ingredient. It returns a text formatted as in the example above.
        """
        return text_with_facts
