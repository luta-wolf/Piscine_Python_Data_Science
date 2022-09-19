import sys
import os

class Research:
	def __init__(self, filename: str) -> None:
		self.filename = filename

	def file_reader(self):
		has_header = True
		line = self.check_file(has_header)
		return line

	def check_file(self, has_header) -> bool:
		if not os.access(self.filename, os.R_OK):
			raise ValueError("File can't be read")
		with open(self.filename, 'r') as infile:
			lines = [line.rstrip() for line in infile]
		if len(lines) < 1:
			raise ValueError("Few lines in file")
		if lines[0] == "0,1" or lines[0] == "1,0":
			has_header = False
		mod_lines = []
		if has_header:
			mod_lines = lines[1:]
		else:
			mod_lines = lines
		for line in mod_lines:
			if line != "0,1" and line != "1,0":
				raise ValueError("Data in the file is incorrect")
		res = []
		for line in mod_lines:
			strs = line.split(',')
			numbers = []
			for number in strs:
				numbers.append(int(number))
			res.append(list(numbers))
		return res

	class Calculations:
		def counts(self, data):
			eagle = 0
			for line in data:
				if line[0] == 1:
					eagle += 1
			tail = len(data) - eagle
			return eagle, tail

		def fractions(self, eagle, tail):
			perсent_eagles = eagle / (eagle + tail) * 100
			perсent_tails = tail / (eagle + tail) * 100
			return perсent_eagles, perсent_tails


def main(filename: str):
	research = Research(filename)
	print(research.file_reader())
	calc = research.Calculations()
	amount = calc.counts(research.file_reader())
	print(amount[0], amount[1])
	perсent = calc.fractions(amount[0], amount[1])
	print(perсent[0], perсent[1])


if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		raise ValueError("Wrong number agruments")
