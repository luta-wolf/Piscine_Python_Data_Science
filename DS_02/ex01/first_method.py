class Research:
	def file_reader(self):
		infile = open("data.csv", "r")
		return infile.read()

def main():
	researcher = Research()
	print(researcher.file_reader())

if __name__ == "__main__":
	main()
