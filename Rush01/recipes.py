#python3

import requests, sys
from bs4 import BeautifulSoup
# import lxml


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

	url = f'https://www.epicurious.com/search/{ticker}?content=recipe'
	try:
		response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
	except requests.exceptions.ConnectionError as e:
		print('Error: {}'.format(e))
		return None
	soup = BeautifulSoup(response.text, "html.parser")
	# soup = BeautifulSoup(response.text, "lxml.parser")
	name = soup.find_all(class_ = "hed")
	rating = soup.find_all(class_ = 'recipes-ratings-summary')
	if name and rating:
		print('III. TOP-3 SIMILAR RECIPES:')
		for i in range(3):
			print(get_line(name, rating, i))
	else:
		print("There are no such recipes.")


if __name__ == "__main__":
	if len(sys.argv) > 1:
		line = ""
		for i in range(1, len(sys.argv)):
			line += sys.argv[i] + '%20'
		line = line[:-3]
		parse(line)
	else:
		raise ValueError("Too few arguments")
