import unittest
import hospital.patient.patients as p
class TestPatients(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start testing in general patients.")

    def setUp(self):
        self.p1 = p.GeneralPatient("Emma Jones", 25, "11/23/2020",1.66, 60, ['vomit'])

    def test_1(self):
        bmi = 60/1.66**2
        self.assertEqual(self.p1.name, "Emma Jones")
        self.assertEqual(self.p1.doc_approve, False)
        self.assertEqual(self.p1.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.assertEqual(self.p1.bmi(), "Patient BMI is {}".format(bmi))
        self.assertEqual(self.p1.display(), 
                         "Patient name: Emma Jones\nPatient age: 25\nIn hospital date: 11/23/2020\nSymptoms: ['vomit']")
        
    def test_2(self):
        self.p1.addition_symptom(['back pain', 'headache'])
        self.assertEqual(self.p1.symptom, ['vomit', 'back pain', 'headache'])
        self.assertEqual(self.p1.addition_symptom(2), "Please enter valid symptoms as list or string.")
        self.p1.addition_symptom('cough')
        self.assertEqual(self.p1.symptom, ['vomit', 'back pain', 'headache', 'cough'])
        self.assertEqual(self.p1.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.p1.recovered_symptom(['back pain', 'headache', 'cough'])
        self.assertEqual(self.p1.symptom, ['vomit'])
        self.assertEqual(self.p1.recovered_symptom('headache'), 
                         "This symptom is not in the list, please provide correct information.")
        self.assertEqual(self.p1.recovered_symptom('vomit'),
                         "This patient has been recorvered already, please check condition to leave.")
        self.assertEqual(self.p1.doc_approve, True)
        self.assertEqual(self.p1.full_recovered(), "Yes, this patient is ready to leave the hospital.")
        
    def tearDown(self):
        self.p1 = None

    @classmethod
    def tearDownClass(cls):
        print("Finish tests in general patients.")


