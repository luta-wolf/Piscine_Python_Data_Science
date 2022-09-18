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


def ticker_symbols(line):
	COMPANIES, STOCKS = data()
	line = line.upper()					# приводим к верхнему регистру
	if line in STOCKS:
		for key, value in COMPANIES.items():	# разбиваем на ключ и значение
			if value == line:
				print(key, STOCKS[line])
	else:
		print("Unknown company")


def main():
	if len(sys.argv) == 2:
		ticker_symbols(sys.argv[1])
		

if __name__ == "__main__":
	main()
