def read_and_write(file):

	in_file = open(file, 'r')
	text = in_file.read() \
		.replace("\",", "\"\t") \
		.replace(",\"", "\t\"") \
		.replace("true,", "true\t") \
        .replace("false,", "false\t")
	out_file = open("ds.tsv", "w")
	out_file.write(text)
	in_file.close()
	out_file.close()


def main():
	read_and_write("ds.csv")


if __name__ == '__main__':
	main()
