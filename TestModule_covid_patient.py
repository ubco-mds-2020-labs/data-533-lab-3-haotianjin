import unittest
import hospital.patient.covid_patient as cp

class TestCovidPatients(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start testing in covid-19 patients.")

    def setUp(self):
        self.p3 = cp.CovidPatient("Joe Mason", 43, "12/01/2020", 1.90, 100, "fever")
        
    def test_1(self):
        bmi = 100/1.90**2
        self.assertEqual(self.p3.name, "Joe Mason")
        self.assertEqual(self.p3.symptom, ['fever'])
        self.assertEqual(self.p3.doc_approve, False)
        self.assertEqual(self.p3.covid_test, True)
        self.assertEqual(self.p3.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.assertEqual(self.p3.bmi(), "Patient BMI is {}".format(bmi))
        self.assertEqual(self.p3.display(), 
                         "Patient name: Joe Mason\nPatient age: 43\nIn hospital date: 12/01/2020\nSymptoms: ['fever']\nTest result: positive")
        
    def test_2(self):
        self.p3.addition_symptom(['back pain', 'headache'])
        self.assertEqual(self.p3.symptom, ['fever', 'back pain', 'headache'])
        self.assertEqual(self.p3.addition_symptom(2), "Please enter valid symptoms as list or string.")
        self.p3.addition_symptom('cough')
        self.assertEqual(self.p3.symptom, ['fever', 'back pain', 'headache', 'cough'])
        self.assertEqual(self.p3.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.p3.recovered_symptom(['back pain', 'headache', 'cough'])
        self.assertEqual(self.p3.symptom, ['fever'])
        self.assertEqual(self.p3.recovered_symptom('headache'), 
                         "This symptom is not in the list, please provide correct information.")
        self.assertEqual(self.p3.recovered_symptom('fever'),
                         "This patient has been recorvered already, please check test result.")
        self.assertEqual(self.p3.doc_approve, True)
        self.assertEqual(self.p3.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.assertEqual(self.p3.test_result('positive'), "Test not passed")
        self.assertEqual(self.p3.test_result(2), "Please provide valid test input.")
        self.assertEqual(self.p3.test_result('negative'), "Test passed, please check condition to leave.")
        self.assertEqual(self.p3.full_recovered(), "Yes, this patient is ready to leave the hospital.")
        
    def tearDown(self):
        self.p3 = None

    @classmethod
    def tearDownClass(cls):
        print("Finish tests in covid-19 patients.")

