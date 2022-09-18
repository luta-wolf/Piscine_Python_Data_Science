import sys

def dataset():
	clients = [
		'andrew@gmail.com',	'jessica@gmail.com',
		'ted@mosby.com',	'john@snow.is',
		'bill_gates@live.com',	'mark@facebook.com',
		'elon@paypal.com',	'jessica@gmail.com'
		]
	participants = [
		'walter@heisenberg.com',	'vasily@mail.ru',
		'pinkman@yo.org',	'jessica@gmail.com',
		'elon@paypal.com',	'pinkman@yo.org',
		'mr@robot.gov',	'eleven@yahoo.com'
		]
	recipients = [
		'andrew@gmail.com',	'jessica@gmail.com',
		'john@snow.is'
		]
	return set(clients), set(participants), set(recipients)

def marketing(argv):
	clients, participants, recipients = dataset()
	if argv == "call_center":
		return  list((clients | participants) - recipients)
	elif argv == "potential_clients":
		return list(participants  - clients)
	elif argv == "loyalty_program":
		return list(clients - participants)
	else:
		return "Wrong argument."


def main():
	if len(sys.argv) == 2:
		print(marketing(sys.argv[1]))

if __name__ == "__main__":
	main()
