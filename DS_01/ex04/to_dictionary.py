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


# def to_dictionary():
# 	data = dataset()
# 	my_dict = {}
# 	for i in data:
# 		if i[1] in my_dict:
# 			my_dict[i[1]] += '\', \''+ i[0]
# 		else:
# 			my_dict[i[1]] = i[0]
# 	for key,value in my_dict.items():
# 		print(f"\'{key}\' : \'{value}\'")

def to_dictionary():
	data = dataset()
	my_dict = {}

	for i in data:
		if i[1] in my_dict:
			my_dict[i[1]].append(i[0])
		else:
			my_dict[i[1]] = [i[0]]
	return my_dict


def print_dict(my_dict):
	for key, value in my_dict.items():
		for amount in value:
			print(f"\'{key}\' : \'{amount}\'")
	print(my_dict)

def name():
	value = to_dictionary()
	print_dict(value)



if __name__ == "__main__":
	name()
