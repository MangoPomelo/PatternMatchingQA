class Picker:
	def addItemsFromFile(self, filepath, item_array):
		with open(filepath, "r", encoding="utf-8") as file:
			for item in file:
				item_array.append(item.strip())

	def findItemsInSentence(self, item_array, sentence):
		item_found = []
		for item in item_array:
			if item in sentence:
				item_found.append(item)
		return item_found