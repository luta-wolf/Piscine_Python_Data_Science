from analytics import Research
from config import *


def main():
    try:
        research = Research(file_path)
        list_data = research.file_reader()
        count_observations = len(list_data)
        calculations = research.Calculations(list_data)
        counts = calculations.counts()
        fractions = calculations.fractions()

        predictions = research.Analytics(list_data)
        list_predicts = predictions.predict_random(num_of_steps)
        pred_heads, pred_tails = tuple(sum(elem) for elem in zip(*list_predicts))
        # list_predict_last = predictions.predict_last()
        content = template_text.format(
            count_observations,
            counts[0], counts[1],
            fractions[0], fractions[1],
            num_of_steps, pred_heads, pred_tails
        )

        predictions.save_file(content, out_file, extension)
    except (IOError, OSError, ValueError) as e:
        print(e)


if __name__ == '__main__':
    main()
