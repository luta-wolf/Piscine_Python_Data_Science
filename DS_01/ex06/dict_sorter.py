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
	my_dict = dict(data)
	my_dict2 = {}							# создание словаря
	for key, value in my_dict.items():
		my_dict2[key]= int(value)
	print(my_dict2)

	sorted_dict = {}
	sorted_keys = sorted(my_dict2, key=my_dict2.get)	# сортировака по значениям
	# print(my_dict)
	for w in sorted_keys:
		sorted_dict[w] = my_dict2[w]

	# print(sorted_dict)

	for key, value in sorted_dict.items():
		print(f"{key} : {value}")



def main():
	dict_sorter()

if __name__ == "__main__":
	main()
