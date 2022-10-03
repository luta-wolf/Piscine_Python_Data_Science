import sys
from NutritionFacts import NutritionFacts
from Forecast import Forecast
from SimilarRecipes import SimilarRecipes

if __name__ == '__main__':

	if len(sys.argv) > 1:
		# 1
		forecast = Forecast('data/epi_r.csv')
		# 2
		nutrFacts = NutritionFacts(sys.argv)
		tmp = nutrFacts.retrieve()
		tmp = [{'Protein': 3.39, 'Total lipid (fat)': 2.12, 'Carbohydrate, by difference': 5.08, 'Energy': 55.0, 'Sugars, total including NLEA': 5.08, 'Fiber, total dietary': 0.0, 'Calcium, Ca': 127, 'Iron, Fe': 0.0, 'Sodium, Na': 55.0, 'Vitamin A, IU': 212, 'Vitamin D (D2 + D3), International Units': 42.0, 'Vitamin C, total ascorbic acid': 1.0, 'Cholesterol': 8.0, 'Fatty acids, total trans': 0.0, 'Fatty acids, total saturated': 1.27}, {'Folic acid': 0.0, 'SFA 4:0': 0.0, 'SFA 6:0': 0.0, 'SFA 10:0': 0.0, 'SFA 16:0': 0.0, 'SFA 18:0': 0.0, 'MUFA 18:1': 0.0, 'PUFA 18:2': 0.0, 'PUFA 18:3': 0.0, 'PUFA 20:4': 0.0, 'PUFA 18:4': 0.0, 'MUFA 20:1': 0.0, 'MUFA 22:1': 0.0, 'SFA 8:0': 0.0, 'SFA 12:0': 0.0, 'SFA 14:0': 0.0, 'PUFA 22:6 n-3 (DHA)': 0.0, 'MUFA 16:1': 0.0, 'PUFA 20:5 n-3 (EPA)': 0.0, 'PUFA 22:5 n-3 (DPA)': 0.0, 'Vitamin D (D2 + D3), International Units': 0.0, 'Fatty acids, total monounsaturated': 0.0, 'Fatty acids, total polyunsaturated': 0.0, 'Alcohol, ethyl': 0.0, 'Fatty acids, total saturated': 0.0, 'Carotene, beta': 0.0, 'Carotene, alpha': 0.0, 'Cryptoxanthin, beta': 0.0, 'Lycopene': 0.0, 'Lutein + zeaxanthin': 0.0, 'Vitamin E (alpha-tocopherol)': 0.0, 'Retinol': 0.0, 'Protein': 0.3, 'Ash': 0.2, 'Fiber, total dietary': 0.2, 'Iron, Fe': 0.42, 'Magnesium, Mg': 2.0, 'Phosphorus, P': 4.0, 'Sodium, Na': 4.0, 'Copper, Cu': 0.036, 'Manganese, Mn': 0.08, 'Vitamin A, IU': 0.0, 'Vitamin C, total ascorbic acid': 0.5, 'Thiamin': 0.0, 'Riboflavin': 0.038, 'Folate, total': 2.0, 'Vitamin B-12': 0.0, 'Tryptophan': 0.004, 'Threonine': 0.004, 'Methionine': 0.001, 'Phenylalanine': 0.011, 'Tyrosine': 0.008, 'Alanine': 0.006, 'Glutamic acid': 0.018, 'Glycine': 0.007, 'Proline': 0.09, 'Cholesterol': 0.0, 'Total lipid (fat)': 0.0, 'Carbohydrate, by difference': 82.4, 'Energy': 1270.0, 'Water': 17.1, 'Calcium, Ca': 6.0, 'Potassium, K': 52.0, 'Zinc, Zn': 0.22, 'Niacin': 0.121, 'Pantothenic acid': 0.068, 'Vitamin B-6': 0.024, 'Isoleucine': 0.008, 'Leucine': 0.01, 'Lysine': 0.008, 'Cystine': 0.003, 'Valine': 0.009, 'Arginine': 0.005, 'Histidine': 0.001, 'Aspartic acid': 0.027, 'Serine': 0.006, 'Vitamin B-12, added': 0.0, 'Vitamin E, added': 0.0, 'Caffeine': 0.0, 'Theobromine': 0.0, 'Sugars, total including NLEA': 82.1, 'Sucrose': 0.89, 'Glucose': 35.8, 'Maltose': 1.44, 'Vitamin K (phylloquinone)': 0.0, 'Galactose': 3.1, 'Fructose': 40.9, 'Vitamin D (D2 + D3)': 0.0, 'Selenium, Se': 0.8, 'Vitamin A, RAE': 0.0, 'Folate, food': 2.0, 'Fluoride, F': 7.0, 'Folate, DFE': 2.0, 'Betaine': 1.7, 'Choline, total': 2.2}, {}]
		nutrFacts.filter('data/DRVs.csv', tmp)
		# 3
		line = ""
		for i in range(1, len(sys.argv)):
			line += sys.argv[i] + '%20'
		line = line[:-3]
		SimilarRecipes.parse(line)

	else:
		raise ValueError("Too few arguments")

# python3 nutritionist.py milk, honey
