import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
import random

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn import metrics, svm, linear_model, tree, ensemble

import pickle
class Forecast:
	"""
	Predicting the rating or the class

	Прогнозирование рейтинга или класса
	"""
	def __init__(self, list_of_ingredients):
		"""
		Put any fields here that you think you will need.

		Поместите сюда все поля, которые, по вашему мнению, вам понадобятся.
		"""
		self.df = pd.read_csv(list_of_ingredients, index_col='alabama')
		self.df.pop('title')
		self.df.pop('calories')
		self.df.pop('protein')
		self.df.pop('fat')
		self.df.pop('sodium')
		self.df.pop('#cakeweek')
		self.df.pop('#wasteless')
		self.df.pop('22-minute meals')
		self.df.pop('3-ingredient recipes')
		self.df.pop('30 days of groceries')
		self.df.pop('advance prep required')

		X = self.df.drop(columns='rating')
		y = self.df['rating']


		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21, stratify=y)
		# print(y_train.value_counts() / y_train.shape[0] - y_test.value_counts() / y_test.shape[0])

		def cross_validation_test(model, split_n=10):
			kf = StratifiedKFold(split_n)
			X = X_train.values
			y = y_train.values

			for train, test in kf.split(X, y):
				model.fit(X[train], y[train])

				train_accuracy = metrics.accuracy_score(model.predict(X[train]), y[train])
				test_accuracy = metrics.accuracy_score(model.predict(X[test]), y[test])

				print(f'train -  {train_accuracy:1.5f}  |  valid -  {test_accuracy:1.5f}')

			accuracy_values = cross_val_score(model, X, y, cv=kf, n_jobs=-1)
			print(f'Average accuracy on crossval is {accuracy_values.mean():1.5f}')
			print(f'Std is {accuracy_values.std():1.5f}\n')

		logreg = linear_model.LogisticRegression(random_state=21, fit_intercept=False)
		# cross_validation_test(logreg, 10)

		# print(X)
		# print(y)
		# print(self.df)
		print("I. OUR FORECAST")
		asd = random.randint(0, 1)
		if asd == 0:
			print("You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients.")
		else:
			print("Healthy Food")

	def preprocess(self):
		"""
		This method transforms the list of ingredients to the data structure that is used in machine learning algorithms for predictions.

		Этот метод преобразует список ингредиентов в структуру данных, которая используется в алгоритмах машинного обучения для прогнозирования.
		"""
		# return vector
		
	def predict_rating(self):
		"""
		This method returns the rating for the list of ingredients using the regression model that you trained upfront.
		Besides the rating itself, the method returns a text that interprets the rating and gives a recommendation as in the example above.

		Этот метод возвращает рейтинг для списка ингредиентов, используя регрессионную модель, которую вы предварительно обучили.
		Кроме самого рейтинга, метод возвращает текст, который интерпретирует рейтинг и дает рекомендацию, как в примере выше.
		"""
		# return rating, text
		
	def predict_rating_category(self):
		"""
		This method returns the rating category for the list of ingredients using the classification model that you trained upfront.
		Besides the rating itself, the method returns a text that interprets the rating category and gives a recommendation as in the example above.

		Этот метод возвращает категорию рейтинга для списка ингредиентов, используя модель классификации, которую вы обучили заранее.
		Кроме самого рейтинга, метод возвращает текст, который интерпретирует категорию рейтинга и дает рекомендацию, как в примере выше.
		"""
		# return rating_cat, text

# python3 nutritionist.py milk, honey, jam