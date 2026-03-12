import unittest
import build_data

class TestCase(unittest.TestCase):

# Ava
    def test_attitude_calc(self):
        q1="True"
        q2="True"
        q3="True"
        q4="True"
        q5="False"
        q6="True"
        q7="False"
        q8="True"
        q9="True"
        q10="False"
        q11="True"
        expected = 0.14
        result = build_data.attitude_calc(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11)
        self.assertEqual(result,expected)

# Sophia
    def test_attitude_calc2(self):
        q1="True"
        q2="True"
        q3="True"
        q4="True"
        q5="True"
        q6="True"
        q7="True"
        q8="True"
        q9="True"
        q10="True"
        q11="True"
        expected = 0.41
        result = build_data.attitude_calc(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11)
        self.assertEqual(result,expected)
