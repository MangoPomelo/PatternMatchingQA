from Picker import *

class EntityPicker(Picker):
	def __init__(self):
		self.disease_array = []
		self.drug_array = []
		self.examination_array = []
		self.food_array = []
		self.sympton_array = []
		super().addItemsFromFile("./EntityDict/disease.txt", self.disease_array)
		super().addItemsFromFile("./EntityDict/drug.txt", self.drug_array)
		super().addItemsFromFile("./EntityDict/examination.txt", self.examination_array)
		super().addItemsFromFile("./EntityDict/food.txt", self.food_array)
		super().addItemsFromFile("./EntityDict/sympton.txt", self.sympton_array)

	def pick(self, sentence):
		data = {}
		disease_found = super().findItemsInSentence(self.disease_array, sentence)
		drug_found = super().findItemsInSentence(self.drug_array, sentence)
		examination_found = super().findItemsInSentence(self.examination_array, sentence)
		food_found = super().findItemsInSentence(self.food_array, sentence)
		sympton_found = super().findItemsInSentence(self.sympton_array, sentence)
		if len(disease_found) > 0:
			data['disease'] = disease_found
		if len(drug_found) > 0:
			data['drug'] = drug_found
		if len(examination_found) > 0:
			data['examination'] = examination_found
		if len(food_found) > 0:
			data['food'] = food_found
		if len(sympton_found) > 0:
			data['sympton'] = sympton_found
		result = {'entity' : data}
		return result



if __name__ == '__main__':
	ep = EntityPicker()
	result = ep.pick("感冒发烧流感能喝红豆银耳汤么")
	print(result)