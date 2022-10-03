import re
import requests
import json
import pandas as pd

class NutritionFacts:
	"""
	Offering nutritional facts on given ingredients.

	Предоставление фактов o питательной ценности тех или иных ингредиентов.
	"""
	def __init__(self, list_of_ingredients):
		"""
		Put any fields here that you think you will need.

		Поместите сюда все поля, которые, по вашему мнению, вам понадобятся.
		"""
		# удаляем название программы, запятые, записывая ингредиенты в новый массив класса
		self.list_of_ingredients = list()
		for tmp in list_of_ingredients[1:]:
			self.list_of_ingredients.append(tmp.replace(',', ''))
		# print(self.list_of_ingredients)

	def retrieve(self):
		"""
		This method gets all the nutrient facts about the given ingredients from the file with pre-collected information. It returns any structure that you find useful.

		Этот метод получает все факты o питательных веществах заданных ингредиентов из файла c предварительно собранной информацией. Он возвращает любую структуру, которую вы считаете полезной.
		"""
		facts = list()

		for ingredient in self.list_of_ingredients:
			tmp = dict()
			res = requests.get(f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query={ingredient}').json()
			i = 0
			while True:
				try:
					tmp[res['foods'][0]['foodNutrients'][i]['nutrientName']] = res['foods'][0]['foodNutrients'][i]['value']
					i += 1
				except:
					break
			facts.append(tmp)

		# print(facts)

		return facts

	def filter(self, must_nutrients, facts):
		"""
		This method selects from the nutrient facts only nutrients from the list of must_nutrients (for example, from PDF-files below) and
		the top-n nutrients with the highest values of daily value norms for the given ingredient. It returns a text formatted as in the example above.

		Этот метод выбирает из фактов o питательных веществах только питательные вещества из списка must_nutrients (например, из PDF-файлов ниже) и
		топ-n питательных веществ c наибольшими значениями норм суточной ценности для данного ингредиента. Возвращается текст, отформатированный как в примере выше.
		"""

		df = pd.read_csv(must_nutrients)

		i = 0
		print("II. NUTRITION FACTS")
		while i < len(self.list_of_ingredients):
			print(self.list_of_ingredients[i].capitalize() + ":")
			if not facts[i]:
				print("...")
				i += 1
				continue
			j = 0
			while True:
				try:
					strForComparison_1 = str(df['Food Component'][j]).split()
					# print(strForComparison_1)
					for tmp in facts[i]:
						strForComparison_2 = str(tmp).split()
						# Сравнивем здесь .lower()
						compose = False
						c = 0
						while c < len(strForComparison_1):
							c1 = 0
							while c1 < len(strForComparison_2):
								if re.sub('[^a-z]', '', strForComparison_1[c].lower()) == re.sub('[^a-z]', '', strForComparison_2[c1].lower()) and re.sub('[^a-z]', '', strForComparison_1[c].lower()) != "total":
									compose = True
									break
								c1 += 1
							c += 1
						if compose == True:
							if round(float(facts[i][tmp]) / float(df['Adults'][j]) * 100) != 0: #ориентрироваться по ...
								print(f"{df['Food Component'][j]} - {round(float(facts[i][tmp]) / float(df['Adults'][j]) * 100)}% of Daily Value")
							break
						# print(strForComparison_2)
					j += 1
					# break #
				except:
					break
			i += 1
			# break #

		# return text_with_facts



# python3 nutritionist.py milk, honey, jam