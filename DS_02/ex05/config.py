def parameters():
	file = "data.csv"
	num_of_steps = 3
	return file, num_of_steps


def report(observation, frac_check, num_of_steps, forecast):
	res = f"""
	Report
	We have made {observation[0] + observation[1]} observations from tossing a coin: {observation[0]} of them were tails and {observation[1]} of
	them were heads. The probabilities are {frac_check[0]:0.2f}\% and {frac_check[1]:0.2f}\%, respectively. Our
	forecast is that in the next {num_of_steps} observations we will have: {forecast[0]} tail and {forecast[1]} heads."""
	return res
