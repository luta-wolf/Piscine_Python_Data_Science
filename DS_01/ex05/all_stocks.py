import sys

def data():
	COMPANIES = {
	'Apple': 'AAPL',
	'Microsoft': 'MSFT',
	'Netflix': 'NFLX',
	'Tesla': 'TSLA',
	'Nokia': 'NOK'
	}
	STOCKS = {
	'AAPL': 287.73,
	'MSFT': 173.79,
	'NFLX': 416.90,
	'TSLA': 724.88,
	'NOK': 3.37
	}
	return COMPANIES, STOCKS

def all_stocks(argv):
	COMPANIES, STOCKS = data()
	line = argv.split(',')
	new_line = []
	for i in line:
		new_line.append(i.strip())
		if "" in new_line:
			return

	for i in new_line:
		if i.capitalize() in COMPANIES:
			print(f"{i.capitalize()} stock price is {STOCKS[COMPANIES[i.capitalize()]]}")
		elif i.upper() in STOCKS:
			for key, value in COMPANIES.items():
				if value == i.upper():
					print(f"{value} is a ticker symbol for {key}")
		else:
			print(f"{i} is an unknown company or an unknown ticker symbol")


def main():
	if len(sys.argv) == 2:
		all_stocks(sys.argv[1])

if __name__ == "__main__":
	main()
