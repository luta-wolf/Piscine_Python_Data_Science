#!python3
import os

def main():
	print(os.environ['VIRTUAL_ENV'])
	try:
		if not os.environ['VIRTUAL_ENV'].endswith('einterdi'):
			raise Exception('Incorrect env')
	except Exception as ex:
		print(ex)
	else:
		os.system('pip install beautifulsoup4 PyTest requests > /dev/null')
		os.system('pip freeze; pip freeze > requirements.txt')

if __name__ == '__main__':
	main()
