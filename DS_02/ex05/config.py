def parameters():
    file = "data.csv"
    num_of_steps = 3
    return file, num_of_steps

def report(observation, frac_check, num_of_steps, forecast):
    res = "Report\n"
    res += "We have made %d observations from tossing a coin: " \
        % (observation[0] + observation[1])
    res += "%d of them were tails and %d of them were heads. " \
        % (observation[0], observation[1])
    res += "The probabilities are %0.2f%% and %0.2f%%, respectively. " \
        % (frac_check[0], frac_check[1])
    res += "Our forecast is that in the next %d observations " % num_of_steps
    res += "we will have: %d tail and %d heads." \
        % (forecast[0], forecast[1])
    return res
