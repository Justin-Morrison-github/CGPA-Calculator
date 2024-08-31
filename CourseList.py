import time
from colorama import Fore


class CourseList:
    def __init__(self, list: list = None):
        if list:
            self.courses = list
            self.names = [course.name for course in self.courses]
            self.subjects = [course.subject for course in self.courses]
            self.sections = [course.section for course in self.courses]
            self.years = [course.year for course in self.courses]
            self.CRNs = [course.CRN for course in self.courses]
            self.course_numbers = [course.course_number for course in self.courses]
            self.credits = [course.credit for course in self.courses]
            self.CGPA_points = [course.CGPA_points for course in self.courses]
            self.terms = [course.term for course in self.courses]
            self.grades = [course.grade for course in self.courses]
            self.in_major = [course.in_major for course in self.courses]

        else:
            self.courses = []

    def append(self, course):
        self.courses.append(course)

    def __iter__(self):
        return iter(self.courses)

    def __repr__(self) -> str:
        for course in self.courses:
            print(course)
            time.sleep(0.05)

        return ""

    def filter_by_year(self, year: int):
        """
        Filters courses by the specified year.
        """
        return CourseList([course for course in self.courses if course.year == year])

    def filter_by_term(self, term):
        """
        Filters courses by the specified term.
        """
        return CourseList([course for course in self.courses if course.term == term])

    def filter_by_year_and_term(self, year: int, term):
        """
        Filters courses by the specified year and term.

        :param year: Integer of wanted year
        :param term: String of wanted term ('fall' or 'winter')
        :return: CourseList object containing courses that took place in that year and term
        """
        return CourseList([course for course in self.courses if course.year == year and course.term == term])

    @property
    def headers(self):
        columns = [
            ("Grade", 8),
            ("Credits", 10),
            ("Term", 8),
            ("Year", 8),
            ("Class", 30),
            ("In Major", 10)
        ]

        header_string = "".join([f"{title:<{width}}" for title, width in columns])
        return f"{Fore.CYAN}{header_string}{Fore.RESET}"

    @property
    def total_credits(self):
        """
        Calculates the total credits of all courses.
        """
        return sum(course.credit for course in self.courses)

    @property
    def major_credits(self):
        """
        Calculates the total credits of all courses.
        """
        return sum(course.credit for course in self.courses if course.in_major)

    @property
    def total_grade_points_earned(self):
        """
        Calculates the total credits of all courses.
        """
        return sum(course.CGPA_points for course in self.courses)

    @property
    def major_grade_points_earned(self):
        """
        Calculates the total credits of all courses.
        """
        return sum(course.CGPA_points for course in self.courses if course.in_major)

    def calculate_CGPA(self):
        return self.total_grade_points_earned / self.total_credits

    def calculate_major_CGPA(self):
        return self.major_grade_points_earned / self.major_credits
