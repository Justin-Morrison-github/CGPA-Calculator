import unittest
from colorama import Fore
from Course import Course, Term
from CourseList import CourseList
from parameterized import parameterized


class TestCourseList(unittest.TestCase):
    def setUp(self):
        self.course_dict = {
            "Year": 2023, "Term": "Fall", "CRN": 30960, "Subject": "CHEM", "Number": 1101, "Section": "B",
            "Name": "Chemistry", "Grade": "A+", "Credit": 0.500, "CGPA Points": 6.00, "Major": "True"}
        self.course = Course(self.course_dict)
        self.course_list = CourseList([self.course])

    @parameterized.expand([
        ("courses", []),
        ("names", None),
        ("subjects", None),
        ("sections", None),
        ("years", None),
        ("CRNs", None),
        ("course_numbers", None),
        ("credits", None),
        ("CGPA_points", None),
        ("terms", None),
        ("grades", None),
        ("in_major", None),
        ("total_credits", None),
        ("total_grade_points_earned", None),
        ("major_credits", None),
        ("major_grade_points_earned", None),

    ])
    def test_init_empty_CourseList(self, attr_name, expected_value):
        course_list = CourseList()
        actual_value = course_list.__getattribute__(attr_name)
        self.assertEqual(actual_value, expected_value)

    def test_len(self):
        self.assertEqual(self.course_list.len(), 1)

    def test_dunder_len(self):
        self.assertEqual(len(self.course_list), 1)

    @parameterized.expand([
        ("names", ["Chemistry"]),
        ("subjects", ["CHEM"]),
        ("sections", ["B"]),
        ("years", [2023]),
        ("CRNs", [30960]),
        ("course_numbers", [1101]),
        ("credits", [0.500]),
        ("CGPA_points", [6.00]),
        ("terms", ["Fall"]),
        ("grades", ["A+"]),
        ("in_major", [True]),
        ("total_credits", 0.500),
        ("total_grade_points_earned", 6.00),
        ("major_credits", 0.500),
        ("major_grade_points_earned", 6.00),

    ])
    def test_all_properties(self, attr_name, value):
        self.assertEqual(getattr(self.course_list, attr_name), value)


if __name__ == "__main__":
    unittest.main()
