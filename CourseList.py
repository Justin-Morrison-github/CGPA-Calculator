import time


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
            self.semesters = [course.semester for course in self.courses]
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

    def filter_by_semester(self, semester):
        """
        Filters courses by the specified semester.
        """
        return CourseList([course for course in self.courses if course.semester == semester])

    def filter_by_year_and_semester(self, year: int, semester):
        """
        Filters courses by the specified year and semester.

        :param year: Integer of wanted year
        :param semester: String of wanted semester ('fall' or 'winter')
        :return: CourseList object containing courses that took place in that year and semester
        """
        return CourseList([course for course in self.courses if course.year == year and course.semester == semester])

    @property
    def headers(self):
        columns = [
            ("Grade", 9),
            ("Credits", 17),
            ("Term", 8),
            ("Year", 8),
            ("Class", 31),
            ("In Major", 11)
        ]

        header_string = "".join([f"{title:<{width}}" for title, width in columns])
        return header_string

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
