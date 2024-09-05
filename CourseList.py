import time
from colorama import Fore


class CourseList:

    def __init__(self, course_list: list = None):
        if course_list:
            self.courses = course_list
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
            self.total_credits = sum(course.credit for course in self.courses)
            self.total_grade_points_earned = sum(course.CGPA_points for course in self.courses)
            self.major_credits = sum(course.credit for course in self.courses if course.in_major)
            self.major_grade_points_earned = sum(course.CGPA_points for course in self.courses if course.in_major)
        else:
            self.courses = []
            self.names = None
            self.subjects = None
            self.sections = None
            self.years = None
            self.CRNs = None
            self.course_numbers = None
            self.credits = None
            self.CGPA_points = None
            self.terms = None
            self.grades = None
            self.in_major = None
            self.total_credits = None
            self.total_grade_points_earned = None
            self.major_credits = None
            self.major_grade_points_earned = None

    def append(self, course):
        self.courses.append(course)

    def len(self):
        return len(self.courses)

    def __len__(self):
        return len(self.courses)

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

    def calculate_CGPA(self):
        return self.total_grade_points_earned / self.total_credits

    def calculate_major_CGPA(self):
        return self.major_grade_points_earned / self.major_credits
