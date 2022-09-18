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

def stock_prices():
	COMPANIES, STOCKS = data()
	if len(sys.argv) == 2:
		line = sys.argv[1].capitalize()
		if line in COMPANIES:
			value = COMPANIES[line]
			print(STOCKS[value])
		else:
			print("Unknown company")


def main():
	stock_prices()


if __name__ == '__main__':
	main()
