import sys

def letter_starter(email):
	with open("employees.tsv") as f1:
		lines = [line.rstrip() for line in f1]
	res = ""
	for line in lines:
		info = line.split('\t')
		if (email == info[2]):
			res = f"Dear {info[0]}, welcome to our team. We are sure that "
			res += "it will be a pleasure to work with you. "
			res += "That's a precondition for the professionals that our company hires."
	if not res:
		res = "No such email"
	print(res)

def main():
	if len(sys.argv) == 2:
		letter_starter(sys.argv[1])

if __name__ == '__main__':
	main()
