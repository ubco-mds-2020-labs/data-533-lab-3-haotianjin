import hospital.patient.patients as pt
class CovidPatient(pt.GeneralPatient):
    def __init__(self, name, age, date, height, weight, symptom):
        pt.GeneralPatient.__init__(self, name, age, date, height, weight, symptom)
        self.covid_test = True
    
    def display(self):
        if self.covid_test:
            return pt.GeneralPatient.display(self) + "\nTest result: positive"
        else:
            return pt.GeneralPatient.display(self) + "\nTest result: negative"
    
    def bmi(self):
        return pt.GeneralPatient.bmi(self)
        
    def full_recovered(self):
        if self.doc_approve == True and self.covid_test == False:
            return "Yes, this patient is ready to leave the hospital."
        else:
            return "No, this patient is not ready to leave the hospital."
        
    def addition_symptom(self, new_symp):
        return pt.GeneralPatient.addition_symptom(self,new_symp)
    
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
            return "This patient has been recorvered already, please check test result."
            
    def test_result(self, test):
        if test == 'negative':
            self.covid_test = False
            return "Test passed, please check condition to leave."
        elif test == 'positive':
            return "Test not passed"
        else:
            return "Please provide valid test input."
            
