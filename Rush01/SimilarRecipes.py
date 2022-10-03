import requests, sys
from bs4 import BeautifulSoup

class SimilarRecipes:
    """
    Recommending similar recipes with additional information
    Рекомендация похожих рецептов c дополнительной информацией
    """
    def get_line(recipes, rating, i):
        start = str(recipes[i]).find("href=")
        tmp =str(recipes[i])[start:]
        finish = tmp.find('>')
        finish2 = tmp.find('<')
        line_name = tmp[finish + 1:finish2]
        line_url = 'https://www.epicurious.com' + tmp[6:finish - 1]
        tmp = str(rating[i]).split()
        line_rating = tmp[4][21:-1]
        new_line = '- ' + line_name + ', rating: ' + line_rating + ', URL: ' + line_url
        return new_line


    def parse(ticker):
        print('III. TOP-3 SIMILAR RECIPES:')
        url = f'https://www.epicurious.com/search/{ticker}?content=recipe'
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
        except requests.exceptions.ConnectionError as e:
            print('Error: {}'.format(e))
            return None
        soup = BeautifulSoup(response.text, "html.parser")
        name = soup.find_all(class_ = "hed")
        rating = soup.find_all(class_ = 'recipes-ratings-summary')
        if name and rating:
            for i in range(3):
                print(SimilarRecipes.get_line(name, rating, i))
        else:
            print("There are no such recipes.")
