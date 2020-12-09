class GeneralPatient:
    def __init__(self, name, age, date, height, weight, symptom):
        self.name = name
        self.age = age
        self.date = date
        self.height = height
        self.weight = weight
        if type(symptom) == list:
            self.symptom = symptom
        elif type(symptom) == str:
            self.symptom = [symptom]
        else:
            return "Please enter valid symptoms as list or string."
        self.doc_approve = False
    
    def display(self):
        return "Patient name: {}\nPatient age: {}\nIn hospital date: {}\nSymptoms: {}".format(self.name,
                      self.age,
                      self.date,
                      self.symptom)
    
    def bmi(self):
        return "Patient BMI is {}".format(self.weight/(self.height**2))
        
    def full_recovered(self):
        if self.doc_approve == True:
            return "Yes, this patient is ready to leave the hospital."
        else:
            return "No, this patient is not ready to leave the hospital."
        
    def addition_symptom(self, new_symptoms):
        if type(new_symptoms) == list:
            for i in new_symptoms:
                self.symptom.append(i)
        elif type(new_symptoms) == str:
            self.symptom.append(new_symptoms)
        else:
            return "Please enter valid symptoms as list or string."
    
    def recovered_symptom(self, rec_symptoms):
        if type(rec_symptoms) == list:
            for i in rec_symptoms:
                if i in self.symptom:
                    self.symptom.remove(i)
                else:
                    return "Symptom {} is not in the list, please provide correct information.".format(i)
        elif type(rec_symptoms) == str:
            if rec_symptoms in self.symptom:
                    self.symptom.remove(rec_symptoms)
            else:
                return "This symptom is not in the list, please provide correct information."
        else:
            return "Please enter valid symptoms as list or string."
        if not self.symptom:
            self.doc_approve = True
            return "This patient has been recorvered already, please check condition to leave."
            

            
            
