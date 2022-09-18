from re import M


def dataset():
	list_of_tuples = [
	('Russia', '25'),
	('France', '132'),
	('Germany', '132'),
	('Spain', '178'),
	('Italy', '162'),
	('Portugal', '17'),
	('Finland', '3'),
	('Hungary', '2'),
	('The Netherlands', '28'),
	('The USA', '610'),
	('The United Kingdom', '95'),
	('China', '83'),
	('Iran', '76'),
	('Turkey', '65'),
	('Belgium', '34'),
	('Canada', '28'),
	('Switzerland', '26'),
	('Brazil', '25'),
	('Austria', '14'),
	('Israel', '12')
	]
	return list_of_tuples

def dict_sorter():
	data = dataset()
	sorted_name = sorted(data, key=lambda x : x[0])
	sorted_digital = sorted(sorted_name, key=lambda x : int(x[1]), reverse=True)
	my_dict =dict(sorted_digital)
	for key in my_dict:
		print(key)


def main():
	dict_sorter()

if __name__ == "__main__":
	main()
