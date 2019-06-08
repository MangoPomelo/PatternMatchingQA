class Parser:
	def parse(self, data):
		sql = []
		entity = data['entity_dict']
		question_types = data['question_types']
		for each_type in question_types:
			if each_type == 'disease_symptom':
				sql.extend(["MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
			elif each_type == 'symptom_disease':
				sql.extend(["MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('symptom')])
			elif each_type == 'disease_cause':
				sql.extend(["MATCH (m:Disease) where m.name = '{0}' return m.name, m.cause".format(i) for i in entity.get('disease')])
			elif each_type == 'disease_complication':
				sql.extend(["MATCH (m:Disease)-[r:acompany_with]->(n:Disease) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
				sql.extend(["MATCH (m:Disease)-[r:acompany_with]->(n:Disease) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
			elif each_type == 'disease_good_food':
				sql.extend(["MATCH (m:Disease)-[r:do_eat]->(n:Food) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
				sql.extend(["MATCH (m:Disease)-[r:recommand_eat]->(n:Food) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
			elif each_type == 'disease_bad_food':
				sql.extend(["MATCH (m:Disease)-[r:no_eat]->(n:Food) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
			elif each_type == 'good_food_disease':
				sql.extend(["MATCH (m:Disease)-[r:do_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('food')])
				sql.extend(["MATCH (m:Disease)-[r:recommand_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('food')])
			elif each_type == 'bad_food_disease':
				sql.extend(["MATCH (m:Disease)-[r:no_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('food')])
			elif each_type == 'disease_drug':
				sql.extend(["MATCH (m:Disease)-[r:common_drug]->(n:Drug) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
				sql.extend(["MATCH (m:Disease)-[r:recommand_drug]->(n:Drug) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
			elif each_type == 'drug_disease':
				sql.extend(["MATCH (m:Disease)-[r:common_drug]->(n:Drug) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('drug')])
				sql.extend(["MATCH (m:Disease)-[r:recommand_drug]->(n:Drug) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('drug')])
			elif each_type == 'disease_examination':
				sql.extend(["MATCH (m:Disease)-[r:need_check]->(n:Check) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('disease')])
			elif each_type == 'examination_disease':
				sql.extend(["MATCH (m:Disease)-[r:need_check]->(n:Check) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entity.get('examination')])
			elif each_type == 'disease_preventability':
				sql.extend(["MATCH (m:Disease) where m.name = '{0}' return m.name, m.prevent".format(i) for i in entity.get('disease')])
			elif each_type == 'disease_lasttime':
				sql.extend(["MATCH (m:Disease) where m.name = '{0}' return m.name, m.cure_lasttime".format(i) for i in entity.get('disease')])
			elif each_type == 'disease_treatment':
				sql.extend(["MATCH (m:Disease) where m.name = '{0}' return m.name, m.cure_way".format(i) for i in entity.get('disease')])
			elif each_type == 'disease_treatment_possibility':
				sql.extend(["MATCH (m:Disease) where m.name = '{0}' return m.name, m.cured_prob".format(i) for i in entity.get('disease')])
			elif each_type == 'disease_susceptibles':
				sql.extend(["MATCH (m:Disease) where m.name = '{0}' return m.name, m.easy_get".format(i) for i in entity.get('disease')])
		return sql