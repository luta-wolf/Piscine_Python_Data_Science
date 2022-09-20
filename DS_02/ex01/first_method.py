class Research:
	def file_reader(self):
		with open("data.csv", "r") as infile:
			return infile.read()

def main():
	researcher = Research()
	print(researcher.file_reader())

if __name__ == "__main__":
	main()
