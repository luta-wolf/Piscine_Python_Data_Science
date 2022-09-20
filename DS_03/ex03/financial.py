#!python3
from time import sleep
import requests, sys
from bs4 import BeautifulSoup


def parse(ticker, table):
	sleep(5)
	url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
	try:
		response = requests.get(url,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
	except requests.exceptions.ConnectionError as e:
		print('Error: {}'.format(e))
		return None
	soup = BeautifulSoup(response.text, "html.parser")
	finance = soup.find_all('div', class_ = 'fi-row')
	tab = {}
	for elem in finance:
		try:
			title = elem.find('div', class_ = 'Va(m)').text
			lst = []
			fin_value = elem.find_all('div', class_ = 'Ta(c)')
			for item in fin_value:
				lst.append(item.text)
			tab[title] = lst
		except Exception as e:
			continue
	try:
		return tuple([table,*tab[table]])
	except KeyError as e:
		print('Error: {}'.format(e))
		return None

def main(ticker, table):
	"""
    Main function.
    """
	res = parse(ticker, table)
	if res:
		print(res)

if __name__ == '__main__':
	try:
		if len(sys.argv) == 3:
			main(sys.argv[1], sys.argv[2])
		else:
			raise ValueError('Count of arg')
	except ValueError as e:
		print('Exception:', e)
