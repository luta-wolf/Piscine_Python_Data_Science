def data_types():
	list_type = []
	line = [
		1,			# int
		'string',	# str
		1.1,		# float
		True,		# boll
		[],			# list
		{},			# dictionary
		(),			# tuple
		set()	]	# set

	for i in line:
		list_type.append(type(i).__name__)

	print(list_type)


if __name__ == '__main__':
	data_types()
