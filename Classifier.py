from EntityPicker import *
from RelationshipPicker import *

class Classifier:
	def __init__(self):
		self.e_picker = EntityPicker()
		self.r_picker = RelationshipPicker()

	def classify(self, sentence):
		question_types = []
		relationship = self.r_picker.pick(sentence)['relationship']
		entity = self.e_picker.pick(sentence)['entity']
		
		if 'disease' in entity and 'symptom' in relationship:
			question_types.append('disease_symptom')
		if 'symptom' in entity and 'symptom' in relationship:
			question_types.append('symptom_disease')

		if 'disease' in entity and 'cause' in relationship:
			question_types.append('disease_cause')

		if 'disease' in entity and 'complication' in relationship:
			question_types.append('disease_complication')

		if 'disease' in entity and 'good_food' in relationship:
			question_types.append('disease_good_food')
		if 'disease' in entity and 'bad_food' in relationship:
			question_types.append('disease_bad_food')

		if 'food' in entity and 'good_food' in relationship and 'cure' in relationship:
			question_types.append('good_food_disease')
		if 'food' in entity and 'bad_food' in relationship and 'cure' in relationship:
			question_types.append('bad_food_disease')

		if 'disease' in entity and 'drug' in relationship:
			question_types.append('disease_drug')
		if 'drug' in entity and 'cure' in relationship:
			question_types.append('drug_disease')

		if 'disease' in entity and 'examination' in relationship:
			question_types.append('disease_examination')
		if 'examination' in entity and 'examination' in relationship and 'cure' in relationship:
			question_types.append('examination_disease')

		if 'disease' in entity and 'preventability' in relationship:
			question_types.append('disease_preventability')

		if 'disease' in entity and 'lasttime' in relationship:
			question_types.append('disease_lasttime')

		if 'disease' in entity and 'treatment' in relationship:
			question_types.append('disease_treatment')

		if 'disease' in entity and 'treatment_possibility' in relationship:
			question_types.append('disease_treatment_possibility')

		if 'disease' in entity and 'susceptibles' in relationship:
			question_types.append('disease_susceptibles')

		data = {'question_types' : question_types, 'entity_dict' : entity}
		return data



if __name__ == '__main__':
	classifier = Classifier()
	classifier.classify("感冒发烧流感该怎么治疗,其治疗痊愈机率是几成,挂什么科室,有什么症状,吃什么药好?")
	classifier.classify("感冒的症状有哪些?")
	classifier.classify("金刚烷胺治什么,感冒多久能好")
	classifier.classify("感冒怎么检查,X光治疗什么,易感人群是什么")