import sys
import os

class Research:
	def __init__(self, filename):
		self.filename = filename

	def file_reader(self):
		line = self.check_file()
		return line

	def check_file(self):
		if not os.access(self.filename, os.R_OK):
			raise ValueError("File can't be read")
		with open(self.filename, 'r') as infile:
			lines = [line.rstrip() for line in infile]
		if len(lines) < 2:
			raise ValueError("Few lines in file")
		if len(lines[0].split(',')) != 2:
			raise ValueError("Header is incorrect")
		for line in lines[1:]:
			if line != "0,1" and line != "1,0":
				raise ValueError("Data in the file is incorrect")
		return "\n".join(lines)


if __name__ == "__main__":
	if len(sys.argv) == 2:
		research = Research(sys.argv[1])
		print(research.file_reader())
	else:
		raise ValueError("Wrong number agruments")



