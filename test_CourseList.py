import unittest
from colorama import Fore
from Course import Course, Term


class TestCourseList(unittest.TestCase):
    def setUp(self):
        course_dict = {
            "Year": 2023, "Term": "Fall", "CRN": 30960, "Subject": "CHEM", "Course Number": 1101, "Section": "B",
            "Course Title": "Chemistry", "Final Grade": "A+", "Credit": 0.500, "CGPA Points": 6.00, "Major": "True"}
        self.course = Course(course_dict)
