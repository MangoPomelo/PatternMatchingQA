from Picker import *

class RelationshipPicker(Picker):
	def __init__(self):
		self.cause_array = []
		self.complication_array = []
		self.cure_array = []
		self.deny_array = []
		self.department_array = []
		self.drug_array = []
		self.examination_array = []
		self.food_array = []
		self.lasttime_array = []
		self.preventability_array = []
		self.susceptibles_array = []
		self.symptom_array = []
		self.treatment_array = []
		self.treatment_possibility_array = []
		super().addItemsFromFile("./Relationship_dict/cause.txt", self.cause_array)
		super().addItemsFromFile("./Relationship_dict/complication.txt", self.complication_array)
		super().addItemsFromFile("./Relationship_dict/cure.txt", self.cure_array)
		super().addItemsFromFile("./Relationship_dict/lasttime.txt", self.lasttime_array)
		super().addItemsFromFile("./Relationship_dict/deny.txt", self.deny_array)
		super().addItemsFromFile("./Relationship_dict/department.txt", self.department_array)
		super().addItemsFromFile("./Relationship_dict/drug.txt", self.drug_array)
		super().addItemsFromFile("./Relationship_dict/examination.txt", self.examination_array)
		super().addItemsFromFile("./Relationship_dict/food.txt", self.food_array)
		super().addItemsFromFile("./Relationship_dict/preventability.txt", self.preventability_array)
		super().addItemsFromFile("./Relationship_dict/susceptibles.txt", self.susceptibles_array)
		super().addItemsFromFile("./Relationship_dict/symptom.txt", self.symptom_array)
		super().addItemsFromFile("./Relationship_dict/treatment.txt", self.treatment_array)
		super().addItemsFromFile("./Relationship_dict/treatment_possibility.txt", self.treatment_possibility_array)

	def pick(self, sentence):
		data = {}
		cause_found = super().findItemsInSentence(self.cause_array, sentence)
		complication_found = super().findItemsInSentence(self.complication_array, sentence)
		cure_found = super().findItemsInSentence(self.cure_array, sentence)
		lasttime_found = super().findItemsInSentence(self.lasttime_array, sentence)
		deny_found = super().findItemsInSentence(self.deny_array, sentence)
		department_found = super().findItemsInSentence(self.department_array, sentence)
		drug_found = super().findItemsInSentence(self.drug_array, sentence)
		examination_found = super().findItemsInSentence(self.examination_array, sentence)
		food_found = super().findItemsInSentence(self.food_array, sentence)
		preventability_found = super().findItemsInSentence(self.preventability_array, sentence)
		susceptibles_found = super().findItemsInSentence(self.susceptibles_array, sentence)
		symptom_found = super().findItemsInSentence(self.symptom_array, sentence)
		treatment_found = super().findItemsInSentence(self.treatment_array, sentence)
		treatment_possibility_found = super().findItemsInSentence(self.treatment_possibility_array, sentence)
		if len(cause_found) > 0:
			data['cause'] = cause_found
		if len(complication_found) > 0:
			data['complication'] = complication_found
		if len(cure_found) > 0:
			data['cure'] = cure_found
		if len(lasttime_found) > 0:
			data['lasttime'] = lasttime_found
		if len(department_found) > 0:
			data['department'] = department_found
		if len(drug_found) > 0:
			data['drug'] = drug_found
		if len(examination_found) > 0:
			data['examination'] = examination_found
		if len(food_found) > 0:
			if len(deny_found) > 0:
				data['bad_food'] = food_found
			else:
				data['good_food'] = food_found
		if len(preventability_found) > 0:
			data['preventability'] = preventability_found
		if len(susceptibles_found) > 0:
			data['susceptibles'] = susceptibles_found
		if len(symptom_found) > 0:
			data['symptom'] = symptom_found
		if len(treatment_found) > 0:
			data['treatment'] = treatment_found
		if len(treatment_possibility_found) > 0:
			data['treatment_possibility'] = treatment_possibility_found
		result = {'relationship' : data}
		return result



if __name__ == '__main__':
	rp = RelationshipPicker()
	result = rp.pick("感冒发烧流感该怎么治疗,其治疗痊愈机率是几成,挂什么科室,有什么症状,吃什么药好?")
	print(result)