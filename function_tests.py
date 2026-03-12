import unittest
import functions
import class_defs
from build_data import getCPstudents
from class_defs import SurveySubmission

class TestCase(unittest.TestCase):

#Sophia
    def test_filter_by_ethnicity(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                           "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                           "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                           "College of Engineering (CENG)", 1.1)]
        key = "White"
        expected = [SurveySubmission("Woman", "White", "First year undergraduate student",
                                           "Bailey College of Science and Mathematics (COSAM)", 0.5)]
        result = functions.filter_by_ethnicity(lst, key)
        self.assertEqual(result,expected)

#Ava
    def test_filter_by_ethnicity2(self):
        lst=[SurveySubmission("Woman","Hispanic/Latinx","First year undergraduate student","Orfalea College of Business (OCOB)",1),
             SurveySubmission("Woman","Asian","First year undergraduate student","College of Engineering (CENG)",1),
             SurveySubmission("Woman","Hispanic/Latinx","First year undergraduate student","College of Engineering (CENG)",0.85)]
        key = "Hispanic/Latinx"
        expected=[SurveySubmission("Woman","Hispanic/Latinx","First year undergraduate student","Orfalea College of Business (OCOB)",1),
                  SurveySubmission("Woman","Hispanic/Latinx","First year undergraduate student","College of Engineering (CENG)",0.85)]
        result = functions.filter_by_ethnicity(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_filter_by_ethnicity_empty_lst(self):
        lst = []
        key = "Hispanic/Latinx"
        expected = []
        result = functions.filter_by_ethnicity(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_filter_by_ethnicity_wrong_key(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                           "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                           "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                           "College of Engineering (CENG)", 1.1)]
        key = "123"
        expected = []
        result = functions.filter_by_ethnicity(lst, key)
        self.assertEqual(result,expected)


#Sophia
    def test_filter_by_gender(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                           "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                           "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                           "College of Engineering (CENG)", 1.1)]
        key = "Woman"
        expected = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                           "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                           "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                           "College of Engineering (CENG)", 1.1)]
        result = functions.filter_by_gender(lst, key)
        self.assertEqual(result,expected)


#Ava
    def test_filter_by_gender2(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "Orfalea College of Business (OCOB)", 1),
               SurveySubmission("Woman", "Asian", "First year undergraduate student", "College of Engineering (CENG)", 1),
               SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Engineering (CENG)", 0.85)]
        key = "Man"
        expected = []
        result = functions.filter_by_gender(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_filter_by_major(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                           "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                           "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                           "College of Engineering (CENG)", 1.1)]
        key = "College of Engineering (CENG)"
        expected =[SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                           "College of Engineering (CENG)", 1.1)]
        result = functions.filter_by_major(lst, key)
        self.assertEqual(result,expected)

#Ava
    def test_filter_by_major2(self):
        lst=[SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "Orfalea College of Business (OCOB)", 1),
               SurveySubmission("Woman", "Asian", "First year undergraduate student", "College of Engineering (CENG)", 1),
               SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Engineering (CENG)", 0.85)]
        key = "Orfalea College of Business (OCOB)"
        expected = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "Orfalea College of Business (OCOB)", 1)]
        result = functions.filter_by_major(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_filter_by_grade(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                           "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                           "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                           "College of Engineering (CENG)", 1.1)]
        key = "Second year undergraduate student"
        expected = []
        result = functions.filter_by_grade(lst, key)
        self.assertEqual(result,expected)


#Ava
    def test_filter_by_grade2(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "Third year undergraduate student",
                                "Orfalea College of Business (OCOB)", 1),
               SurveySubmission("Woman", "Asian", "First year undergraduate student", "College of Engineering (CENG)", 1),
               SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Engineering (CENG)", 0.85)]
        key = "Third year undergraduate student"
        result = functions.filter_by_grade(lst, key)
        expected = [SurveySubmission("Woman", "Hispanic/Latinx", "Third year undergraduate student",
                          "Orfalea College of Business (OCOB)", 1)]
        self.assertEqual(result,expected)

#Sophia
    def test_mean(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student", "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student", "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student", "College of Engineering (CENG)", 1.1)]
        key = "Woman"
        expected = 0.5
        result = functions.get_mean(lst, key)
        self.assertEqual(result, expected)

#Ava
    def test_mean2(self):
        lst=[SurveySubmission("Woman","Hispanic/Latinx","First year undergraduate student","Orfalea College of Business (OCOB)",1),
             SurveySubmission("Woman","Asian","First year undergraduate student","College of Engineering (CENG)",1),
             SurveySubmission("Woman","Hispanic/Latinx","First year undergraduate student","College of Engineering (CENG)",0.85)]
        key = "First year undergraduate student"
        expected = 0.95
        result = functions.get_mean(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_mean_empty_lst(self):
        lst = []
        key = "First year undergraduate student"
        # divide by 0 error because list is of length 0
        expected = None
        result = functions.get_mean(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_mean_wrong_key(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student", "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student", "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student", "College of Engineering (CENG)", 1.1)]
        key = "123"
        expected = None
        result = functions.get_mean(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_sd(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student", "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student", "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student", "College of Engineering (CENG)", 1.1)]
        key =  "Woman"
        expected =  0.6
        result = functions.get_sd(lst, key)
        self.assertEqual(result,expected)

#Ava
    def test_sd2(self):
        lst=[SurveySubmission("Woman","Hispanic/Latinx","First year undergraduate student","Orfalea College of Business (OCOB)",1),
             SurveySubmission("Woman","Asian","First year undergraduate student","College of Engineering (CENG)",1),
             SurveySubmission("Woman","Hispanic/Latinx","First year undergraduate student","College of Engineering (CENG)",0.85)]
        key = "First year undergraduate student"
        expected = 0.09
        result = functions.get_sd(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_sd_empty_lst(self):
        lst = []
        key = "First year undergraduate student"
        expected = None
        result = functions.get_sd(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_sd_wrong_key(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                "College of Engineering (CENG)", 1.1)]
        key = "123"
        expected = None
        result = functions.get_sd(lst, key)
        self.assertEqual(result,expected)

#Sophia
    def test_get_Statdata(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student", "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student", "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student", "College of Engineering (CENG)", 1.1)]
        key = "Woman"
        expected = class_defs.StatVar(0.5, 0.6, 3)
        result = functions.get_Statdata(lst, key)
        self.assertEqual(result,expected)

#Ava
    def test_get_Statdata2(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "Orfalea College of Business (OCOB)", 1),
               SurveySubmission("Woman", "Asian", "First year undergraduate student", "College of Engineering (CENG)", 1),
               SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Engineering (CENG)", 0.85)]
        key = "First year undergraduate student"
        expected= class_defs.StatVar(0.95, 0.09, 3)
        result = functions.get_Statdata(lst,key)
        self.assertEqual(expected,result)

#Sophia
    def test_get_Statdata_empty_lst(self):
        lst = []
        key = "First year undergraduate student"
        expected = None
        self.assertEqual(functions.get_Statdata(lst,key),expected)

#Sophia
    def test_get_Statdata_wrong_key(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                "College of Engineering (CENG)", 1.1)]
        key = "123"
        expected = None
        self.assertEqual(functions.get_Statdata(lst,key),expected)

#Sophia
#This test is simply a testcase with an example list of SurveySubmission objects, and will not provide data we are interested in.
    def test_compare_mean(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                "College of Engineering (CENG)", 1.1)]
        obj1 = "Hispanic/Latinx"
        obj2 = "White"
        expected = 0.5
        result = functions.compare_mean(obj1, obj2, lst)
        self.assertEqual(result,expected)

#Sophia
    def test_compare_mean_empty_lst(self):
        lst = []
        obj1 = "Hispanic/Latinx"
        obj2 = "White"
        expected = None
        result = functions.compare_mean(obj1, obj2, lst)
        self.assertEqual(result,expected)

#Sophia
    def test_compare_mean_wrong_obj(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                "College of Engineering (CENG)", 1.1)]
        obj1 = "Sophia"
        obj2 = "Woman"
        expected = None
        self.assertEqual(functions.compare_mean(obj1, obj2, lst),expected)

#Sophia
#This test will compare the mean math attitudes of Cal Poly boys versus Cal Poly girls using our survey's findings.
    def test_compare_mean_CPboys_vs_CPgirls(self):
        lst = getCPstudents()
        obj1 = "Man"
        obj2 = "Woman"
        expected = 0.38
        result = functions.compare_mean(obj1, obj2, lst)
        # function will print "Man's mean math attitude is greater than Woman's mean math attitude, 0.38 > 0.16"
        self.assertEqual(result,expected)

#Ava
#This test will compare the mean math attitudes of CLA students and CENG students using our survey's findings.
    def test_compare_mean_CLA_vs_CENG(self):
        lst = getCPstudents()
        obj1 = "College of Liberal Arts (CLA)"
        obj2 = "College of Engineering (CENG)"
        expected = 0.33
        result = functions.compare_mean(obj1, obj2, lst)
        # function will print "College of Engineering (CENG)'s mean math attitude is greater than College of Liberal Arts (CLA)'s mean math attitude, 0.33 > -0.29"
        self.assertEqual(expected,result)

#Sophia
#This test is simply a testcase with an example list of SurveySubmission objects, and will not provide data we are interested in.
    def test_compare_sd(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                "College of Engineering (CENG)", 1.1)]
        obj1 = "Hispanic/Latinx"
        obj2 = "White"
        expected = 0.85
        result = functions.compare_sd(obj1, obj2, lst)
        self.assertEqual(result,expected)

#Sophia
    def test_compare_sd_empty_lst(self):
        lst = []
        obj1 = "Hispanic/Latinx"
        obj2 = "White"
        expected = None
        result = functions.compare_sd(obj1, obj2, lst)
        self.assertEqual(result,expected)

#Sophia
    def test_compare_sd_wrong_obj(self):
        lst = [SurveySubmission("Woman", "Hispanic/Latinx", "First year undergraduate student",
                                "College of Liberal Arts (CLA)", -0.1),
               SurveySubmission("Woman", "White", "First year undergraduate student",
                                "Bailey College of Science and Mathematics (COSAM)", 0.5),
               SurveySubmission("Woman", "Hispanic/Latinx", "Fourth year undergraduate student",
                                "College of Engineering (CENG)", 1.1)]
        obj1 = "Sophia"
        obj2 = "Woman"
        expected = None
        self.assertEqual(functions.compare_sd(obj1, obj2, lst),expected)

#Ava
#This test will compare the standard deviation math attitudes of Asian Cal Poly students versus Hispanic/Latinx Cal Poly students using our survey's findings.
    def test_compare_sd_asian_vs_hispanics(self):
        lst=getCPstudents()
        obj1 = "Asian"
        obj2 = "Hispanic/Latinx"
        expected = 0.4
        result = functions.compare_sd(obj1,obj2,lst)
        # function will print "Asian 's standard deviation math attitude is greater than  Hispanic/Latinx 's standard deviation math attitude,  0.4  >  0.37"
        self.assertEqual(expected,result)

#Ava
#This test will compare the standard deviation math attitudes of fifth grade girls versus female Cal Poly students using the Journal of Child Development study alongside our survey's findings.
    def test_compare_sd_grade5_vs_cp(self):
        lst = getCPstudents()
        obj1 = "Grade 5 Girls"
        obj2 = "Woman"
        expected = 0.4
        result = functions.compare_sd(obj1,obj2,lst)
        # function will print "Woman 's standard deviation math attitude is greater than  Grade 5 Girls 's standard deviation math attitude,  0.4  >  -0.17"
        self.assertEqual(expected,result)




