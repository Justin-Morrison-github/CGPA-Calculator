import unittest
from colorama import Fore
from Course import Course, Term
from parameterized import parameterized


class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course_dict = {
            "Year": 2023, "Term": "Fall", "CRN": 30960, "Subject": "CHEM", "Course Number": 1101, "Section": "B",
            "Course Title": "Chemistry", "Final Grade": "A+", "Credit": 0.500, "CGPA Points": 6.00, "Major": "True"}
        self.course = Course(self.course_dict)

    def test_init_empty_course(self):
        course = Course()
        self.assertEqual(course.year, None)
        self.assertEqual(course.term, None)
        self.assertEqual(course.CRN, None)
        self.assertEqual(course.subject, None)
        self.assertEqual(course.course_number, None)
        self.assertEqual(course.section, None)
        self.assertEqual(course.name, None)
        self.assertEqual(course.grade, None)
        self.assertEqual(course.credit, None)
        self.assertEqual(course.CGPA_points, None)
        self.assertEqual(course.in_major, None)

    def test_init_course_year(self):
        self.assertIsInstance(self.course.year, int)
        self.assertEqual(self.course.year, 2023)
        self.assertEqual(len(str(self.course.year)), 4)

        self.course_dict['Year'] = "Text"
        with self.assertRaises(ValueError):
            Course(self.course_dict)

    def test_init_course_term(self):
        self.assertIsInstance(self.course.term, str)
        self.assertEqual(self.course.term, "Fall")
        self.assertIn(self.course_dict["Term"],  Term.term_list)
        self.course_dict["Term"] = 1000
        with self.assertRaises(ValueError):
            Course(self.course_dict)

    def test_init_course_CRN(self):
        self.assertIsInstance(self.course.CRN, int)
        self.assertEqual(self.course.CRN, 30960)
        self.assertEqual(len(str(self.course.CRN)), 5)
        self.course_dict["CRN"] = 'Text'
        with self.assertRaises(ValueError):
            Course(self.course_dict)

    def test_init_course_subject(self):
        self.assertIsInstance(self.course.subject, str)
        self.assertEqual(self.course.subject, "CHEM")
        self.assertEqual(len(str(self.course.subject)), 4)

    def test_init_course_course_number(self):
        self.assertIsInstance(self.course.course_number, int)
        self.assertEqual(self.course.course_number, 1101)
        self.assertEqual(len(str(self.course.course_number)), 4)
        self.course_dict["Course Number"] = "Text"
        with self.assertRaises(ValueError):
            Course(self.course_dict)

    def test_init_course_section(self):
        self.assertIsInstance(self.course.section, str)
        self.assertEqual(self.course.section, "B")
        self.assertEqual(len(str(self.course.section)), 1)

    def test_init_course_name(self):
        self.assertIsInstance(self.course.section, str)
        self.assertEqual(self.course.name, "Chemistry")
        self.assertEqual(len(str(self.course.name)), 9)

    def test_init_course_grade(self):
        self.assertIsInstance(self.course.grade, str)
        self.assertEqual(self.course.grade, "A+")
        self.assertEqual(len(str(self.course.grade)), 2)
        self.assertEqual(self.course.grades[self.course.grade], 12.0)

    def test_init_course_credit(self):
        self.assertIsInstance(self.course.credit, float)
        self.assertEqual(self.course.credit, 0.500)
        self.assertTrue(self.course.credit % 0.25 == 0)

    def test_init_course_CGPA_points(self):
        self.assertIsInstance(self.course.CGPA_points, float)
        self.assertEqual(self.course.CGPA_points, 6.00)
        self.assertEqual(self.course.grades[self.course.grade] * self.course.credit, self.course.CGPA_points)
        self.assertEqual(self.course.grades[self.course.grade] * self.course.credit, 6.00)

    def test_init_course_in_major(self):
        self.assertIsInstance(self.course.in_major, bool)
        self.assertTrue(self.course.in_major)


# ---------------------------------------------------


    @parameterized.expand([
        ("A+", 12.0),
        ("A", 11.0),
        ("A-", 10.0),
        ("B+", 9.0),
        ("B", 8.0),
        ("B-", 7.0),
        ("C+", 6.0),
        ("C", 5.0),
        ("C-", 4.0),
        ("D+", 3.0),
        ("D", 2.0),
        ("D-", 1.0),
        ("F", 0.0),
        ("SAT", 0.0),
        ("UNS", 0.0),
    ])
    def test_course_grade_values_from_letter_grade(self, letter_grade, point_grade):
        self.assertEqual(self.course.grades[letter_grade], point_grade)

    def test_init_course_terms(self):
        self.assertEqual(Term.FALL, "Fall")
        self.assertEqual(Term.WINTER, "Winter")
        self.assertEqual(Term.SUMMER, "Summer")

    def test_init_course_valid_terms(self):
        self.assertEqual(self.course.valid_terms["Fall"], [2023])
        self.assertEqual(self.course.valid_terms["Winter"], [2024])
        self.assertEqual(self.course.valid_terms["Summer"], [])

        self.assertEqual(self.course.valid_terms[Term.FALL], [2023])
        self.assertEqual(self.course.valid_terms[Term.WINTER], [2024])
        self.assertEqual(self.course.valid_terms[Term.SUMMER], [])

    def test_init_course_grade_colors(self):
        self.assertEqual(self.course.grade_colors["A+"], f"{Fore.GREEN}A+{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["A"], f"{Fore.GREEN}A{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["A-"], f"{Fore.GREEN}A-{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["B+"], f"{Fore.BLUE}B+{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["B"], f"{Fore.BLUE}B{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["B-"], f"{Fore.BLUE}B-{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["C+"], f"{Fore.YELLOW}C+{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["C"], f"{Fore.YELLOW}C{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["C-"], f"{Fore.YELLOW}C-{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["D+"], f"{Fore.RED}D+{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["D"], f"{Fore.RED}D{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["D-"], f"{Fore.RED}D-{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["F"], f"{Fore.RED}F{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["SAT"], f"{Fore.GREEN}SAT{Fore.RESET}")
        self.assertEqual(self.course.grade_colors["UNS"], f"{Fore.RED}UNS{Fore.RESET}")

    def test_repr(self):
        self.assertEqual(repr(self.course),
                         f"{Fore.GREEN}A+{Fore.RESET}      0.50      Fall    2023    Chemistry                     Yes")


if __name__ == "__main__":
    unittest.main()
